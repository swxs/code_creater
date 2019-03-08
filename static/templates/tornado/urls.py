# -*- coding: utf-8 -*-
# @File    : {{app.name}}.py
# @AUTH    : model_creater
# @Time    : {{current_time}}

from tornado.web import url
import api.views.{{app.name}} as views

url_mapping = [
    url(r"/api/{{app.name}}/create/", views.{{app.name | get_title}}Handler),
    url(r"/api/{{app.name}}/list/", views.{{app.name | get_title}}Handler),
    url(r"/api/{{app.name}}/select/([a-zA-Z0-9&%\.~-]+)/", views.{{app.name | get_title}}Handler),
    url(r"/api/{{app.name}}/update/([a-zA-Z0-9&%\.~-]+)/", views.{{app.name | get_title}}Handler),
    url(r"/api/{{app.name}}/delete/([a-zA-Z0-9&%\.~-]+)/", views.{{app.name | get_title}}Handler),
]
