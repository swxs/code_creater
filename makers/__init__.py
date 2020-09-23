# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @AUTH    : swxs
# @Time    : 2019/2/26 15:07

import os
import sys
import settings
from ..utils.Helper_productor import Productor
from .maker import Maker


class MakerProductor(Productor):
    def __init__(
        self,
        root_dir: object,
        start_dir: object,
        base_module: object = None,
        temp_module: object = None,
        pattern: object = '*.py',
    ):
        super().__init__(root_dir, start_dir, base_module=base_module, temp_module=temp_module, pattern=pattern)


base_path = os.path.dirname(os.path.abspath(__file__))
productor = MakerProductor(settings.SITE_ROOT, base_path, Maker, Maker, "*.py")
