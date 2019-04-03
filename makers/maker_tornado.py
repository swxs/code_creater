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
        # 创建 app 下的 __init__.py 文件, 只创建一次
        dst_path = get_dir_path(task.get('target'), app_name)
        tmpl = os.path.join(task.get('framework'), 'apps', '__init__.py')
        dst_file = os.path.join(dst_path, f'__init__.py')
        self.render_once(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        # 创建 app/consts 下的 __init__.py 文件, 只创建一次
        dst_path = get_dir_path(task.get('target'), app_name, 'consts')
        tmpl = os.path.join(task.get('framework'), 'apps', '__init__.py')
        dst_file = os.path.join(dst_path, f'__init__.py')
        self.render_once(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        # 创建 app/models 下的 __init__.py 文件, 只创建一次
        dst_path = get_dir_path(task.get('target'), app_name, 'models')
        tmpl = os.path.join(task.get('framework'), 'apps', '__init__.py')
        dst_file = os.path.join(dst_path, f'__init__.py')
        self.render_once(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        # 创建 app/utils 下的 __init__.py 文件, 只创建一次
        dst_path = get_dir_path(task.get('target'), app_name, 'utils')
        tmpl = os.path.join(task.get('framework'), 'apps', '__init__.py')
        dst_file = os.path.join(dst_path, f'__init__.py')
        self.render_once(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        # 创建 app/urls 下的 __init__.py 文件, 只创建一次
        dst_path = get_dir_path(task.get('target'), app_name, 'urls')
        tmpl = os.path.join(task.get('framework'), 'apps', '__init__.py')
        dst_file = os.path.join(dst_path, f'__init__.py')
        self.render_once(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        # 创建 app/views 下的 __init__.py 文件, 只创建一次
        dst_path = get_dir_path(task.get('target'), app_name, 'views')
        tmpl = os.path.join(task.get('framework'), 'apps', '__init__.py')
        dst_file = os.path.join(dst_path, f'__init__.py')
        self.render_once(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        # 创建 app/consts 下的 consts.py 文件, 记录映射信息
        dst_path = get_dir_path(task.get('target'), app_name, 'consts')
        tmpl = os.path.join(task.get('framework'), 'apps', 'consts.py')
        dst_file = os.path.join(dst_path, f'{model.name}.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        # 创建 app/models 下的 models.py 文件, 记录模块信息
        dst_path = get_dir_path(task.get('target'), app_name, 'models')
        tmpl = os.path.join(task.get('framework'), 'apps', 'models.py')
        dst_file = os.path.join(dst_path, f'{model.name}.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        # 创建 app/utils 下的 utils.py 文件, 记录模块操作信息
        dst_path = get_dir_path(task.get('target'), app_name, 'utils')
        tmpl = os.path.join(task.get('framework'), 'apps', 'utils.py')
        dst_file = os.path.join(dst_path, f'{model.name}.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        # 创建 app/urls 下的 urls.py 文件, 记录模块操作信息
        dst_path = get_dir_path(task.get('target'), app_name, 'urls')
        tmpl = os.path.join(task.get('framework'), 'apps', 'urls.py')
        dst_file = os.path.join(dst_path, f'{model.name}.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        # 创建 app/views 下的 views.py 文件, 记录模块操作信息
        dst_path = get_dir_path(task.get('target'), app_name, 'views')
        tmpl = os.path.join(task.get('framework'), 'apps', 'views.py')
        dst_file = os.path.join(dst_path, f'{model.name}.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)
