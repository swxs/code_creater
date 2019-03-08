# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:38

import re
from typing import (Dict, Any, List)

re_letter = re.compile(r'[a-zA-Z]')


def get_title(name: str) -> str:
    """
    驼峰表示: field_name=>FieldName
    :param name:
    :return:
    """
    if "_" in name:
        str = ""
        name_part_list = name.split("_")
        for name_part in name_part_list:
            str += name_part.title()
        return str
    else:
        return name.title()


def get_upper(name: str) -> str:
    """
    大写表示：field_name=>FIELDNAME
    :param name:
    :return:
    """
    if "_" in name:
        str = ""
        name_part_list = name.split("_")
        for name_part in name_part_list:
            str += name_part.upper()
        return str
    else:
        return name.upper()


def get_params(field: Dict[str, Any]) -> str:
    """
    设置字段model的参数列表
    :param field:
    :return:
    """

    def get_value(value):
        if isinstance(value, (int, float)):
            return f"{value}"
        else:
            return f"\"{value}\""

    return ", ".join(
        [
            "{0}={1}".format(key, get_value(value))
            for key, value in field.get('params', {}).items()
        ]
    )


def get_editable_field_list(field_list: List[Any]) -> List[Any]:
    return [
        field
        for field in field_list
        if field.get("settings", {}).get("editable", True)
    ]


def get_index_field_list(field_list: List[Any]) -> List[Any]:
    return [
        field
        for field in field_list
        if field.get("settings", {}).get("indexes", False)
    ]


def get_argument_type(field: Dict[str, Any]) -> str:
    return "get_arguments" if field.get('type') in ["List"] else "get_argument"


def concat_field_selected_name_with_comma(field_list: List[Any]) -> str:
    return ", ".join(f"{field.get('name')}={field.get('name')}" for field in field_list)
