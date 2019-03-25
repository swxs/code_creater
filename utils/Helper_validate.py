# -*- coding: utf-8 -*-

import re

try:
    from typing.re import Pattern
except:
    Pattern = re.compile(r"")


class RegType:
    ALL = r'.*'
    APP = r'[Aa]pp'
    COMMIT = r'#'
    META = r'meta'
    DEFAULT = r'default'
    ENUM = r'enum'
    ALLOW_INHERITANCE = r'allow_inheritance'
    PARENT = r'parent'
    INDEX = r'index'
    UNIQ = r'uniq'


class Validate:
    @classmethod
    def _find_reg(self, reg_type):
        if reg_type in RegType.__dict__:
            return reg_type
        if isinstance(reg_type, Pattern):
            return reg_type.pattern
        else:
            return reg_type

    @classmethod
    def has(cls, value, reg_type=RegType.ALL):
        try:
            return re.search(r'{0}'.format(cls._find_reg(reg_type)), value, re.M) is not None
        except TypeError:
            return False

    @classmethod
    def any(cls, value, reg_type_list=None):
        try:
            return any(Validate.has(value, reg_type=reg_type) for reg_type in reg_type_list)
        except TypeError:
            return False

    @classmethod
    def start_with(cls, value, reg_type=RegType.ALL):
        try:
            return re.match(r'^({0})'.format(cls._find_reg(reg_type)), value, re.M) is not None
        except TypeError:
            return False

    @classmethod
    def end_with(cls, value, reg_type=RegType.ALL):
        try:
            return re.match(r'.*?({0})$'.format(cls._find_reg(reg_type)), value, re.M) is not None
        except TypeError:
            return False

    @classmethod
    def check(cls, value, reg_type=RegType.ALL):
        try:
            return re.match(r'^{0}$'.format(cls._find_reg(reg_type)), value, re.M) is not None
        except TypeError:
            return False

    @classmethod
    def clear(cls, value, reg_type=RegType.ALL):
        try:
            return re.sub(r'{0}'.format(cls._find_reg(reg_type)), "", value, re.M)
        except TypeError:
            return False

    @classmethod
    def getall(cls, value, reg_type=RegType.ALL):
        try:
            result = re.findall(r'({0})+'.format(cls._find_reg(reg_type)), value, re.M)
            if len(result) > 0 and isinstance(result[0], tuple):
                return [value[0] for value in result]
            return result
        except TypeError:
            return []
