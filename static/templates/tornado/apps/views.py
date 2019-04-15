# -*- coding: utf-8 -*-
# @File    : {{model.name}}.py
# @AUTH    : model

from base import BaseHandler
from common.Utils.log_utils import getLogger
from ...BaseConsts import *
from ..utils.{{model.name | get_title}} import {{model.name | get_title}}

log = getLogger("views/{{model.name}}")


class {{model.name | get_title}}Handler(BaseHandler):
    @BaseHandler.ajax_base()
    def get(self, {{model.name | get_lower}}_id=None):
        if {{model.name | get_lower}}_id:
            {{model.name | get_lower}} = {{model.name | get_title}}.select(id={{model.name | get_lower}}_id)
            return {{model.name | get_lower}}.to_front()
        else:
            {{model.name | get_lower}}_list = {{model.name | get_title}}.filter()
            return [{{model.name | get_lower}}.to_front() for {{model.name | get_lower}} in {{model.name | get_lower}}_list]

    @BaseHandler.ajax_base()
    def post(self, {{model.name | get_lower}}_id=None):
        if {{model.name | get_lower}}_id:
            params = dict()
            {# 如果存在继承， 添加父类字段 #}
            {% if "parent" in model and model["parent"] %}
            {% for field in apps_dict[app_name][model["parent"]].field_list %}
            {% if field.field_type == "list" %}
            params['{{field.field_name}}'] = self.get_arguments('{{field.field_name}}', undefined)
            {% else %}
            params['{{field.field_name}}'] = self.get_argument('{{field.field_name}}', undefined)
            {% endif %}
            {% endfor %}
            {% endif %}
            {# 添加字段 #}
            {% for field in model.field_list %}
            {% if field.field_type == "list" %}
            params['{{field.field_name}}'] = self.get_arguments('{{field.field_name}}', undefined)
            {% else %}
            params['{{field.field_name}}'] = self.get_argument('{{field.field_name}}', undefined)
            {% endif %}
            {% endfor %}
            {{model.name | get_lower}} = {{model.name | get_title}}.select(id={{model.name | get_lower}}_id)
            {{model.name | get_lower}} = {{model.name | get_lower}}.copy(**params)
            return {{model.name | get_lower}}.id
        else:
            params = dict()
            {# 如果存在继承， 添加父类字段 #}
            {% if "parent" in model and model["parent"] %}
            {% for field in apps_dict[app_name][model["parent"]].field_list %}
            {% if field.field_type == "list" %}
            params['{{field.field_name}}'] = self.get_arguments('{{field.field_name}}', [])
            {% else %}
            params['{{field.field_name}}'] = self.get_argument('{{field.field_name}}', None)
            {% endif %}
            {% endfor %}
            {% endif %}
            {# 添加字段 #}
            {% for field in model.field_list %}
            {% if field.field_type == "list" %}
            params['{{field.field_name}}'] = self.get_arguments('{{field.field_name}}', [])
            {% else %}
            params['{{field.field_name}}'] = self.get_argument('{{field.field_name}}', None)
            {% endif %}
            {% endfor %}
            {{model.name | get_lower}} = {{model.name | get_title}}.create(**params)
            return {{model.name | get_lower}}.id

    @BaseHandler.ajax_base()
    def put(self, {{model.name | get_lower}}_id=None):
        params = dict()
        {# 如果存在继承， 添加父类字段 #}
        {% if "parent" in model and model["parent"] %}
        {% for field in apps_dict[app_name][model["parent"]].field_list %}
        {% if field.field_type == "list" %}
        params['{{field.field_name}}'] = self.get_arguments('{{field.field_name}}', [])
        {% else %}
        params['{{field.field_name}}'] = self.get_argument('{{field.field_name}}', None)
        {% endif %}
        {% endfor %}
        {% endif %}
        {# 添加字段 #}
        {% for field in model.field_list %}
        {% if field.field_type == "list" %}
        params['{{field.field_name}}'] = self.get_arguments('{{field.field_name}}', [])
        {% else %}
        params['{{field.field_name}}'] = self.get_argument('{{field.field_name}}', None)
        {% endif %}
        {% endfor %}
        {{model.name | get_lower}} = {{model.name | get_title}}.select(id={{model.name | get_lower}}_id)
        {{model.name | get_lower}} = {{model.name | get_lower}}.update(**params)
        return {{model.name | get_lower}}.id

    @BaseHandler.ajax_base()
    def patch(self, {{model.name | get_lower}}_id=None):
        params = dict()
        {# 如果存在继承， 添加父类字段 #}
        {% if "parent" in model and model["parent"] %}
        {% for field in apps_dict[app_name][model["parent"]].field_list %}
        {% if field.field_type == "list" %}
        params['{{field.field_name}}'] = self.get_arguments('{{field.field_name}}', undefined)
        {% else %}
        params['{{field.field_name}}'] = self.get_argument('{{field.field_name}}', undefined)
        {% endif %}
        {% endfor %}
        {% endif %}
        {# 添加字段 #}
        {% for field in model.field_list %}
        {% if field.field_type == "list" %}
        params['{{field.field_name}}'] = self.get_arguments('{{field.field_name}}', undefined)
        {% else %}
        params['{{field.field_name}}'] = self.get_argument('{{field.field_name}}', undefined)
        {% endif %}
        {% endfor %}
        {{model.name | get_lower}} = {{model.name | get_title}}.select(id={{model.name | get_lower}}_id)
        {{model.name | get_lower}} = {{model.name | get_lower}}.update(**params)
        return {{model.name | get_lower}}.id

    @BaseHandler.ajax_base()
    def delete(self, {{model.name | get_lower}}_id=None):
        {{model.name | get_lower}} = {{model.name | get_title}}.select(id={{model.name | get_lower}}_id)
        {{model.name | get_lower}}.delete()
        return None

    def set_default_headers(self):
        self._headers.add("version", "1")
