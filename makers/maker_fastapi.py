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
        dst_path = get_dir_path(self.target, app.name_lower)

        # 创建 app 下的 __init__.py 文件, 只创建一次
        tmpl = os.path.join(self.output.get('framework'), 'apps', '__init__.py.jinja2')
        dst_file = os.path.join(dst_path, f'__init__.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        # 创建 app/models 下的 __init__.py 文件, 只创建一次
        tmpl = os.path.join(self.output.get('framework'), 'apps', '__init__.py.jinja2')
        dst_file = os.path.join(dst_path, 'models', f'__init__.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        # 创建 app/dao 下的 __init__.py 文件, 只创建一次
        tmpl = os.path.join(self.output.get('framework'), 'apps', '__init__.py.jinja2')
        dst_file = os.path.join(dst_path, 'dao', f'__init__.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        # 创建 app/schemas 下的 __init__.py 文件, 只创建一次
        tmpl = os.path.join(self.output.get('framework'), 'apps', '__init__.py.jinja2')
        dst_file = os.path.join(dst_path, 'schemas', f'__init__.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        # 创建 app/handlers 下的 __init__.py 文件, 只创建一次
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'api', '__init__.py.jinja2')
        dst_file = os.path.join(dst_path, 'api', f'__init__.py')
        self.render_once(tmpl, {'app': app}, dst_file)

        # 创建 app 下的 consts.py 文件, 记录映射信息
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'consts.py.jinja2')
        dst_file = os.path.join(dst_path, 'consts.py')
        self.render(tmpl, {'app': app}, dst_file)


    def make(self, app, klass):
        dst_path = get_dir_path(self.target, app.name_lower)

        # 创建 app/models 下的 {app}.py 文件, 记录模块信息
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'models', 'model.py.jinja2')
        dst_file = os.path.join(dst_path, 'models', f'{klass.name_lower}.py')
        self.render(tmpl, {'app': app, 'klass': klass}, dst_file)

        # 创建 app/dao 下的 {app}.py 文件, 记录映射信息
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'dao', 'dao.py.jinja2')
        dst_file = os.path.join(dst_path, 'dao', f'{klass.name_lower}.py')
        self.render(tmpl, {'app': app, 'klass': klass}, dst_file)

        # 创建 app/utils 下的 {app}.py 文件, 记录模块自定义操作信息, 只创建一次
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'utils', 'util.py.jinja2')
        dst_file = os.path.join(dst_path, f'{klass.name_lower}_utils.py')
        self.render_once(tmpl, {'app': app, 'klass': klass}, dst_file)

        # 创建 app/schemas 下的 {app}.py 文件, 记录模块自定义操作信息
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'schemas', 'schema.py.jinja2')
        dst_file = os.path.join(dst_path, 'schemas', f'{klass.name_lower}.py')
        self.render(tmpl, {'app': app, 'klass': klass}, dst_file)

        # 创建 app/api 下的 {app}.py 文件, 记录处理类信息
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'api', 'api.py.jinja2')
        dst_file = os.path.join(dst_path, 'api', f'{klass.name_lower}.py')
        self.render(tmpl, {'app': app, 'klass': klass}, dst_file)
