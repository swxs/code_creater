# -*- coding: utf-8 -*-
# @File    : {{model.name}}.py
# @AUTH    : model_creater

import datetime
import mongoengine as model
from ..consts.{{model.name | title}} import *
{% if "parent" in model and model["parent"] %}
from .{{apps_dict[app_name][model["parent"]].name | title}} import {{apps_dict[app_name][model["parent"]].name | title}}
{% else %}
from ...BaseModel import BaseModelDocument
{% endif %}
from mongoengine_utils import NAME_DICT


{% if "parent" in model and model["parent"] %}
class {{model.name | title}}({{apps_dict[app_name][model["parent"]].name | title}}):
{% else %}
class {{model.name | title}}(BaseModelDocument):
{% endif %}
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
        {% if "index_list" is in(model["meta"]) and model["meta"]["index_list"] %}
        'indexes': [
            {% for index in model["meta"]["index_list"] %}
            {
                'fields': [{{index | get_index_params}}],
                {% if index["is_uniq"] %}
                'unique ': True,
                {% endif %}
            },
            {% endfor %}
        ],
        {% endif %}
        {% if "allow_inheritance" is in(model["meta"]) and model["meta"]["allow_inheritance"] %}
        'allow_inheritance': True,
        {% endif %}
    }
    {% endif %}


NAME_DICT["{{model.name | title}}"] = {{model.name | title}}
