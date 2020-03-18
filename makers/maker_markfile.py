# -*- coding: utf-8 -*-
# @File    : maker_markfile.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:19

import os
from .maker import Maker
from .registry import factory


@factory.add_makers
class MakerMarkfile(Maker):
    name = "markfile"

    def total_make(self, app, task):
        tmpl = os.path.join(task.get('framework'), 'base.md.jinja2')
        dst_file = os.path.join(task.get('target'), app.name, 'base.md')
        self.render(tmpl, {'app': app}, dst_file)

    def make(self, app, klass, task):
        tmpl = os.path.join(task.get('framework'), 'create.md.jinja2')
        dst_file = os.path.join(task.get('target'), app.name, klass.name, 'create.md')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'copy.md.jinja2')
        dst_file = os.path.join(task.get('target'), app.name, klass.name, 'copy.md')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'select.md.jinja2')
        dst_file = os.path.join(task.get('target'), app.name, klass.name, 'select.md')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'select_list.md.jinja2')
        dst_file = os.path.join(task.get('target'), app.name, klass.name, 'select_list.md')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'update.md.jinja2')
        dst_file = os.path.join(task.get('target'), app.name, klass.name, 'update.md')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'delete.md.jinja2')
        dst_file = os.path.join(task.get('target'), app.name, klass.name, 'delete.md')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)
