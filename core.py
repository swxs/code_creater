# -*- coding: utf-8 -*-
# @File    : core.py
# @AUTH    : swxs
# @Time    : 2019/3/25 14:13

import re
from pprint import pprint
from xmindparser import xmind_to_dict
from .filters import title, lower, upper
from .utils.Helper_validate import RegType, Validate

TASK = None


class Node(object):
    def __init__(self, topic):
        self.topic = topic

        title_parts = [part.strip() for part in topic.get("title").replace("：", ":").split(":")]
        self.name = title_parts[0]
        self.sub = title_parts[1:]

        self.children = []
        for topic in topic.get("topics", []):
            self.children.append(Node(topic))


class Root(object):
    def __init__(self, node):
        self.apps = []
        self.meta = None
        self.descriptions = []

        for child in node.children:
            if Validate.start_with(child.name, RegType.DESC):
                self.descriptions.append(Desc(child))
            elif Validate.has(child.name, RegType.APP):
                self.apps.append(App(child))

    def __repr__(self):
        return f"""{self.apps}"""


class App(object):
    def __init__(self, node):
        self.name = title(node.sub[0])
        self.klasses = []
        self.meta = Meta(None)
        self.descriptions = []

        for child in node.children:
            if Validate.start_with(child.name, RegType.DESC):
                self.descriptions.append(Desc(child))
            elif Validate.check(child.name, RegType.META):
                self.meta = Meta(child)
            else:
                self.klasses.append(Klass(child))

    def __repr__(self):
        return f"""
            {self.name}模块:
                其描述为：{self.descriptions}
                其属性为：{self.meta}
                包含下列类:
                    {self.klasses}"""


class Desc(object):
    def __init__(self, node):
        self.name = ":".join([node.name.lstrip("#").strip(), *node.sub])
        self.group = []

        for child in node.children:
            self.group.append(Desc(child))

    def __repr__(self):
        return f"{self.name}"


class Meta(object):
    def __init__(self, node=None):
        """[summary]

        Args:
            node ([type], optional): [description]. Defaults to None.
        """
        self.values = {}
        self.descriptions = []

        if node:
            for child in node.children:
                if Validate.start_with(child.name, RegType.DESC):
                    self.descriptions.append(Desc(child))
                elif Validate.check(child.name, RegType.ALLOW_INHERITANCE):
                    self.values["allow_inheritance"] = True
                elif Validate.check(child.name, RegType.PARENT):
                    self.values["parent"] = child.children[0].name
                elif Validate.check(child.name, RegType.IMPORT):
                    self.values["import_list"] = []
                    for import_child in child.children:
                        _import = dict(
                            name=import_child.name,
                        )
                        self.values["import_list"].append(_import)
                elif Validate.check(child.name, RegType.TOKEN):
                    self.values["tokens"] = []
                    for token_children in child.children:
                        token = {"field": token_children.name, "name": token_children.children[0].name, "func": []}
                        _current_token = token_children.children[0]
                        while _current_token.children:
                            token["func"].append(_current_token.children[0].name)
                            _current_token = _current_token.children[0]
                        self.values["tokens"].append(token)
                elif Validate.check(child.name, RegType.INDEX):
                    self.values["index_list"] = []
                    for index_child in child.children:
                        index = dict(
                            field_name_list=[index_child.name, *index_child.sub],
                            uniq=False,
                        )
                        for params in index_child.children:
                            if Validate.check(params.name, f"uniq"):
                                index["uniq"] = True
                        self.values["index_list"].append(index)
                else:
                    self.values[child.name] = Meta(child).values

    def __repr__(self):
        return f"{self.values}"


class Klass(object):
    def __init__(self, node):
        self.name = title(node.name)
        self.fields = []
        self.meta = Meta(None)
        self.descriptions = []

        for child in node.children:
            if Validate.start_with(child.name, RegType.DESC):
                self.descriptions.append(Desc(child))
            elif Validate.check(child.name, RegType.META):
                self.meta = Meta(child)
            else:
                self.fields.append(Field(child))

    def __repr__(self):
        return f"""
                        {self.name}
                            其描述为：{self.descriptions}
                            其属性为：{self.meta}
                            包含下列字段：
                                {self.fields}"""


class Field(object):
    CONVERTS = {
        "str": ("str", "str"),
        "string": ("str", "str"),
        "int": ("int", "int"),
        "float": ("float", "float"),
        "bool": ("boolean", "boolean"),
        "boolean": ("boolean", "boolean"),
        "id": ("objectid", "objectid"),
        "objectid": ("objectid", "objectid"),
        "object_id": ("objectid", "objectid"),
        "datetime": ("datetime", "datetime"),
        "dict": ("dict", "dict"),
        "list": ("list", None),
        "strlist": ("list", "str"),
        "intlist": ("list", "int"),
        "idlist": ("list", "objectid"),
        "objectidlist": ("list", "objectid"),
        "dictlist": ("list", "dict"),
    }

    def __init__(self, node):
        """
        简介
        ----------


        参数
        ----------
        node :
            节点
        """
        self.name = lower(node.name)
        if node.sub:
            self.ttype = lower(node.sub[0])
        else:
            self.ttype = "str"
        self.field_type = self.CONVERTS[self.ttype][0]
        self.field_detail_type = self.CONVERTS[self.ttype][1]
        self.values = {}
        self.descriptions = []

        for child in node.children:
            if Validate.start_with(child.name, RegType.DESC):
                self.descriptions.append(Desc(child))
            elif Validate.start_with(child.name, RegType.DEFAULT):
                self.values["default"] = child.sub[0]
            elif Validate.start_with(child.name, RegType.REF):
                self.values["ref"] = child.sub[0]
            elif Validate.start_with(child.name, RegType.NOCREATE):
                self.values["no_create"] = True
            elif Validate.start_with(child.name, RegType.ENUM):
                enum_list = []
                for enum_child in child.children:
                    if Validate.start_with(enum_child.name, RegType.START_KEY) and Validate.end_with(
                        enum_child.name, RegType.END_KEY
                    ):
                        for enum_child in TASK['key'][enum_child.name[2:-2]]:
                            enum_list.append(
                                {
                                    "key": enum_child['key'],
                                    "value": enum_child['value'],
                                }
                            )
                    else:
                        enum_list.append(
                            {
                                "key": enum_child.sub[0],
                                "value": enum_child.name,
                            }
                        )
                self.values["enums"] = enum_list
            elif Validate.start_with(child.name, f"from_jwt"):
                field_node = child.children[0]
                changes = list()

                current_node = field_node
                while current_node.children:
                    changes.append(current_node.children[0].name)
                    current_node = current_node.children[0]

                self.values["from_jwt"] = {"name": field_node.name, "changes": changes}
            else:
                self.values[child.name] = Meta(child).values

    def __repr__(self):
        return f"""
                                {self.name}:
                                    其描述为：{self.descriptions}
                                    其属性为: {self.values}"""


def parseModel(filename, task=None):
    xminddict = xmind_to_dict(filename)

    global TASK
    TASK = task
    xmindtopic = Node(xminddict[0]["topic"])
    root = Root(xmindtopic)
    pprint(root)
    return root
