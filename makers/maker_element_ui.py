# -*- coding: utf-8 -*-
# @File    : maker_element_ui.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:14

import os
from .maker import Maker
from .registry import factory
from utils.utils import get_dir_path


@factory.add_makers
class MakerElementUI(Maker):
    name = "element-ui"

    def total_make(self, app_name, models, task):
        pass

    def make(self, app_name, model, task):
        # 创建 app/consts 下的 consts.py 文件, 记录映射信息
        dst_path = get_dir_path(task.get('target'), 'api')
        tmpl = os.path.join(task.get('framework'), 'api.js.jinja2')
        dst_file = os.path.join(dst_path, f'{model.name}.js')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        # 创建 app/models 下的 models.py 文件, 记录模块信息
        dst_path = get_dir_path(task.get('target'), 'enum')
        tmpl = os.path.join(task.get('framework'), 'enum.js.jinja2')
        dst_file = os.path.join(dst_path, f'{model.name}.js')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)
