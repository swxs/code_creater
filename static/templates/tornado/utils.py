# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# @File    : {{model.name}}.py
# @AUTH    : model
# @Time    : {{current_time}}

import datetime
import models_fields
from BaseDocument import BaseDocument
from common.Utils.log_utils import getLogger

log = getLogger("utils/{self.model_name}")


class {{model.name | get_title}}(BaseDocument):
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

    def __init__(self, **kwargs):
        super({{model.name | get_title}}, self).__init__(**kwargs)