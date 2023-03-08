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
    default = field.values.get("default", None)
    default_create = field.values.get("default_create", None)
    default_update = field.values.get("default_update", None)

    if field.values.get("no_create"):
        params_list.append(f"create=False")

    if enums:
        params_list.append(f"enums=consts.{get_enum_list(field, klass)}")
    if default is not None:
        if default in ('False', 'false') and field_type in ("bool",):
            params_list.append(f"default=False")
        elif default in ('True', 'true') and field_type in ("bool",):
            params_list.append(f"default=True")
        elif enums:
            params_list.append(f"default=consts.{get_enum_upper(default, field, klass)}")
        elif field_type in ("int",):
            params_list.append(f"default={int(default)}")
        elif field_type in ("float",):
            params_list.append(f"default={float(default)}")
        else:
            params_list.append(f"default={default}")
    if default_create is not None:
        params_list.append(f"default_create={default_create}")
    if default_update is not None:
        params_list.append(f"default_update={default_update}")
    return ", ".join(params_list)


def get_dao_params(field, klass) -> str:
    params_list = list()

    field_type = field.field_type
    field_detail_type = field.field_detail_type
    requirement = field.values.get("requirement", False)
    enums = field.values.get("enums", None)
    default = field.values.get("default", None)

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

    if requirement:
        params_list.append(f"allow_none=False")
    else:
        params_list.append(f"allow_none=True")

    if enums:
        params_list.append(f"enums=consts.{get_enum_list(field, klass)}")
    if default is not None:
        if default in ('False', 'false') and field_type in ("bool",):
            params_list.append(f"default=False")
        elif default in ('True', 'true') and field_type in ("bool",):
            params_list.append(f"default=True")
        elif enums:
            params_list.append(f"default=consts.{get_enum_upper(default, field, klass)}")
        elif field_type in ("int",):
            params_list.append(f"default={int(default)}")
        elif field_type in ("float",):
            params_list.append(f"default={float(default)}")
        else:
            params_list.append(f"default={default}")
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
    requirement = field.values.get("requirement", False)
    enums = field.values.get("enums", None)
    default = field.values.get("default", None)
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

    if requirement:
        params_list.append(f"requirement=True")
    else:
        params_list.append(f"requirement=False")

    if enums:
        params_list.append(f"enums=consts.{get_enum_list(field, klass)}")
    if default is not None:
        if default in ('False', 'false') and field_type in ("bool",):
            params_list.append(f"default=False")
        elif default in ('True', 'true') and field_type in ("bool",):
            params_list.append(f"default=True")
        elif enums:
            params_list.append(f"default=consts.{get_enum_upper(default, field, klass)}")
        elif field_type in ("int",):
            params_list.append(f"default={int(default)}")
        elif field_type in ("float",):
            params_list.append(f"default={float(default)}")
        else:
            params_list.append(f"default={default}")

    # if "_description" in field:
    #     params_list.append(f"helper_text='{field['_description']}'")
    if params_list:
        return ", ".join(params_list) + ","
    else:
        return ""


def get_token(token):
    value = f'self.tokens.get("{token["name"]}")'
    for f in token['func'][::-1]:
        value = f"{f}({value})"
    return value
