# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:37

from functools import lru_cache


@lru_cache()
def get_base_name(name: str):
    """
    驼峰表示: field_name=>FieldName
    :param name:
    :return:
    """
    name_list = []
    current_str = ""
    for code in name:
        if code in ("_",):
            name_list.append(current_str)
            current_str = ""
        elif code.upper() == code:
            if current_str != "":
                name_list.append(current_str.lower())
                current_str = code.lower()
            else:
                current_str = code.lower()
        else:
            current_str += code
    name_list.append(current_str)
    return [name for name in name_list if name]


def get_title(name: str) -> str:
    """
    驼峰表示: field_name=>FieldName
    :param name:
    :return:
    """
    name_list = get_base_name(name)
    return "".join(name.title() for name in name_list)


def get_lower(name: str) -> str:
    """
    小写表示：Field_Name, FieldName, fieldName, field_name, FIELD_NAME=>field_name
    :param name:
    :return:
    """
    name_list = get_base_name(name)
    return "_".join(name.lower() for name in name_list)


def get_upper(name: str) -> str:
    """
    大写表示：Field_Name, FieldName, fieldName, field_name, FIELD_NAME=>FIELD_NAME
    :param name:
    :return:
    """
    name_list = get_base_name(name)
    return "_".join(name.upper() for name in name_list)
