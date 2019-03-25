# -*- coding: utf-8 -*-
# @File    : maker_tornado.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:14

import os
from .maker import Maker
from .registry import factory
from utils.Helper_dir import get_dir_path


@factory.add_makers
class MakerTornado(Maker):
    name = "tornado"

    def make(self, app_name, model, task):
        # 创建 __init__.py 文件
        dst_path = get_dir_path(task.get('target'), app_name)
        tmpl = os.path.join(task.get('framework'), '__init__.py')
        dst_file = os.path.join(dst_path, f'__init__.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        dst_path = get_dir_path(task.get('target'), app_name, 'consts')
        tmpl = os.path.join(task.get('framework'), 'consts.py')
        dst_file = os.path.join(dst_path, f'{model.name}.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        dst_path = get_dir_path(task.get('target'), app_name, 'models')
        tmpl = os.path.join(task.get('framework'), 'models.py')
        dst_file = os.path.join(dst_path, f'{model.name}.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        dst_path = get_dir_path(task.get('target'), app_name, 'utils')
        tmpl = os.path.join(task.get('framework'), 'utils.py')
        dst_file = os.path.join(dst_path, f'{model.name}.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        dst_path = get_dir_path(task.get('target'), app_name, 'urls')
        tmpl = os.path.join(task.get('framework'), 'urls.py')
        dst_file = os.path.join(dst_path, f'{model.name}.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        dst_path = get_dir_path(task.get('target'), app_name, 'views')
        tmpl = os.path.join(task.get('framework'), 'views.py')
        dst_file = os.path.join(dst_path, f'{model.name}.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)
