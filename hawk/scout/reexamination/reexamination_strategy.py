# SPDX-FileCopyrightText: 2022 Carnegie Mellon University
#
# SPDX-License-Identifier: GPL-2.0-only

import queue
from abc import ABCMeta, abstractmethod
from typing import List, Tuple

from ..core.model import Model


class ReexaminationStrategy(metaclass=ABCMeta):

    @property
    @abstractmethod
    def reexamines_old_results(self) -> bool:
        """Returns True if old results are reexamined by strategy"""
        pass

    @abstractmethod
    def get_new_queues(self, model: Model, 
                       old_queues: List[queue.PriorityQueue]) -> Tuple[List[queue.PriorityQueue], int]:
        """Generates a new queue with reexamined results"""
        pass
