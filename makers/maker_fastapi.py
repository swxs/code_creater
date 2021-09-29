# -*- coding: utf-8 -*-
# @File    : maker_tornado.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:14

import os
from .maker import Maker
from ..utils.utils import get_dir_path


class MakerFastapi(Maker):
    name = "fastapi"

    def total_make(self, app):
        # 创建 app 下的 __init__.py 文件, 只创建一次
        dst_path = get_dir_path(self.target, app.name)
        tmpl = os.path.join(self.output.get('framework'), 'apps', '__init__.py.jinja2')
        dst_file = os.path.join(dst_path, f'__init__.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        # 创建 app/utils 下的 __init__.py 文件, 只创建一次
        dst_path = get_dir_path(self.target, app.name, 'utils')
        tmpl = os.path.join(self.output.get('framework'), 'apps', '__init__.py.jinja2')
        dst_file = os.path.join(dst_path, f'__init__.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        # 创建 app 下的 custom_handlers.py 文件, 只创建一次
        dst_path = get_dir_path(self.target, app.name)
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'custom_handlers.py.jinja2')
        dst_file = os.path.join(dst_path, f'custom_handlers.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        # 创建 app下的 consts.py 文件, 记录映射信息
        dst_path = get_dir_path(self.target, app.name)
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'consts.py.jinja2')
        dst_file = os.path.join(dst_path, 'consts.py')
        self.render(tmpl, {'app': app}, dst_file)

        # 创建 app下的 models.py 文件, 记录模块信息
        dst_path = get_dir_path(self.target, app.name)
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'models.py.jinja2')
        dst_file = os.path.join(dst_path, 'models.py')
        self.render(tmpl, {'app': app}, dst_file)

        # 创建 app 下的 dao.py 文件, 记录映射信息
        dst_path = get_dir_path(self.target, app.name)
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'dao.py.jinja2')
        dst_file = os.path.join(dst_path, f'dao.py')
        self.render(tmpl, {'app': app}, dst_file)

        # 创建 app 下的 handlers.py 文件, 记录处理类信息
        dst_path = get_dir_path(self.target, app.name)
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'handlers.py.jinja2')
        dst_file = os.path.join(dst_path, f'handlers.py')
        self.render(tmpl, {'app': app}, dst_file)

    def make(self, app, klass):
        # 创建 app/utils 下的 utils.py 文件, 记录模块自定义操作信息
        dst_path = get_dir_path(self.target, app.name, 'utils')
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'utils.py.jinja2')
        dst_file = os.path.join(dst_path, f'{klass.name}.py')
        self.render_once(tmpl, {'klass': klass, 'app': app}, dst_file)
