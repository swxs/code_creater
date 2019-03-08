# -*- coding: utf-8 -*-
# @File    : run.py
# @AUTH    : swxs
# @Time    : 2019/2/27 10:59

import os
import yaml
import json
import datetime
from jinja2 import Environment, PackageLoader, select_autoescape
from makers import maker_markfile, maker_tornado, factory

from tornado.util import ObjectDict


def dict2objectdict(adict):
    for key, value in adict.items():
        if isinstance(value, dict):
            new_value = dict2objectdict(value)
            adict[key] = new_value
    obj = ObjectDict(adict)
    return obj


script_path = os.path.dirname(os.path.abspath(__file__))

jinja_env = Environment(
    loader=PackageLoader('static'),
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True,
    extensions=['jinja2.ext.loopcontrols']
)


def render(tmpl, adict, dst_file, overwrite=True):
    if not overwrite:
        if os.path.exists(dst_file):
            print('Skipped. Target file: %s exists!' % dst_file)
            return
    tmpl = tmpl.replace('\\', '/')
    template = jinja_env.get_template(tmpl)

    # 添加部分常用方法
    adict.update(dict(
        current_time=f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"
    ))

    code = template.render(**adict)
    if not os.path.exists(os.path.dirname(dst_file)):
        os.makedirs(os.path.dirname(dst_file))
    open(dst_file, 'w', encoding='utf-8').write(code)


if __name__ == "__main__":
    config = dict2objectdict(yaml.load(open('config.yaml', encoding='utf8')))
    if os.path.exists('local_config.yaml'):
        local_config = dict2objectdict(yaml.load(open('local_config.yaml', encoding='utf8')))
        config.update(local_config)

    ALL_MODEL = None

    for root, path, files in os.walk(os.path.join(os.getcwd(), "block")):
        for file in files:
            if not (ALL_MODEL is not None and file not in ALL_MODEL):
                with open(os.path.join(root, file)) as info:
                    app = dict2objectdict(json.load(info))
                    app_list = []
                    factory.make_code(jinja_env, app_list, config, render)
