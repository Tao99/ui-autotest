#!/usr/bin/env python3.7
# _*_ coding:utf-8 _*_
import os
import sys
sys.path.append(os.path.dirname(__file__))

# 测试项目的绝对路径
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)) + "/Project")
sys.path.append(BASE_DIR)


# yaml测试用例集合
TEST_CASE_YAML_SUIT = os.path.join(BASE_DIR, "testcase/suit", "login-suit.yml")
# yaml测试用例
TEST_CASE_YAML_CASE = os.path.join(BASE_DIR, "testcase/case", "login-case.yml")
# 邮件配置文件
CONFIG_DIR = os.path.join(BASE_DIR, "config", "email.ini")
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR, "report")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR, "logs")
# py测试用例目录
TEST_CASE_PY = os.path.join(BASE_DIR, "test_py")
