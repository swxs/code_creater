# -*- coding: utf-8 -*-
# @File    : {{app.name}}.py
# @AUTH    : model_creater
# @Time    : {{current_time}}

import datetime
import mongoengine as models
from common.Utils.log_utils import getLogger

log = getLogger("models/{{app.name}}")


class {{app.name | get_title}}(models.Document):
    {% for field in app.settings %}
    {% if field.type in ['datetime', ] %}
    {{field.name}} = models.DateTimeField({{field | get_params}})
    {% elif field.type in ['String', 'str', 'text'] %}
    {{field.name}} = models.StringField({{field | get_params}})
    {% elif field.type in ['Int', 'int', ] %}
    {{field.name}} = models.IntField({{field | get_params}})
    {% elif field.type in ['strlist', 'intlist'] %}
    {{field.name}} = models.ListField({{field | get_params}})
    {% elif field.type in ['Dict', 'dict'] %}
    {{field.name}} = models.DictField({{field | get_params}})
    {% elif field.type in ['Boolean', 'bool'] %}
    {{field.name}} = models.BooleanField({{field | get_params}})
    {% elif field.type in ['objectid'] %}
    {{field.name}} = models.ObjectIdField({{field | get_params}})
    {% endif %}
    {% endfor %}

    meta = {
        'indexes': [
        ]
    }