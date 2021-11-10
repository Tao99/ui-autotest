#!/usr/bin/env python3.7
# _*_ coding:utf-8 _*_

from .runner import Runner
from .HTMLTestRunner import HTMLTestRunner
from .basepage import BasePage
from .loader import Loader
from .logger import Logger
from .read_excel import ReadExcel
from .operate import yamlPage
from .send_email import send_email
from .new_report import new_report


__all__ = ['BasePage', 'Loader', 'Runner', 'yamlPage', 'new_report',
           'HTMLTestRunner', 'send_email', 'Logger', 'ReadExcel']

# Expose obsolete functions for backwards compatibility


__all__.extend(['find_test_method'])
