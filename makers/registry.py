# -*- coding: utf-8 -*-
# @File    : registry.py
# @AUTH    : swxs
# @Time    : 2019/2/26 15:45


class Factory(object):
    def __init__(self):
        self.maker_dict = dict()

    def make_code(self, env, apps_dict, params_dict, config):
        for task in config:
            maker = self.maker_dict[task.get('framework')](env, apps_dict, params_dict, config)
            for (app_name, models) in apps_dict.items():
                if app_name == "_description":
                    continue
                maker.total_make(app_name, models, task)
                for (model_name, model) in models.items():
                    if model_name == "_description":
                        continue
                    try:
                        maker.make(app_name, model, task)
                    except Exception as e:
                        print(e)

    def add_makers(self, maker):
        self.maker_dict[maker.name] = maker
        return maker


factory = Factory()
