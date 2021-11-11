#!/usr/bin/env python3.7
# _*_ coding:utf-8 _*_
import time
import unittest
from HTest import setting
from HTest.send_email import send_email
from HTest.new_report import new_report
import HTest


# 加载yaml格式的测试用例
def add_case_yaml():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(HTest.yamlPage))
    return suite


def run_case(case):
    now = time.strftime("%Y%m%d%H%M%S")
    filename = setting.TEST_REPORT + '/' + now + 'yaml.html'
    fp = open(filename, 'w', encoding='utf-8')
    runner = HTest.HTMLTestRunner(stream=fp, title='自动化测试报告',
                                  description='运行环境：Linux deepin 20.2.2， 浏览器：Chrome', verbosity=2)
    runner.run(case)
    fp.close()
    report = new_report(setting.TEST_REPORT)  # 调用模块生成最新的报告
    send_email(report)  # 调用发送邮件模块


def test_yaml():
    case = add_case_yaml()
    run_case(case)
