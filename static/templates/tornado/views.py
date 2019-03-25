# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# @File    : {{model.name}}.py
# @AUTH    : model
# @Time    : {{current_time}}

from base import BaseHandler
from api.consts.const import undefined
from api.utils.{{model.name}} import {{model.name | get_title}}
from common.Utils.log_utils import getLogger

log = getLogger("views/{{model.name}}")


class {{model.name | get_title}}Handler(BaseHandler):
    @BaseHandler.ajax_base()
    def get(self, {{model.name}}_id=None):
        if {{model.name}}_id:
            {{model.name}} = {{model.name | get_title}}.select(id={{model.name}}_id)
            return {{model.name}}.to_front()
        else:
            {{model.name}}_list = {{model.name | get_title}}.filter()
            return [{{model.name}}.to_front() for {{model.name}} in {{model.name}}_list]

    @BaseHandler.ajax_base()
    def post(self):
        {% for field in model.settings | get_editable_field_list %}
        {% if field.type in ['List',] %}
        {{field.name}} = self.get_arguments("{{field.name}}", None)
        {% else %}
        {{field.name}} = self.get_argument("{{field.name}}", None)
        {% endif %}
        {% endfor %}
        {{model.name}} = {{model.name | get_title}}.create({{ model.settings | get_editable_field_list | concat_field_selected_name_with_comma }})
        return {{model.name}}.to_front()

    @BaseHandler.ajax_base()
    def put(self, {{model.name}}_id):
        {% for field in model.settings | get_editable_field_list %}
        {% if field.type in ['List'] %}
        {{field.name}} = self.get_arguments("{{field.name}}", None)
        {% else %}
        {{field.name}} = self.get_argument("{{field.name}}", None)
        {% endif %}
        {% endfor %}
        {{model.name}} = {{model.name | get_title}}.select(id={{model.name}}_id)
        {{model.name}} = {{model.name}}.update({{ model.settings | get_editable_field_list | concat_field_selected_name_with_comma }})
        return {{model.name}}.to_front()

    @BaseHandler.ajax_base()
    def patch(self, {{model.name}}_id):
        {% for field in model.settings | get_editable_field_list %}
        {% if field.type in ['List',] %}
        {{field.name}} = self.get_arguments("{{field.name}}", undefined)
        {% else %}
        {{field.name}} = self.get_argument("{{field.name}}", undefined)
        {% endif %}
        {% endfor %}
        {{model.name}} = {{model.name | get_title}}.select(id={{model.name}}_id)
        {{model.name}} = {{model.name}}.update({{ model.settings | get_editable_field_list | concat_field_selected_name_with_comma }})
        return {{model.name}}.to_front()

    @BaseHandler.ajax_base()
    def delete(self, {{model.name}}_id):
        {{model.name}} = {{model.name | get_title}}.select(id={{model.name}}_id)
        {{model.name}}.delete()
        return None

    def set_default_headers(self):
        self._headers.add("version", "1")