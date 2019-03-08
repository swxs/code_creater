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

    def make(self, app, task):
        tmpl = os.path.join(task.get('framework'), 'create.md')
        dst_file = os.path.join(task.get('target'), "docs", app.name, 'create.md')
        self.render(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'select.md')
        dst_file = os.path.join(task.get('target'), "docs", app.name, 'select.md')
        self.render(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'update.md')
        dst_file = os.path.join(task.get('target'), "docs", app.name, 'update.md')
        self.render(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'delete.md')
        dst_file = os.path.join(task.get('target'), "docs", app.name, 'delete.md')
        self.render(tmpl, {'app': app}, dst_file)
