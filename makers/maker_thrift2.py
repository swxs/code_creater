# -*- coding: utf-8 -*-
# @File    : maker_thrift2.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:25

import os
from .maker import Maker
from ..utils.utils import get_dir_path


class MakerThrift2(Maker):
    name = "thrift2"

    def total_make(self, app):
        dst_path = get_dir_path(self.target, app.name, 'rpc')

        tmpl = os.path.join(self.output.get('framework'), 'protocols', 'model.thrift.jinja2')
        dst_file = os.path.join(dst_path, 'protocols', 'model.thrift')
        self.render(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(self.output.get('framework'), 'protocols', 'main.thrift.jinja2')
        dst_file = os.path.join(dst_path, 'protocols', 'main.thrift')
        self.render_once(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(self.output.get('framework'), '__init__.py.jinja2')
        dst_file = os.path.join(dst_path, '__init__.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(self.output.get('framework'), 'base_client.py.jinja2')
        dst_file = os.path.join(dst_path, 'base_client.py')
        self.render(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(self.output.get('framework'), 'base_server.py.jinja2')
        dst_file = os.path.join(dst_path, 'base_server.py')
        self.render(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(self.output.get('framework'), 'client.py.jinja2')
        dst_file = os.path.join(dst_path, 'client.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(self.output.get('framework'), 'server.py.jinja2')
        dst_file = os.path.join(dst_path, 'server.py')
        self.render_once(tmpl, {'app': app}, dst_file)

    def make(self, app, klass):
        pass
