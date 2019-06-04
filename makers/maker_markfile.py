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

    def total_make(self, app_name, models, task):
        tmpl = os.path.join(task.get('framework'), 'base.md.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, 'base.md')
        self.render(tmpl, {'models': models, 'app_name': app_name}, dst_file)

    def make(self, app_name, model, task):
        tmpl = os.path.join(task.get('framework'), 'create.md.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, model.name, 'create.md')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'copy.md.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, model.name, 'copy.md')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'select.md.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, model.name, 'select.md')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'select_list.md.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, model.name, 'select_list.md')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'update.md.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, model.name, 'update.md')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'delete.md.jinja2')
        dst_file = os.path.join(task.get('target'), app_name, model.name, 'delete.md')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)
