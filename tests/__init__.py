# -*- coding: utf-8 -*-

import datetime
import os
import sys
from operator import ge
import unittest
import functools


class MyLoader(unittest.TestLoader):
    def getTestCaseNames(self, testCaseClass):
        """Return a sorted sequence of method names found within testCaseClass
        """

        def isTestMethod(attrname, testCaseClass=testCaseClass, prefix=self.testMethodPrefix):
            return attrname.startswith(prefix) and callable(getattr(testCaseClass, attrname))

        testFnNames = list(filter(isTestMethod, dir(testCaseClass)))

        def ln(f):
            return getattr(testCaseClass, f).__code__.co_firstlineno

        def ln_cmp(a, b):
            return (ln(a) > ln(b)) - (ln(a) < ln(b))

        if self.sortTestMethodsUsing:
            testFnNames.sort(key=functools.cmp_to_key(ln_cmp))
        return testFnNames


"""
√1. 如何自动设置test运行顺序，不同文件按文件名，相同文件按行号
    使用MyLoader重写了方法加载的顺序， 注意在迁移到py3时需要对应做修改

×2. 如何动态切换mongodb
    settings中的db_connect迁移到main.py中，test.__init__.py中调用mock连接， 在status中， 添加setUP和tearDown处理
    具体可参见 status_region_tests.py 文件

×3. 如何测试/apps/, 基于requests Cookie留存登录信息
    数据库相关有点问题无法统一， 暂时放弃对接口的测试

4. 如何生成一部分测试代码, (自动化创建, 批量)
    增， 检查相关属性正常 （基于field？）
    删， 检查各种条件不满足不可以删除（基于逻辑）， 以及成功的删除
    改， 检查相关属性正常 （基于field？）
    查， 检查各种条件可以获得正确的结果（基于逻辑）
    自定义属性， 如何当作一般属性处理
    自定义方法， 如何判定返回值正确？

√5. 如何组织参数等信息
    目前统一将参数放置在test_data.test_config中， 具体组织方式待定

暂定下文件名规范：
api_XXX_tests.py 测试API
utils_XXX_tests.py 测试模块方法， 基于mock
status_XXX_tests.py 测试当前数据库或文件是否符合规则
helper_XXX_tests.py 测试基础方法， 注意一种不能有关于任何数据的内容，对基于文件的方法将模拟格式文件放在test_data下
"""


def report_to_shell(suite):
    runner = unittest.TextTestRunner()

    # 执行测试
    runner.run(suite)


def report_to_html(suite):
    import HTMLTestRunner

    now = datetime.datetime.now()
    path = settings.get_dir_path(settings.SITE_ROOT, "tests", "reports")
    report_file = os.path.join(path, f"{now:%Y_%m_%d_%H_%M_%S}_report.html")

    # 执行测试
    with open(report_file, "wb") as report:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=f"{now}_report")
        runner.run(suite)


REPORT_TARGET_DICT = {
    "html": report_to_html,
    "shell": report_to_shell
}


def run_tests(target="shell"):
    # 定义测试集合
    suite = unittest.TestSuite()

    # 构建测试用例集
    loader = MyLoader()
    all_case = loader.discover('./', pattern='*_tests.py')
    for case in all_case:
        # 循环添加case到测试集合里面
        suite.addTests(case)

    try:
        REPORT_TARGET_DICT[target](suite)
    except Exception:
        print(f"{target} is failed!")
        REPORT_TARGET_DICT["shell"](suite)


# 设置测试结果处理方法


if __name__ == "__main__":
    run_tests(target="shell")
