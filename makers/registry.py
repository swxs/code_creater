# -*- coding: utf-8 -*-
# @File    : registry.py
# @AUTH    : swxs
# @Time    : 2019/2/26 15:45

import os
from collections import defaultdict


class Factory(object):
    def __init__(self):
        self.maker_dict = dict()

    def make_code(self, env, apps_dict, config, render):
        for task in config:
            maker = self.maker_dict[task.get('framework')](env, apps_dict, config, render)
            for (app_name, models) in apps_dict.items():
                for model_name, model in models.items():
                    try:
                        maker.make(app_name, model, task)
                    except Exception as e:
                        print(e)

    def add_makers(self, maker):
        self.maker_dict[maker.name] = maker
        return maker


factory = Factory()
