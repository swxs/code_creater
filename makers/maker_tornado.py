# -*- coding: utf-8 -*-
# @File    : maker_tornado.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:14

import os
from .maker import Maker
from .registry import factory


@factory.add_makers
class MakerTornado(Maker):
    name = "tornado"

    def make(self, app, task):
        dst_path = os.path.join(task.get('target'), app.get('name'))
        self.add_init(dst_path)

        tmpl = os.path.join(task.get('framework'), 'consts.py')
        dst_file = os.path.join(task.get('target'), 'consts', f'{app.name}.py')
        self.render(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'models.py')
        dst_file = os.path.join(task.get('target'), 'models', f'{app.name}.py')
        self.render(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'utils.py')
        dst_file = os.path.join(task.get('target'), 'utils', f'{app.name}.py')
        self.render(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'urls.py')
        dst_file = os.path.join(task.get('target'), 'urls', f'{app.name}.py')
        self.render(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join(task.get('framework'), 'views.py')
        dst_file = os.path.join(task.get('target'), 'views', f'{app.name}.py')
        self.render(tmpl, {'app': app}, dst_file)
