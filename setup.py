# -*- coding: utf-8 -*-
# @File    : setup.py.py
# @AUTH    : swxs
# @Time    : 2019/6/4 13:46

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="code creater",
    version="0.0.1",
    author="swxs",
    author_email="xiaorenju1@gmail.com",
    description="code creater",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swxs/code_creater",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
