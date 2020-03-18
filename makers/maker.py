# -*- coding: utf-8 -*-
# @File    : maker.py
# @AUTH    : swxs
# @Time    : 2019/2/26 15:41

import os
import abc
import datetime

class Maker(object, metaclass=abc.ABCMeta):
    name = 'base'

    def __init__(self, env, root, params_dict, config):
        self.env = env
        self.config = config
        self.root = root
        self.params_dict = params_dict
        for conf in self.config:
            target_path = conf.get('target')
            if not os.path.exists(target_path):
                os.makedirs(target_path)
        self.register_filters()

    def base_render(self, tmpl, adict, dst_file, overwrite=True):
        if not overwrite:
            if os.path.exists(dst_file):
                print('Skipped. Target file: %s exists!' % dst_file)
                return

        # 添加部分常用方法
        adict.update(dict(
            current_time=f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"
        ))
        adict.update(**self.params_dict)
        tmpl = tmpl.replace('\\', '/')
        code = self.env.get_template(tmpl).render(**adict)
        if not os.path.exists(os.path.dirname(dst_file)):
            os.makedirs(os.path.dirname(dst_file))
        open(dst_file, 'w', encoding='utf-8').write(code)

    def register_filters(self):
        from importlib import import_module
        from inspect import getmembers, isfunction
        module_name_list = [
            f'filters',
            f'filters.{self.name}'
        ]
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
                    print(f'Warning! Filter [{name}] in {module_name} already defined! The latter will overwrite the formmer!')
                else:
                    print(f'Filter loaded: {name}')
                self.env.filters[name] = func

    def render(self, tmpl, adict, dst_file):
        adict.update(dict(
            root=self.root,
        ))
        return self.base_render(tmpl, adict, dst_file)

    def render_once(self, tmpl, adict, dst_file):
        if os.path.exists(dst_file):
            return
        adict.update(dict(
            root=self.root,
        ))
        return self.base_render(tmpl, adict, dst_file)

    @abc.abstractmethod
    def make(self, app, task):
        """
        具体的渲染机制实现
        :return:
        """

    @abc.abstractmethod
    def total_make(self, app, klass, task):
        """
        具体的渲染机制实现
        :return:
        """
