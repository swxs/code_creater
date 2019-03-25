# -*- coding: utf-8 -*-
# @File    : maker.py
# @AUTH    : swxs
# @Time    : 2019/2/26 15:41

import os
import abc


class Maker(object, metaclass=abc.ABCMeta):
    def __init__(self, env, apps_dict, config, render):
        self.env = env
        self.config = config
        self.base_render = render
        self.apps_dict = apps_dict
        for conf in self.config:
            target_path = conf.get('target')
            if not os.path.exists(target_path):
                os.makedirs(target_path)
        self.register_filters()

    def render(self, tmpl, adict, dst_file):
        adict.update(dict(
            apps_dict=self.apps_dict,
        ))
        return self.base_render(tmpl, adict, dst_file)

    @abc.abstractmethod
    def make(self, name, app, task):
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
