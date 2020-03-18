# -*- coding: utf-8 -*-
# @File    : registry.py
# @AUTH    : swxs
# @Time    : 2019/2/26 15:45


class Factory(object):
    def __init__(self):
        self.maker_dict = dict()

    def make_code(self, env, root, params_dict, config):
        for task in config:
            maker = self.maker_dict[task.get('framework')](env, root, params_dict, config)
            for app in root.apps:
                maker.total_make(app, task)
                for klass in app.klasses:
                    try:
                        maker.make(app, klass, task)
                    except Exception as e:
                        print(e)

    def add_makers(self, maker):
        self.maker_dict[maker.name] = maker
        return maker


factory = Factory()
