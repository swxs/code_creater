# -*- coding: utf-8 -*-
# @File    : {{model.name}}.py
# @AUTH    : model_creater
# @Time    : {{current_time}}

import datetime
import mongoengine as model
from common.Utils.log_utils import getLogger

log = getLogger("model/{{model.name}}")


class {{model.name | get_title}}(model.Document):
    {% for field in model.field_list %}
    {% if field.field_type == "datetime" %}
    {{field.field_name}} = model.DateTimeField({{field|get_model_params(model)}})
    {% elif field.field_type == "str" %}
    {{field.field_name}} = model.StringField({{field|get_model_params(model)}})
    {% elif field.field_type == "int" %}
    {{field.field_name}} = model.IntField({{field|get_model_params(model)}})
    {% elif field.field_type == "list" %}
    {{field.field_name}} = model.ListField({{field|get_model_params(model)}})
    {% elif field.field_type == "dict" %}
    {{field.field_name}} = model.DictField({{field|get_model_params(model)}})
    {% elif field.field_type == "boolean" %}
    {{field.field_name}} = model.BooleanField({{field|get_model_params(model)}})
    {% elif field.field_type == "objectid" %}
    {{field.field_name}} = model.ObjectIdField({{field|get_model_params(model)}})
    {% else %}
    {{field.field_name}} = model.StringField({{field|get_model_params(model)}})
    {% endif %}
    {% endfor %}

    {% if "meta" is in(model) %}
    meta = {
        'indexes': [
            {% for index in model["meta"]["index_list"] %}
            {
                'fields': [{{index | get_index_params}}],
                {% if index["is_uniq"] %}
                'unique ': True,
                {% endif %}
            },
            {% endfor %}
        ]
    }
    {% endif %}