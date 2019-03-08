# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# @File    : {{app.name}}.py
# @AUTH    : model_creater
# @Time    : {{current_time}}

from base import BaseHandler
from api.consts.const import undefined
from api.utils.{{app.name}} import {{app.name | get_title}}
from common.Utils.log_utils import getLogger

log = getLogger("views/{{app.name}}")


class {{app.name | get_title}}Handler(BaseHandler):
    @BaseHandler.ajax_base()
    def get(self, {{app.name}}_id=None):
        if {{app.name}}_id:
            {{app.name}} = {{app.name | get_title}}.select(id={{app.name}}_id)
            return {{app.name}}.to_front()
        else:
            {{app.name}}_list = {{app.name | get_title}}.filter()
            return [{{app.name}}.to_front() for {{app.name}} in {{app.name}}_list]

    @BaseHandler.ajax_base()
    def post(self):
        {% for field in app.settings | get_editable_field_list %}
        {% if field.type in ['List',] %}
        {{field.name}} = self.get_arguments("{{field.name}}", None)
        {% else %}
        {{field.name}} = self.get_argument("{{field.name}}", None)
        {% endif %}
        {% endfor %}
        {{app.name}} = {{app.name | get_title}}.create({{ app.settings | get_editable_field_list | concat_field_selected_name_with_comma }})
        return {{app.name}}.to_front()

    @BaseHandler.ajax_base()
    def put(self, {{app.name}}_id):
        {% for field in app.settings | get_editable_field_list %}
        {% if field.type in ['List'] %}
        {{field.name}} = self.get_arguments("{{field.name}}", None)
        {% else %}
        {{field.name}} = self.get_argument("{{field.name}}", None)
        {% endif %}
        {% endfor %}
        {{app.name}} = {{app.name | get_title}}.select(id={{app.name}}_id)
        {{app.name}} = {{app.name}}.update({{ app.settings | get_editable_field_list | concat_field_selected_name_with_comma }})
        return {{app.name}}.to_front()

    @BaseHandler.ajax_base()
    def patch(self, {{app.name}}_id):
        {% for field in app.settings | get_editable_field_list %}
        {% if field.type in ['List',] %}
        {{field.name}} = self.get_arguments("{{field.name}}", undefined)
        {% else %}
        {{field.name}} = self.get_argument("{{field.name}}", undefined)
        {% endif %}
        {% endfor %}
        {{app.name}} = {{app.name | get_title}}.select(id={{app.name}}_id)
        {{app.name}} = {{app.name}}.update({{ app.settings | get_editable_field_list | concat_field_selected_name_with_comma }})
        return {{app.name}}.to_front()

    @BaseHandler.ajax_base()
    def delete(self, {{app.name}}_id):
        {{app.name}} = {{app.name | get_title}}.select(id={{app.name}}_id)
        {{app.name}}.delete()
        return None

    def set_default_headers(self):
        self._headers.add("version", "{{app.info.get('version', 1)}}")