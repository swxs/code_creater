import os
from typing import (
    Any,
    Dict,
)


class ObjectDict(Dict[str, Any]):
    """Makes a dictionary behave like an object, with attribute-style access."""

    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name: str, value: Any) -> None:
        self[name] = value


def dict2objectdict(adict):
    for key, value in adict.items():
        if isinstance(value, dict):
            new_value = dict2objectdict(value)
            adict[key] = new_value
    obj = ObjectDict(adict)
    return obj


def get_dir_path(path, *paths):
    dir_path = os.path.join(path, *paths)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path
