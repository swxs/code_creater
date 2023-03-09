# -*- coding: utf-8 -*-
# @File    : maker.py
# @AUTH    : swxs
# @Time    : 2019/2/26 15:41

import os
import abc
import black
import datetime
from ..utils.utils import dict2objectdict

import logging

logger = logging.getLogger("main")


class Maker(object, metaclass=abc.ABCMeta):
    def __init__(self, env, root, task, output):
        self.env = env
        self.root = root
        self.task = task
        self.output = output
        self.params_dict = dict2objectdict(self.task.get('params', {}))
        self.target = os.path.join(self.output.get('target'))
        if not os.path.exists(self.target):
            os.makedirs(self.target)
        self.register_filters()

    def register_filters(self):
        from importlib import import_module
        from inspect import getmembers, isfunction

        module_name_list = [f'code_creater.filters', f'code_creater.filters.{self.name}']
        module_list = []
        filter_set = set()
        for name in module_name_list:
            try:
                imported_module = import_module(name)
                module_list.append((name, imported_module))
            except ModuleNotFoundError:
                continue
        for module_name, module in module_list:
            print(f'Filter module found: {module_name}')
            function_list = [o for o in getmembers(module) if isfunction(o[1])]
            for name, func in function_list:
                if name in filter_set:
                    print(
                        f'Warning! Filter [{name}] in {module_name} already defined! The latter will overwrite the formmer!'
                    )
                else:
                    print(f'Filter loaded: {name}')
                self.env.filters[name] = func

    def run(self):
        for app in self.root.apps:
            self.total_make(app)
            for klass in app.klasses:
                try:
                    self.make(app, klass)
                except Exception as e:
                    print(e)

    def base_render(self, tmpl, adict, dst_file, overwrite=True):
        if not overwrite:
            if os.path.exists(dst_file):
                print('Skipped. Target file: %s exists!' % dst_file)
                return

        # 添加部分常用方法
        try:
            adict.update(dict(current_time=f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"))
            adict.update(**self.params_dict)
            tmpl = tmpl.replace('\\', '/')
            code = self.env.get_template(tmpl).render(**adict)
            if not os.path.exists(os.path.dirname(dst_file)):
                os.makedirs(os.path.dirname(dst_file))
            # 这边通过判断文件类型，决定应用哪个formatter到代码上
            _, ext = os.path.splitext(dst_file)
            if ext == ".py":
                code = black.format_str(
                    code, mode=black.Mode(line_length=120, string_normalization=False, is_pyi=False)
                )
            open(dst_file, 'w', encoding='utf-8').write(code)
        except Exception as e:
            logger.exception(f"创建异常!")

    def render(self, tmpl, adict, dst_file):
        adict.update(
            dict(
                root=self.root,
            )
        )
        return self.base_render(tmpl, adict, dst_file)

    def render_once(self, tmpl, adict, dst_file):
        if os.path.exists(dst_file):
            return
        adict.update(
            dict(
                root=self.root,
            )
        )
        return self.base_render(tmpl, adict, dst_file)

    def make(self, app, klass):
        """
        具体的渲染机制实现
        :return:
        """
        raise NotImplementedError()

    def total_make(self, app):
        """
        具体的渲染机制实现
        :return:
        """
        raise NotImplementedError()
