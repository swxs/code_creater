# -*- coding: utf-8 -*-
# @File    : {{model.name}}.py
# @AUTH    : model

import datetime
import mongoengine_utils as model
from ..models.{{model.name | get_title }} import {{model.name | get_title}} as _
{% if "parent" in model and model["parent"] %}
from .{{apps_dict[app_name][model["parent"]].name | get_title}} import {{apps_dict[app_name][model["parent"]].name | get_title}}
{% else %}
from ...BaseUtils import BaseUtils
{% endif %}
from common.Utils.log_utils import getLogger

log = getLogger("utils/{self.model_name}")


{% if "parent" in model and model["parent"] %}
class {{model.name | get_title}}({{apps_dict[app_name][model["parent"]].name | get_title}}):
{% else %}
class {{model.name | get_title}}(BaseUtils):
{% endif %}
    {% for field in model.field_list %}
    {% if field.field_type == "datetime" %}
    {{field.field_name}} = model.DateTimeField({{field|get_utils_params(model)}})
    {% elif field.field_type == "str" %}
    {{field.field_name}} = model.StringField({{field|get_utils_params(model)}})
    {% elif field.field_type == "int" %}
    {{field.field_name}} = model.IntField({{field|get_utils_params(model)}})
    {% elif field.field_type == "list" %}
    {{field.field_name}} = model.ListField({{field|get_utils_params(model)}})
    {% elif field.field_type == "dict" %}
    {{field.field_name}} = model.DictField({{field|get_utils_params(model)}})
    {% elif field.field_type == "boolean" %}
    {{field.field_name}} = model.BooleanField({{field|get_utils_params(model)}})
    {% elif field.field_type == "objectid" %}
    {{field.field_name}} = model.ObjectIdField({{field|get_utils_params(model)}})
    {% else %}
    {{field.field_name}} = model.StringField({{field|get_utils_params(model)}})
    {% endif %}
    {% endfor %}

    def __init__(self, **kwargs):
        super({{model.name | get_title}}, self).__init__(**kwargs)

    {% for field in model.field_list %}
    {% if "ref" is in(field) %}
    {% set ref_model = apps_dict[app_name][field["ref"]] %}
    @property
    def {{ref_model["name"] | get_lower}}(self):
        from .{{ref_model["name"] | get_title}} import {{ref_model["name"] | get_title}}
        return {{ref_model["name"] | get_title}}.get_{{ref_model["name"] | get_lower}}_by_{{ref_model["name"] | get_lower}}_id(self.{{field.field_name}})

    {% endif %}
    {% endfor %}
    @classmethod
    def get_{{model.name | get_lower}}_by_{{model.name | get_lower}}_id(cls, {{model.name | get_lower}}_id):
        return cls.select(id={{model.name | get_lower}}_id)

    {% if ("meta" is in(model)) and ("listorder") is in(model["meta"]) %}
    def create(self, **kwargs):
        {% for field in model.field_list %}
        {{field.field_name}} = {{model.name | get_title}}.first().{{field.field_name}} + 100000
        {% endfor %}
        super({{model.name | get_title}}, self).create(**kwargs)

    {% endif %}