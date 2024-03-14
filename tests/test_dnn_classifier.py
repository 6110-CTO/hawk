# Copyright (c) 2024 Carnegie Mellon University
# SPDX-License-Identifier: GPLv2-only

from pathlib import Path

import pytest
import torch
import torchvision

from hawk.scout.trainer.dnn_classifier.model import DNNClassifierModel


@pytest.mark.cuda
@pytest.mark.benchmark(group="dnn_classifier_model")
@pytest.mark.parametrize("batch_size", [1, 10])
def test_dnn_classifier(benchmark, testcontext, objectprovider, batch_size):
    model_path = Path(__file__).parent.joinpath("assets", "model.pth")
    if not model_path.exists():
        pytest.skip("Missing model to load with DNNClassiferModel")

    if not torch.cuda.is_available():
        pytest.skip("CUDA not available")

    benchmark.extra_info.update(
        {
            "torch_version": torch.__version__,
            "torchvision_version": torchvision.__version__,
        }
    )

    args = dict()
    model = DNNClassifierModel(args, model_path, 0, "hawk", testcontext)

    def infer(model, requests):
        return list(model.infer(requests))

    requests = [objectprovider] * batch_size
    results = benchmark(infer, model, requests)

    assert len(results) == batch_size
