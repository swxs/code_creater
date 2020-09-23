# -*- coding: utf-8 -*-
# @File    : maker_markfile.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:19

import os
from .maker import Maker


class MakerMarkfile(Maker):
    name = "markfile"

    def total_make(self, app):
        tmpl = os.path.join(self.output.get('framework'), 'base.md.jinja2')
        dst_file = os.path.join(self.target, app.name, 'base.md')
        self.render(tmpl, {'app': app}, dst_file)

    def make(self, app, klass):
        tmpl = os.path.join(self.output.get('framework'), 'create.md.jinja2')
        dst_file = os.path.join(self.target, app.name, klass.name, 'create.md')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)

        tmpl = os.path.join(self.output.get('framework'), 'copy.md.jinja2')
        dst_file = os.path.join(self.target, app.name, klass.name, 'copy.md')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)

        tmpl = os.path.join(self.output.get('framework'), 'select.md.jinja2')
        dst_file = os.path.join(self.target, app.name, klass.name, 'select.md')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)

        tmpl = os.path.join(self.output.get('framework'), 'select_list.md.jinja2')
        dst_file = os.path.join(self.target, app.name, klass.name, 'select_list.md')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)

        tmpl = os.path.join(self.output.get('framework'), 'update.md.jinja2')
        dst_file = os.path.join(self.target, app.name, klass.name, 'update.md')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)

        tmpl = os.path.join(self.output.get('framework'), 'delete.md.jinja2')
        dst_file = os.path.join(self.target, app.name, klass.name, 'delete.md')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)
