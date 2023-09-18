# -*- coding: utf-8 -*-
# @File    : maker_tornado.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:14

import os
from .maker import Maker
from ..utils.utils import get_dir_path


class MakerAppYaml(Maker):
    name = "app-yaml"

    def make(self, app, klass):
        dst_path = get_dir_path(self.target, app.name_lower)

        # 创建 app/models 下的 {app}.py 文件, 记录模块信息
        tmpl = os.path.join(self.output.get('framework'), 'apps', 'models', 'model.py.jinja2')
        dst_file = os.path.join(dst_path, 'models', f'{klass.name_lower}.py')
        self.render(tmpl, {'app': app, 'klass': klass}, dst_file)
