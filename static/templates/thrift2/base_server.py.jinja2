# -*- coding: utf-8 -*-
# @File    : base_server.py
# @AUTH    : model_creater

import os
import json
import thriftpy2
from thriftpy2.rpc import make_server
from rpc.utils import render_thrift
from api.{{app_name | title}}.utils.{{app_name | title}} import {{app_name | title}}


rpc_dir = os.path.abspath(os.path.dirname(__file__))
{{app_name | lower}}_thrift = thriftpy2.load(rpc_dir + "/protocols/main.thrift", module_name="{{app_name | lower}}_thrift")

class BaseDispatcher(object):
    {% for model_name, model in models.items() %}
    @render_thrift({{app_name | lower}}_thrift.CreateResult)
    def create_{{app_name | lower}}_{{model_name | lower}}(self, **kwargs):
        result = {{app_name | lower}}_thrift.CreateResult
        {{model_name | lower}} = {{model_name | title}}.create(**kwargs)
        result.id = {{model_name | lower}}.id
        result.code = 0
        return result

    @render_thrift({{app_name | lower}}_thrift.UpdateResult)
    def update_{{app_name | lower}}_{{model_name|lower}}(self, {{model_name | lower}}_id, **kwargs):
        result = {{app_name | lower}}_thrift.UpdateResult()
        {{model_name | lower}} = {{model_name | title}}.select(id={{model_name | lower}}_id)
        {{model_name | lower}} = {{model_name | lower}}.update(**kwargs)
        result.id = {{model_name | lower}}.id
        result.code = 0
        return result

    @render_thrift({{app_name | lower}}_thrift.DeleteResult)
    def delete_{{app_name | lower}}_{{model_name | lower}}(self, {{model_name | lower}}_id):
        result = {{app_name | lower}}_thrift.DeleteResult()
        {{model_name | lower}} = {{model_name | title}}.select(id={{model_name | lower}}_id)
        {{model_name | lower}}.delete()
        result.code = 0
        return result

    @render_thrift({{app_name | lower}}_thrift.{{model_name | title}}Result)
    def select_{{app_name | lower}}_{{model_name|lower}}(self, {{model_name | lower}}_id):
        result = {{model_name | lower}}_thrift.{{model_name | title}}Result()
        {{model_name | lower}} = {{model_name | title}}.select(id={{model_name | lower}}_id)
        result_object = {{app_name | lower}}_thrift.{{model_name | lower}}
        result_object.id = str({{model_name | lower}}.id)
        {% for field in model.field_list %}
            {% if field.field_type == "datetime" %}
        result_object.{{field.field_name}} = {{model.name|lower}}.{{field.field_name}}.strftime('%Y-%m-%d %H:%M:%S.%f')
            {% elif field.field_type == "str" %}
        result_object.{{field.field_name}} = {{model.name|lower}}.{{field.field_name}}
            {% elif field.field_type == "int" %}
        result_object.{{field.field_name}} = {{model.name | lower}}.{{field.field_name}}
            {% elif field.field_type == "list" %}
                {% if field.field_detail_type == "str" %}
        result_object.{{field.field_name}} = {{model.name | lower}}.{{field.field_name}}
                {% elif field.field_detail_type == "int" %}
        result_object.{{field.field_name}} = {{model.name | lower}}.{{field.field_name}}
                {% elif field.field_detail_type == "objectid" %}
        result_object.{{field.field_name}} = [str(i) for i in {{model.name|lower}}.{{field.field_name}}]
                {% elif field.field_detail_type == "dict" %}
        result_object.{{field.field_name}} = [json.dumps(i) for i in {{model.name|lower}}.{{field.field_name}}]
                {% else %}
        result_object.{{field.field_name}} = {{model.name | lower}}.{{field.field_name}}
                {% endif %}
            {% elif field.field_type == "dict" %}
        result_object.{{field.field_name}} = json.dumps({{model.name|lower}}.{{field.field_name}})
            {% elif field.field_type == "boolean" %}
        result_object.{{field.field_name}} = {{model.name|lower}}.{{field.field_name}}
            {% elif field.field_type == "objectid" %}
        result_object.{{field.field_name}} = str({{model.name|lower}}.{{field.field_name}})
            {% else %}
        result_object.{{field.field_name}} = {{model.name|lower}}.{{field.field_name}}
            {% endif %}
        {% endfor %}
        result.{{model.name|lower}} = result_object
        result.code = 0
        return result

    @render_thrift({{app_name | lower}}_thrift.{{model.name}}SearchResult)
    def list_{{app_name | lower}}_{{model.name | lower}}(self):
        result = {{app_name | lower}}_thrift.{{model.name | title}}SearchResult()
        {{model.name | lower}}_list = {{model_name | title}}.filter()
        result_object_list = []
        for {{model.name|lower}} in {{model.name | lower}}_list:
            result_object = {{app_name | lower}}_thrift.{{model_name | lower}}
            result_object.id = str({{model_name | lower}}.id)
            {% for field in model.field_list %}
                {% if field.field_type == "datetime" %}
            result_object.{{field.field_name}} = {{model.name | lower}}.{{field.field_name}}.strftime('%Y-%m-%d %H:%M:%S.%f')
                {% elif field.field_type == "str" %}
            result_object.{{field.field_name}} = {{model.name | lower}}.{{field.field_name}}
                {% elif field.field_type == "int" %}
            result_object.{{field.field_name}} = {{model.name | lower}}.{{field.field_name}}
                {% elif field.field_type == "list" %}
                    {% if field.field_detail_type == "str" %}
            result_object.{{field.field_name}} = {{model.name | lower}}.{{field.field_name}}
                    {% elif field.field_detail_type == "int" %}
            result_object.{{field.field_name}} = {{model.name | lower}}.{{field.field_name}}
                    {% elif field.field_detail_type == "objectid" %}
            result_object.{{field.field_name}} = [str(i) for i in {{model.name | lower}}.{{field.field_name}}]
                    {% elif field.field_detail_type == "dict" %}
            result_object.{{field.field_name}} = [json.dumps(i) for i in {{model.name | lower}}.{{field.field_name}}]
                    {% else %}
            result_object.{{field.field_name}} = {{model.name | lower}}.{{field.field_name}}
                    {% endif %}
                {% elif field.field_type == "dict" %}
            result_object.{{field.field_name}} = json.dumps({{model.name | lower}}.{{field.field_name}})
                {% elif field.field_type == "boolean" %}
            {{field.field_name}} = {{model.name | lower}}.result_object.{{field.field_name}}
                {% elif field.field_type == "objectid" %}
            result_object.{{field.field_name}} = str({{model.name | lower}}.{{field.field_name}})
                {% else %}
            result_object.{{field.field_name}} = {{model.name | lower}}.{{field.field_name}}
                {% endif %}
            {% endfor %}
            result_object_list.append(result_object)
        result.code = 0
        result.{{model_name|lower}}_list = result_object_list
        return result

{% endfor %}


if __name__ == '__main__':
    from ..client_pool import get_rpc_server_host, get_rpc_server_port

    server = make_server(
        {{app_name | lower}}_thrift.{{app_name | title}}Service,
        BaseDispatcher(),
        get_rpc_server_host('{{app_name | title}}'),
        get_rpc_server_port('{{app_name | title}}'),
        client_timeout=None
    )
    server.serve()