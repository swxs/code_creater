# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# @File    : {{app.name}}.py
# @AUTH    : model_creater
# @Time    : {{current_time}}

import datetime
import models_fields
from BaseDocument import BaseDocument
from common.Utils.log_utils import getLogger

log = getLogger("utils/{self.model_name}")


class {{app.name | get_title}}(BaseDocument):
    {% for field in app.settings %}
    {% if field.type in ['DateTime', ] %}
    {{field.name}} = models_fields.DateTimeField({{field | get_params}})
    {% elif field.type in ['String', ] %}
    {{field.name}} = models_fields.StringField({{field | get_params}})
    {% elif field.type in ['Int', ] %}
    {{field.name}} = models_fields.IntField({{field | get_params}})
    {% elif field.type in ['List',] %}
    {{field.name}} = models_fields.ListField({{field | get_params}})
    {% elif field.type in ['Dict', ] %}
    {{field.name}} = models_fields.DictField({{field | get_params}})
    {% elif field.type in ['Boolean', ] %}
    {{field.name}} = models_fields.BooleanField({{field | get_params}})
    {% elif field.type in ['objectid'] %}
    {{field.name}} = models_fields.ObjectIdField({{field | get_params}})
    {% endif %}
    {% endfor %}

    def __init__(self, **kwargs):
        super({{app.name | get_title}}, self).__init__(**kwargs)