# SPDX-FileCopyrightText: 2022 Carnegie Mellon University <satya-group@lists.andrew.cmu.edu>
#
# SPDX-License-Identifier: GPL-2.0-only

from typing import Optional

from hawk.core.object_provider import ObjectProvider

class ResultProvider(object):

    def __init__(self, obj: ObjectProvider, score: float, model_version: Optional[int]): 
        self.id = obj.id
        self.content = obj.content
        self.attributes = obj.attributes
        self.gt = obj.gt
        self.score = score
        self.model_version = model_version
