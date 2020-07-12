# -*- coding: utf-8 -*-
# @File    : maker_tornado.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:14

import os
from .maker import Maker
from .registry import factory
from utils.utils import get_dir_path


@factory.add_makers
class MakerTornado(Maker):
    name = "tornado"

    def total_make(self, app, task):
        # 创建 app 下的 __init__.py 文件, 只创建一次
        dst_path = get_dir_path(task.get('target'), app.name)
        tmpl = os.path.join(task.get('framework'), 'apps', '__init__.py.jinja2')
        dst_file = os.path.join(dst_path, f'__init__.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        # 创建 app/utils 下的 __init__.py 文件, 只创建一次
        dst_path = get_dir_path(task.get('target'), app.name, 'utils')
        tmpl = os.path.join(task.get('framework'), 'apps', '__init__.py.jinja2')
        dst_file = os.path.join(dst_path, f'__init__.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        # 创建 app 下的 custom_handlers.py 文件, 只创建一次
        dst_path = get_dir_path(task.get('target'), app.name)
        tmpl = os.path.join(task.get('framework'), 'apps', 'custom_handlers.py.jinja2')
        dst_file = os.path.join(dst_path, f'custom_handlers.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        # 创建 app下的 consts.py 文件, 记录映射信息
        dst_path = get_dir_path(task.get('target'), app.name)
        tmpl = os.path.join(task.get('framework'), 'apps', 'consts.py.jinja2')
        dst_file = os.path.join(dst_path, 'consts.py')
        self.render(tmpl, {'app': app}, dst_file)

        # 创建 app下的 models.py 文件, 记录模块信息
        dst_path = get_dir_path(task.get('target'), app.name)
        tmpl = os.path.join(task.get('framework'), 'apps', 'models.py.jinja2')
        dst_file = os.path.join(dst_path, 'models.py')
        self.render(tmpl, {'app': app}, dst_file)

        # 创建 app 下的 dao.py 文件, 记录映射信息
        dst_path = get_dir_path(task.get('target'), app.name)
        tmpl = os.path.join(task.get('framework'), 'apps', 'dao.py.jinja2')
        dst_file = os.path.join(dst_path, f'dao.py')
        self.render(tmpl, {'app': app}, dst_file)

        # 创建 app 下的 handlers.py 文件, 记录处理类信息
        dst_path = get_dir_path(task.get('target'), app.name)
        tmpl = os.path.join(task.get('framework'), 'apps', 'handlers.py.jinja2')
        dst_file = os.path.join(dst_path, f'handlers.py')
        self.render(tmpl, {'app': app}, dst_file)

    def make(self, app, klass, task):
        # 创建 app/utils 下的 utils.py 文件, 记录模块自定义操作信息
        dst_path = get_dir_path(task.get('target'), app.name, 'utils')
        tmpl = os.path.join(task.get('framework'), 'apps', 'utils.py.jinja2')
        dst_file = os.path.join(dst_path, f'{klass.name}.py')
        self.render_once(tmpl, {'klass': klass, 'app': app}, dst_file)
