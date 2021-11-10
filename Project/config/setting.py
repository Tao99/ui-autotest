#!/usr/bin/env python3.7
# _*_ coding:utf-8 _*_
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


# 邮件配置文件
CONFIG_DIR = os.path.join(BASE_DIR, "config", "email.ini")
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR, "report")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR, "logs")
# 测试数据目录
TEST_CASE_PY = os.path.join(BASE_DIR, "testcase")
# 测试用例目录
TEST_CASE_PATH = os.path.join(BASE_DIR, "teststeps")
# 测试用例主文件
TEST_CASE_YAML = os.path.join(BASE_DIR, "teststeps", "main.yaml")
# 测试url
URL = 'https://qiye.aliyun.com/'


