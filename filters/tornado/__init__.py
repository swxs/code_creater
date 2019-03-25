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


def get_enum_upper(name, field, model):
    return f"{get_upper(model.name)}_{get_upper(field.get('field_name'))}_{get_upper(name)}"


def get_enum_list(field, model):
    return f"{get_upper(model.name)}_{get_upper(field.get('field_name'))}_LIST"


def get_index_params(index):
    params_list = list()
    for field_name in index['field_name_list']:
        params_list.append(f"'{field_name}'")
    return ", ".join(params_list)


def get_model_params(field, model) -> str:
    params_list = list()
    if "enums" in field:
        params_list.append(f"enums={get_enum_list(field, model)}")
    if "default" in field:
        if field["default"] in ('False', 'false'):
            params_list.append(f"default=False")
        elif field["default"] in ('True', 'true'):
            params_list.append(f"default=true")
        elif "enums" in field:
            params_list.append(f"default={get_enum_upper(field['default'], field, model)}")
        elif field["field_type"] in ("int",):
            params_list.append(f"default={int(field['default'])}")
        elif field["field_type"] in ("float",):
            params_list.append(f"default={float(field['default'])}")
        else:
            params_list.append(f"default='{field['default']}'")
    if "help_text" in field:
        params_list.append(f"helper_text='{field['help_text']}'")
    return ", ".join(params_list)


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
