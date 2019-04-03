# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:38

import re
from typing import (Dict, Any, List)

re_letter = re.compile(r'[a-zA-Z]')


def get_enum_upper(name, field, model):
    from .. import get_upper
    return f"{get_upper(model.name)}_{get_upper(field.get('field_name'))}_{get_upper(name)}"


def get_enum_list(field, model):
    from .. import get_upper
    return f"{get_upper(model.name)}_{get_upper(field.get('field_name'))}_LIST"


def get_index_params(index):
    params_list = list()
    for field_name in index['field_name_list']:
        params_list.append(f"'{field_name}'")
    return ", ".join(params_list)


def get_utils_params(field, model) -> str:
    params_list = list()
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
