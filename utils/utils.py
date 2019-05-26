import os
from tornado.util import ObjectDict


def get_dir_path(path, *paths):
    dir_path = os.path.join(path, *paths)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def dict2objectdict(adict):
    for key, value in adict.items():
        if isinstance(value, dict):
            new_value = dict2objectdict(value)
            adict[key] = new_value
    obj = ObjectDict(adict)
    return obj
