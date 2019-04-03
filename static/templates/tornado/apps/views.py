# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# @File    : {{model.name}}.py
# @AUTH    : model
# @Time    : {{current_time}}

from base import BaseHandler
from api.consts.const import undefined
from ..utils.{{model.name | get_title}} import {{model.name | get_title}}
from common.Utils.log_utils import getLogger

log = getLogger("views/{{model.name}}")


class {{model.name | get_title}}Handler(BaseHandler):
    @BaseHandler.ajax_base()
    def get(self, {{model.name | get_lower}}_id=None):
        if {{model.name | get_lower}}_id:
            {{model.name | get_lower}} = {{model.name | get_title}}.select(id={{model.name | get_lower}}_id)
            return {{model.name}}.to_front()
        else:
            {{model.name | get_lower}}_list = {{model.name | get_title}}.filter()
            return [{{model.name | get_lower}}.to_front() for {{model.name | get_lower}} in {{model.name | get_lower}}_list]

    @BaseHandler.ajax_base()
    def post(self):
        params = self.get_all_arguments()
        {{model.name | get_lower}} = {{model.name | get_title}}.create(params)
        return {{model.name | get_lower}}.to_front()

    @BaseHandler.ajax_base()
    def put(self, {{model.name | get_lower}}_id):
        params = self.get_all_arguments()
        {{model.name | get_lower}} = {{model.name | get_title}}.select(id={{model.name | get_lower}}_id)
        {{model.name | get_lower}} = {{model.name | get_lower}}.update(params)
        return {{model.name | get_lower}}.to_front()

    @BaseHandler.ajax_base()
    def patch(self, {{model.name | get_lower}}_id):
        params = self.get_all_arguments()
        {{model.name | get_lower}} = {{model.name | get_title}}.select(id={{model.name | get_lower}}_id)
        {{model.name | get_lower}} = {{model.name | get_lower}}.update(params)
        return {{model.name | get_lower}}.to_front()

    @BaseHandler.ajax_base()
    def delete(self, {{model.name | get_lower}}_id):
        {{model.name | get_lower}} = {{model.name | get_title}}.select(id={{model.name | get_lower}}_id)
        {{model.name | get_lower}}.delete()
        return None

    def set_default_headers(self):
        self._headers.add("version", "1")
