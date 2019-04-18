# -*- coding: utf-8 -*-
# @File    : {{model.name}}.py
# @AUTH    : model

from tornado.web import url
from ..views.{{model.name | title}} import {{model.name | title}}Handler

url_mapping = [
    url(r"/api/{{app_name | lower}}/{{model.name}}/(?:([a-zA-Z0-9&%\.~-]+)/)?", {{model.name | title}}Handler),
]
