import os
import yaml
import json
from jinja2 import Environment, PackageLoader, select_autoescape
from makers import maker_tornado, factory

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
    loader=PackageLoader('templates'),
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True,
    extensions=['jinja2.ext.loopcontrols']
)


def register_filters():
    from importlib import import_module
    from inspect import getmembers, isfunction
    module_name_list = [
        'filters.' + config.frontend,
    ]
    module_list = []
    filter_set = set()
    for name in module_name_list:
        try:
            imported_module = import_module(name)
            module_list.append((name, imported_module))
        except ModuleNotFoundError:
            continue
    for module_name, module in module_list:
        print(f'Filter module found: {module_name}')
        function_list = [o for o in getmembers(module) if isfunction(o[1])]
        for name, func in function_list:
            if name in filter_set:
                print(f'Warning! Filter [{name}] in {module_name} already defined! The latter will overwrite the formmer!')
            else:
                print(f'Filter loaded: {name}')
            jinja_env.filters[name] = func


def render(tmpl, adict, dst_file, overwrite=True):
    if not overwrite:
        if os.path.exists(dst_file):
            print('Skipped. Target file: %s exists!' % dst_file)
            return
    tmpl = tmpl.replace('\\', '/')
    template = jinja_env.get_template(tmpl)
    code = template.render(**adict)
    if not os.path.exists(os.path.dirname(dst_file)):
        os.makedirs(os.path.dirname(dst_file))
    open(dst_file, 'w', encoding='utf-8').write(code)


if __name__ == "__main__":
    config = dict2objectdict(yaml.load(open('config.yaml', encoding='utf8')))
    if os.path.exists('local_config.yaml'):
        local_config = dict2objectdict(yaml.load(open('local_config.yaml', encoding='utf8')))
        config.update(local_config)

    with open(os.path.join(script_path, "block", "container.json")) as info:
        app_list = [dict2objectdict(json.load(info))]
        factory.make_code(app_list, config, render)
