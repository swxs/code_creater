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

    def make(self, app, task):
        tmpl = os.path.join('backend', 'rpc', self.config.backend.rpc, 'rpc.protocol')
        dst_file = os.path.join(self.config.target.backend, 'rpc', 'protocols', app.name + '.thrift')
        self.render(tmpl, {'app': app, 'conv_type': MakerThrift2.conv_type}, dst_file)

        tmpl = os.path.join('backend', 'rpc', self.config.backend.rpc, 'rpc_server.py')
        dst_file = os.path.join(self.config.target.backend, 'rpc', app.name + '_rpc_server.py')
        self.render(tmpl, {'app': app}, dst_file)

        tmpl = os.path.join('backend', 'rpc', self.config.backend.rpc, 'rpc_client.py')
        dst_file = os.path.join(self.config.target.backend, 'rpc', app.name + '_rpc_client.py')
        self.render(tmpl, {'app': app}, dst_file)
