# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:38

import re
from typing import Dict, Any, List

re_letter = re.compile(r'[a-zA-Z]')


def get_enum_upper(name, field, klass):
    from .. import upper

    return f"{upper(klass.name)}_{upper(field.name)}_{upper(name)}"


def get_enum_list(field, klass):
    from .. import upper

    return f"{upper(klass.name)}_{upper(field.name)}_LIST"


def get_index_params(index):
    params_list = list()
    for field_name in index['field_name_list']:
        params_list.append(f"'{field_name}'")
    return ", ".join(params_list)


def get_dao_params(field, klass) -> str:
    params_list = list()

    field_type = field.field_type
    field_detail_type = field.field_detail_type
    enums = field.values.get("enums", None)
    default_create = field.values.get("default_create", None)
    default_update = field.values.get("default_update", None)

    if field_type == "list":
        if field_detail_type == "str":
            params_list.append(f"fields.StringField()")
        elif field_detail_type == "int":
            params_list.append(f"fields.StringField()")
        elif field_detail_type == "objectid":
            params_list.append(f"fields.ObjectIdField()")
        elif field_detail_type == "dict":
            params_list.append(f"fields.DictField()")
        else:
            pass

    if enums:
        params_list.append(f"enums=consts.{get_enum_list(field, klass)}")

    if default_create is not None:
        if default_create in ('False', 'false') and field_type in ("bool",):
            params_list.append(f"default_create=False")
        elif default_create in ('True', 'true') and field_type in ("bool",):
            params_list.append(f"default_create=True")
        elif "{" in default_create and "}" in default_create:
            params_list.append(f"default_create={default_create[1:-1]}")
        elif enums:
            params_list.append(f"default_create=consts.{get_enum_upper(default_create, field, klass)}")
        elif field_type in ("int",):
            params_list.append(f"default_create={int(default_create)}")
        elif field_type in ("float",):
            params_list.append(f"default_create={float(default_create)}")
        else:
            params_list.append(f"default_create={default_create}")

    if default_update is not None:
        if default_update in ('False', 'false') and field_type in ("bool",):
            params_list.append(f"default_update=False")
        elif default_update in ('True', 'true') and field_type in ("bool",):
            params_list.append(f"default_update=True")
        elif "{" in default_update and "}" in default_update:
            params_list.append(f"default_update={default_update[1:-1]}")
        elif enums:
            params_list.append(f"default_update=consts.{get_enum_upper(default_update, field, klass)}")
        elif field_type in ("int",):
            params_list.append(f"default_update={int(default_update)}")
        elif field_type in ("float",):
            params_list.append(f"default_update={float(default_update)}")
        else:
            params_list.append(f"default_update={default_update}")

    # if "_description" in field:
    #     params_list.append(f"helper_text='{field['_description']}'")
    if params_list:
        return ", ".join(params_list) + ","
    else:
        return ""


def get_model_params(field, klass) -> str:
    params_list = list()

    field_type = field.field_type
    field_detail_type = field.field_detail_type

    required = field.values.get("required", False)
    unique = field.values.get("unique", False)
    nullable = field.values.get("nullable", False)

    if required:
        params_list.append(f"required=True")
    else:
        params_list.append(f"required=False")

    if unique:
        params_list.append(f"unique=True")
    else:
        params_list.append(f"unique=False")

    if nullable:
        params_list.append(f"allow_none=True")
    else:
        params_list.append(f"allow_none=False")

    if field_type == "list":
        if field_detail_type == "str":
            params_list.append(f"fields.StringField()")
        elif field_detail_type == "int":
            params_list.append(f"fields.StringField()")
        elif field_detail_type == "objectid":
            params_list.append(f"fields.ObjectIdField()")
        elif field_detail_type == "dict":
            params_list.append(f"fields.DictField()")
        else:
            pass

    if params_list:
        return ", ".join(params_list) + ","
    else:
        return ""


def get_token(token):
    value = f'self.tokens.get("{token["name"]}")'
    for f in token['func'][::-1]:
        value = f"{f}({value})"
    return value
