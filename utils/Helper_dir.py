# -*- coding: utf-8 -*-
# @File    : Helper_dir.py
# @AUTH    : swxs
# @Time    : 2019/3/25 16:02

import os


def get_dir_path(path, *paths):
    dir_path = os.path.join(path, *paths)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path
