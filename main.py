# -*- coding: utf-8 -*-
# @File    : run.py
# @AUTH    : swxs
# @Time    : 2019/2/27 10:59

import os
import yaml
import fire
from core import parseModel
from makers import factory
from utils import utils
from jinja2 import Environment, PackageLoader, select_autoescape

script_path = os.path.dirname(os.path.abspath(__file__))

jinja_env = Environment(
    loader=PackageLoader('static'),
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True,
    extensions=['jinja2.ext.loopcontrols']
)


def run(filename):
    """
    获取文件指定的配置文件及其对应输出， 并生成模板
    :param filename:
    :return:
    """
    config_filepath = os.path.join(script_path, "conf", filename)
    if not os.path.exists(config_filepath):
        exit("文件不存在")
    config = yaml.safe_load(open(config_filepath, encoding='utf8'))

    for task in config.get('tasks', []):
        app_filepath = os.path.join(script_path, "apps", task.get('input', ""))
        if not os.path.exists(config_filepath):
            continue
            
        root = parseModel(app_filepath, task)
        params_dict = utils.dict2objectdict(task.get('params', {}))
        factory.make_code(jinja_env, root, params_dict, task.get('output', []))


if __name__ == "__main__":
    fire.Fire(run)
