# -*- coding: utf-8 -*-
# @File    : core.py
# @AUTH    : swxs
# @Time    : 2019/3/25 14:13

import re
from xmindparser import xmind_to_dict
from filters import get_title
from utils.Helper_validate import RegType, Validate


def parseModel(filename):
    apps = dict()
    tmp_apps = dict()

    adict = xmind_to_dict(filename)
    root = adict[0]["topic"]
    print(f"正在生成{root.get('title')}相关内容")
    for topic in root.get("topics", []):
        title = topic.get("title").strip()
        if Validate.has(title, RegType.APP):
            if Validate.start_with(title, RegType.COMMIT):
                continue

            parts = title.replace("：", ":").split(":")
            app_name = get_title(parts[1].strip())
            tmp_apps[app_name] = topic

    for app_name, app_node in tmp_apps.items():
        apps_dict = dict()
        for topic in app_node.get("topics", []):
            name = get_title(topic.get("title").strip())
            app = dict(name=name, field_list=[], parent=None)
            for field_topic in topic.get("topics", []):
                field_name = field_topic.get("title").strip()
                if Validate.check(field_name, RegType.META):
                    meta = parseMeta(app, field_topic)
                    if meta:
                        app["meta"] = meta
                else:
                    field = parseField(app, field_topic)
                    if field:
                        app["field_list"].append(field)
            apps_dict[name] = app
        print(apps_dict)
        apps[app_name] = apps_dict
    return apps


def parseField(app, topic):
    parts = topic.get("title").strip().replace("：", ":").split(":")
    if len(parts) == 0:
        return None
    elif len(parts) == 1:
        parts.append("str")
    else:
        pass

    if Validate.start_with(parts[0], RegType.COMMIT):
        return None

    field_name = parts[0].strip()
    ttype = parts[1].strip().lower()

    field_type = "str"
    field_detail_type = None

    if ttype in ("int",):
        field_type = "int"
    elif ttype in ("float", "Float"):
        field_type = "float"
    elif ttype in ("bool", "boolean"):
        field_type = "boolean"
    elif ttype in ("id", "objectid", "object_id"):
        field_type = "objectid"
    elif ttype in ("strlist",):
        field_type = "list"
        field_detail_type = "str"
    elif ttype in ("intlist",):
        field_type = "list"
        field_detail_type = "int"
    elif ttype in ("objectidlist", "idlist"):
        field_type = "list"
        field_detail_type = "objectid"
    elif ttype in ("dictlist",):
        field_type = "list"
        field_detail_type = "dict"
    elif ttype in ("list",):
        field_type = "list"
    elif ttype in ("str", "string"):
        field_type = "str"
    elif ttype in ("datetime",):
        field_type = "datetime"
    elif ttype in ("dict",):
        field_type = "dict"
    else:
        print("unknown field type: %s" % ttype)

    field_dict = dict(field_name=field_name, field_type=field_type, struct=field_detail_type)
    for info in topic.get("topics", []):
        title = info.get("title").strip()
        if Validate.start_with(title, RegType.COMMIT):
            help_text_parts = title.split("#")
            field_dict["help_text"] = help_text_parts[1].strip()
        elif Validate.start_with(title, RegType.DEFAULT):
            default_parts = title.replace("：", ":").split(":")
            if len(default_parts) > 1:
                field_dict["default"] = default_parts[1].strip()
            else:
                pass
        elif Validate.start_with(title, RegType.ENUM):
            enum_list = list()
            for enum in info.get("topics", []):
                enum_dict = dict()
                enum_parts = enum.get("title").strip().replace("：", ":").split(":")
                if len(enum_parts) < 2:
                    pass
                else:
                    enum_dict["value"] = enum_parts[0].strip()
                    enum_dict["name"] = enum_parts[1].strip()
                enum_list.append(enum_dict)
            field_dict["enums"] = enum_list
        else:
            print(field_name, title)
    return field_dict


def parseMeta(app, topic):
    meta_dict = dict(
        allow_inheritance=False,
        index_list=[],
    )
    for info in topic.get("topics", []):
        title = info.get("title").strip()
        if Validate.check(title, RegType.ALLOW_INHERITANCE):
            meta_dict["allow_inheritance"] = True
        elif Validate.check(title, RegType.PARENT):
            parent_info = info.get("topics", [])
            if len(parent_info) > 0:
                parent_name = parent_info[0].get("title").strip()
                app["parent"] = parent_name
        elif Validate.start_with(title, RegType.INDEX):
            index_list = info.get("topics", [])
            for index in index_list:
                deep_index = index.get("topics", [])
                is_uniq = False
                if len(deep_index) > 0:
                    deep_index_info = deep_index[0].get("title").strip()
                    if Validate.start_with(deep_index_info, RegType.UNIQ):
                        is_uniq = True
                index_info = dict(
                    field_name_list=index.get("title").strip().replace("，", ",").split(","),
                    is_uniq=is_uniq
                )
                meta_dict["index_list"].append(index_info)
        else:
            print(title)
    return meta_dict
