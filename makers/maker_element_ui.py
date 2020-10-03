# -*- coding: utf-8 -*-
# @File    : maker_element_ui.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:14

import os
from .maker import Maker
from ..utils.utils import get_dir_path


class MakerElementUI(Maker):
    name = "element-ui"

    def total_make(self, app):
        pass

    def make(self, app, klass):
        # 创建基础文件
        dst_path = get_dir_path(self.target)

        filenames = [
            "vue.config.js.jinja2",
            "README.md.jinja2",
            "prettier.config.js.jinja2",
            "package.json.jinja2",
            "babel.config.js.jinja2",
            ".gitignore.jinja2",
            ".eslintrc.js.jinja2",
            ".eslintignore.jinja2",
            os.path.join("src", "router.js.jinja2"),
            os.path.join("src", "main.js.jinja2"),
            os.path.join("src", "App.vue.jinja2"),
            os.path.join("src", "views", "404.vue.jinja2"),
            os.path.join("src", "views", "index.vue.jinja2"),
            os.path.join("src", "utils", "auth.js.jinja2"),
            # os.path.join("src", "views", "home.vue.jinja2"),
            os.path.join("src", "plugins", "axios.js.jinja2"),
            os.path.join("src", "plugins", "element.js.jinja2"),
            os.path.join("src", "assets", "js", "bus.js.jinja2"),
            os.path.join("src", "assets", "style", "base.less.jinja2"),
            os.path.join("src", "assets", "style", "common.less.jinja2"),
            # os.path.join("src", "assets", "fonts", "Cemicons.eot.jinja2"),
            # os.path.join("src", "assets", "fonts", "Cemicons.svg.jinja2"),
            # os.path.join("src", "assets", "fonts", "Cemicons.ttf.jinja2"),
            # os.path.join("src", "assets", "fonts", "Cemicons.woff.jinja2"),
        ]
        for filename in filenames:
            tmpl = os.path.join(self.output.get('framework'), filename)
            dst_file = os.path.join(dst_path, filename[:-7])
            self.render_once(tmpl, {'klass': klass, 'app': app}, dst_file)

        #
        dst_path = get_dir_path(self.target, 'src', 'views')
        tmpl = os.path.join(self.output.get('framework'), 'src', 'views', 'home.vue.jinja2')
        dst_file = os.path.join(dst_path, f'home.vue')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)

        # 创建 对应模块的 api.js 文件, 实现模块访问方法
        dst_path = get_dir_path(self.target, 'src', 'api')
        tmpl = os.path.join(self.output.get('framework'), 'src', 'api', 'api.js.jinja2')
        dst_file = os.path.join(dst_path, f'{klass.name}.js')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)

        # 创建 对应模块的 enum.js 文件, 记录模块字段映射常量
        dst_path = get_dir_path(self.target, 'src', 'enum')
        tmpl = os.path.join(self.output.get('framework'), 'src', 'enum', 'enum.js.jinja2')
        dst_file = os.path.join(dst_path, f'{klass.name}.js')
        self.render(tmpl, {'klass': klass, 'app': app}, dst_file)
