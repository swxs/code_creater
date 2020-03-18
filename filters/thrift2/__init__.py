# -*- coding: utf-8 -*-
# @File    : __init__.py
# @AUTH    : swxs
# @Time    : 2019/4/17 10:06

def get_ttype(field):
    ttype_dict = {
        'str': 'string',
        'int': 'i32',
        'bool': 'bool',
        'strlist': 'list<string>',
        'intlist': 'list<inting>',
        'objectid': 'string'
    }
    return ttype_dict.get(field.field_type, 'string')