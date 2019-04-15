# -*- coding: utf-8 -*-
# @File    : {{model.name}}.py
# @AUTH    : model_creater
{% for field in model.field_list %}
{% if "enums" is in(field) %}

{% for enum in field["enums"] %}
{{enum["value"] | get_enum_upper(field, model) }} = {{ loop.index }}
{% endfor %}

{{field | get_enum_list(model)}} = [
{% for enum in field["enums"] %}
    ({{enum["value"] | get_enum_upper(field, model) }}, '{{enum["name"]}}'),
{% endfor %}
]
{% endif %}
{% endfor %}
