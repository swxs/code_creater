# -*- coding: utf-8 -*-
# @File    : run.py
# @AUTH    : swxs
# @Time    : 2019/2/27 10:59

import os
import yaml
import fire
import datetime
from tornado.util import ObjectDict
from jinja2 import Environment, PackageLoader, select_autoescape
from core import parseModel
from makers import factory


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


def run(filename):
    """
    获取文件指定的配置文件及其对应输出， 并生成模板
    :param filename:
    :return:
    """
    config_filepath = os.path.join(script_path, "conf", filename)
    if not os.path.exists(config_filepath):
        exit("文件不存在")
    config = yaml.load(open(config_filepath, encoding='utf8'))

    for task in config.get('tasks', []):
        app_filepath = os.path.join(script_path, "apps", task.get('input', ""))
        if not os.path.exists(config_filepath):
            continue
        apps_dict = dict2objectdict(parseModel(app_filepath))
        factory.make_code(jinja_env, apps_dict, task.get('output', []), render)


if __name__ == "__main__":
    fire.Fire(run)
