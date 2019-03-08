# -*- coding: utf-8 -*-
# @File    : registry.py
# @AUTH    : swxs
# @Time    : 2019/2/26 15:45

import os
from collections import defaultdict


class Factory(object):
    def __init__(self):
        self.maker_dict = dict()

    def make_code(self, env, app_list, config, render):
        for app in app_list:
            for task in config.tasks:
                try:
                    self.maker_dict[task.get('framework')](env, app_list, config, render).make(app, task)
                except Exception as e:
                    print(e)

    def add_makers(self, maker):
        self.maker_dict[maker.name] = maker
        return maker


factory = Factory()
