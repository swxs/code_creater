# -*- coding: utf-8 -*-
# @File    : run.py
# @AUTH    : swxs
# @Time    : 2019/2/27 10:59

import os
import time
import yaml
import click
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, as_completed
from jinja2 import Environment, PackageLoader, select_autoescape

from .parser import parseModel
from .makers import maker_productor
from .utils.timeit import timeit

script_path = os.path.dirname(os.path.abspath(__file__))

jinja_env = Environment(
    loader=PackageLoader('code_creater.static'),
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True,
    extensions=['jinja2.ext.loopcontrols'],
)


@click.command()
@click.argument('filename')
@timeit
def run(filename):
    """
    简介
    ----------
    获取文件指定的配置文件及其对应输出， 并生成模板

    参数
    ----------
    filename :配置文件名

    """
    config_filepath = os.path.join(script_path, "conf", filename)
    if not os.path.exists(config_filepath):
        exit("文件不存在")
    config = yaml.safe_load(open(config_filepath, encoding='utf8'))

    def run_task(root, task, output):
        maker = maker_productor[output.get('framework')](jinja_env, root, task, output)
        maker.run()
        return True

    core_number = multiprocessing.cpu_count()
    executor = ThreadPoolExecutor(max_workers=3)  # core_number * 2

    all_futures = {}
    for task in config.get('tasks', []):
        app_filepath = os.path.join(script_path, "apps", task.get('input', ""))
        if os.path.exists(config_filepath):
            root = parseModel(app_filepath, task)
            for output in task.get('output', []):
                future = executor.submit(run_task, root, task, output)
                all_futures[future] = False

    for future in as_completed(all_futures):
        print(future.result())

if __name__ == "__main__":
    run()
