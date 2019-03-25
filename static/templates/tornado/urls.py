# -*- coding: utf-8 -*-
# @File    : {{model.name}}.py
# @AUTH    : model
# @Time    : {{current_time}}

from tornado.web import url
import api.views.{{model.name}} as views

url_mapping = [
    url(r"/api/{{model.name}}/create/", views.{{model.name | get_title}}Handler),
    url(r"/api/{{model.name}}/list/", views.{{model.name | get_title}}Handler),
    url(r"/api/{{model.name}}/select/([a-zA-Z0-9&%\.~-]+)/", views.{{model.name | get_title}}Handler),
    url(r"/api/{{model.name}}/update/([a-zA-Z0-9&%\.~-]+)/", views.{{model.name | get_title}}Handler),
    url(r"/api/{{model.name}}/delete/([a-zA-Z0-9&%\.~-]+)/", views.{{model.name | get_title}}Handler),
]
