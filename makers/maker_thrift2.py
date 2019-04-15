# -*- coding: utf-8 -*-
# @File    : maker_thrift2.py
# @AUTH    : swxs
# @Time    : 2019/2/26 16:25

import os
from .maker import Maker
from .registry import factory


@factory.add_makers
class MakerThrift2(Maker):
    name = "thrift2"

    @classmethod
    def conv_type(cls, ttype):
        ttype_dict = {
            'str': 'string',
            'int': 'i32',
            'bool': 'bool',
            'strlist': 'list<string>',
            'intlist': 'list<inting>',
            'objectid': 'string'
        }
        return ttype_dict.get(ttype, 'string')

    def total_make(self, app_name, models, task):
        pass

    def make(self, app_name, model, task):
        tmpl = os.path.join('backend', 'rpc', self.config.backend.rpc, 'rpc.protocol')
        dst_file = os.path.join(self.config.target.backend, 'rpc', 'protocols', model.name + '.thrift')
        self.render(tmpl, {'model': model, 'conv_type': MakerThrift2.conv_type}, dst_file)

        tmpl = os.path.join('backend', 'rpc', self.config.backend.rpc, 'rpc_server.py')
        dst_file = os.path.join(self.config.target.backend, 'rpc', model.name + '_rpc_server.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)

        tmpl = os.path.join('backend', 'rpc', self.config.backend.rpc, 'rpc_client.py')
        dst_file = os.path.join(self.config.target.backend, 'rpc', model.name + '_rpc_client.py')
        self.render(tmpl, {'model': model, 'app_name': app_name}, dst_file)
