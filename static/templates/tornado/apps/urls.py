# -*- coding: utf-8 -*-
# @File    : {{model.name}}.py
# @AUTH    : model
# @Time    : {{current_time}}

from tornado.web import url
from ..views.{{model.name | get_title}} import {{model.name | get_title}}Handler


url_mapping = [
    url(r"/api/{{model.name}}/(([a-zA-Z0-9&%\.~-]+)/)?", {{model.name | get_title}}Handler),
]
