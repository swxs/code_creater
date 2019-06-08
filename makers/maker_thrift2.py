# -*- coding: utf-8 -*-
# @File    : maker_thrift2.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:25

import os
from .maker import Maker
from .registry import factory


@factory.add_makers
class MakerThrift2(Maker):
    name = "thrift2"

    def total_make(self, app_name, models, task):
        tmpl = os.path.join(task.get('framework'), 'protocols', 'model.thrift.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, 'protocols', 'model.thrift')
        self.render(tmpl, {'models': models, 'app_name': app_name}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'protocols', 'main.thrift.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, 'protocols', 'main.thrift')
        self.render_once(tmpl, {'models': models, 'app_name': app_name}, dst_file)

        tmpl = os.path.join(task.get('framework'), '__init__.py.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, '__init__.py')
        self.render_once(tmpl, {'models': models, 'app_name': app_name}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'base_client.py.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, 'base_client.py')
        self.render(tmpl, {'models': models, 'app_name': app_name}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'base_server.py.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, 'base_server.py')
        self.render(tmpl, {'models': models, 'app_name': app_name}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'client.py.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, 'client.py')
        self.render_once(tmpl, {'models': models, 'app_name': app_name}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'server.py.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, 'server.py')
        self.render_once(tmpl, {'models': models, 'app_name': app_name}, dst_file)

    def make(self, app_name, model, task):
        pass
