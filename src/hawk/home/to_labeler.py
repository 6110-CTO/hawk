# SPDX-FileCopyrightText: 2024 Carnegie Mellon University
#
# SPDX-License-Identifier: GPL-2.0-only

from __future__ import annotations

import io
import threading
import time
from dataclasses import dataclass, field
from itertools import count
from pathlib import Path
from typing import TYPE_CHECKING

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from logzero import logger
from prometheus_client import Counter, Gauge, Histogram

from .stats import (
    HAWK_LABELED_OBJECTS,
    HAWK_LABELER_QUEUED_LENGTH,
    HAWK_LABELER_QUEUED_TIME,
)
from .to_scout import Label
from .utils import tailf

matplotlib.use("agg")

if TYPE_CHECKING:
    from .to_scout import ScoutQueue


@dataclass
class LabelerDiskQueue:
    mission_id: str
    scout_queue: ScoutQueue
    mission_dir: Path
    label_queue_size: int = 0

    token_semaphore: threading.BoundedSemaphore = field(init=False, repr=False)

    labeled_objects: Counter = field(init=False)
    queue_length: Gauge = field(init=False)
    queued_time: Histogram = field(init=False)

    def __post_init__(self) -> None:
        if self.label_queue_size <= 0:
            self.label_queue_size = 9999

        # track number of unlabeled items being handled by the labeler
        self.token_semaphore = threading.BoundedSemaphore(self.label_queue_size)

        # track labeler statistics
        self.labeled_objects = HAWK_LABELED_OBJECTS
        for label in [0, 1]:  # Hint to prometheus_client which labels we may use
            HAWK_LABELED_OBJECTS.labels(
                mission=self.mission_id, labeler="disk", label=label
            )

        self.queue_length = HAWK_LABELER_QUEUED_LENGTH.labels(
            mission=self.mission_id, labeler="disk"
        )
        self.queued_time = HAWK_LABELER_QUEUED_TIME.labels(
            mission=self.mission_id, labeler="disk"
        )

    def start(self) -> LabelerDiskQueue:
        # start the threads that interact with the labeler
        threading.Thread(target=self.labeler_to_home, daemon=True).start()
        threading.Thread(target=self.home_to_labeler, daemon=True).start()
        return self

    def home_to_labeler(self) -> None:
        unlabeled_jsonl = self.mission_dir / "unlabeled.jsonl"
        tile_dir = self.mission_dir / "images"
        tile_dir.mkdir(exist_ok=True)

        for index in count():
            # block until the labeler is ready to accept more.
            self.token_semaphore.acquire()

            # pull the next result from the priority queue
            result = self.scout_queue.get()

            logger.info(
                f"Labeling {result.object_id} {result.scout_index} {result.score}"
            )

            # write result image file to disk
            tile_jpeg = tile_dir.joinpath(f"{index:06}.jpeg")
            if result.object_id.endswith(".npy"):  # for radar missions with .npy files
                self.gen_heatmap(result.data, tile_jpeg)
            else:
                tile_jpeg.write_bytes(result.data)
            logger.info(f"SAVED TILE {tile_jpeg}")

            # update label_queue_length metric
            self.queue_length.inc()

            # append metadata to unlabeled.jsonl file
            meta_json = result.to_json(index=index, queued_time=time.time())
            with unlabeled_jsonl.open("a") as f:
                f.write(f"{meta_json}\n")

            # logger.info(f"Meta: {count:06} {meta_json}")
            self.scout_queue.task_done()

    def labeler_to_home(self) -> None:
        labeled_jsonl = self.mission_dir / "labeled.jsonl"
        labeled_jsonl.touch()

        logger.info("Started reading labeled results from labeler")

        # read label results and forward to the scouts
        with labeled_jsonl.open() as fp:
            # Seek to the end of the labeled.jsonl file, assuming we've already
            # forwarded all labels, there really is no good way to track what
            # we've done because the semaphore we use doesn't survive a restart.
            fp.seek(0, 2)

            for label_json in tailf(fp):
                now = time.time()

                # update label_queue_length metric
                self.queue_length.dec()

                # release next unlabeled result to labeler
                self.token_semaphore.release()

                label = Label.from_json(label_json)
                self.scout_queue.put(label)

                # update stats
                self.labeled_objects.labels(
                    mission=self.mission_id, labeler="disk", label=label.image_label
                ).inc()

                # track time it took to apply label
                if label.queued_time is not None:
                    queue_elapsed = now - label.queued_time
                    self.queued_time.observe(queue_elapsed)

    def gen_heatmap(self, data_: bytes, tile_path: Path) -> None:
        with io.BytesIO(data_) as bytes_file:
            data = np.load(bytes_file, allow_pickle=True)
        plt.imshow(
            data.sum(axis=2).transpose(), cmap="viridis", interpolation="nearest"
        )
        plt.xticks([0, 16, 32, 48, 63], [-13, -6.5, 0, 6.5, 13], fontsize=8)
        plt.yticks([0, 64, 128, 192, 255], [50, 37.5, 25, 12.5, 0])
        plt.xlabel("velocity (m/s)")
        plt.ylabel("range (m)")
        # plt.title("RD Map")
        plt.savefig(tile_path, bbox_inches="tight")
        plt.close("all")
