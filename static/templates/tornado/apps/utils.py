# -*- coding: utf-8 -*-
# @File    : {{model.name}}.py
# @AUTH    : model_creater

from ..commons.{{model.name | title}} import {{model.name | title}} as Base{{model.name | title}}


class {{model.name | title}}(Base{{model.name | title}}):
    def __init__(self, **kwargs):
        super({{model.name | title}}, self).__init__(**kwargs)
