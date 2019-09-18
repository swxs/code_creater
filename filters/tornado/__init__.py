# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:38

import re
from typing import (Dict, Any, List)

re_letter = re.compile(r'[a-zA-Z]')


def get_enum_upper(name, field, model):
    from .. import upper
    return f"{upper(model.name)}_{upper(field.get('field_name'))}_{upper(name)}"


def get_enum_list(field, model):
    from .. import upper
    return f"{upper(model.name)}_{upper(field.get('field_name'))}_LIST"


def get_index_params(index):
    params_list = list()
    for field_name in index['field_name_list']:
        params_list.append(f"'{field_name}'")
    return ", ".join(params_list)


def get_utils_params(field, model) -> str:
    params_list = list()
    if "no_create" in field:
        params_list.append(f"create=False")
    return ", ".join(params_list)


def get_model_params(field, model) -> str:
    params_list = list()

    if field["field_type"] == "list":
        if "field_detail_type" not in field:
            params_list.append(f"fields.StringField()")
        elif field["field_detail_type"] == "str":
            params_list.append(f"fields.StringField()")
        elif field["field_detail_type"] == "int":
            params_list.append(f"fields.StringField()")
        elif field["field_detail_type"] == "objectid":
            params_list.append(f"fields.ObjectIdField()")
        elif field["field_detail_type"] == "dict":
            params_list.append(f"fields.DictField()")
        else:
            params_list.append(f"fields.StringField()")

    params_list.append(f"allow_none=True")
    if "enums" in field:
        params_list.append(f"enums={get_enum_list(field, model)}")
    if "default" in field:
        if field["default"] in ('False', 'false'):
            params_list.append(f"default=False")
        elif field["default"] in ('True', 'true'):
            params_list.append(f"default=True")
        elif "enums" in field:
            params_list.append(f"default={get_enum_upper(field['default'], field, model)}")
        elif field["field_type"] in ("int",):
            params_list.append(f"default={int(field['default'])}")
        elif field["field_type"] in ("float",):
            params_list.append(f"default={float(field['default'])}")
        else:
            params_list.append(f"default='{field['default']}'")
    if "_description" in field:
        params_list.append(f"helper_text='{field['_description']}'")
    return ", ".join(params_list)
