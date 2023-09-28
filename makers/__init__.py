# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @AUTH    : swxs
# @Time    : 2019/2/26 15:07

import os
import sys

from .. import core
from ..utils.Helper_productor import Productor
from .maker import Maker


base_path = os.path.dirname(os.path.abspath(__file__))
maker_productor = Productor(core.path.SITE_ROOT, base_path, Maker, Maker, "*.py")
