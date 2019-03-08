# -*- coding: utf-8 -*-
# @File    : maker.py
# @AUTH    : swxs
# @Time    : 2019/2/26 15:41

import os
import abc


class Maker(object, metaclass=abc.ABCMeta):
    def __init__(self, env, app_list, config, render):
        self.env = env
        self.config = config
        self.render = render
        self.app_list = app_list

        self.register_filters()

    def add_init(self, target_path):
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        dst_file = os.path.join(target_path, '__init__.py')
        if not os.path.exists(dst_file):
            open(dst_file, 'wb').close()

    @abc.abstractmethod
    def make(self, app, task):
        """
        具体的渲染机制实现
        :return:
        """

    def register_filters(self):
        from importlib import import_module
        from inspect import getmembers, isfunction
        module_name_list = [
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
