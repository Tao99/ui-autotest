#!/usr/bin/env python3.7
# _*_ coding:utf-8 _*_

from .runner import Runner
from .HTMLTestRunner import HTMLTestRunner
from .basepage import BasePage
from .loader import Loader
from .get_excel import read_excel, write_excel
from .operate import yamlPage
from .send_email import send_email
from .new_report import new_report


__all__ = ['BasePage', 'Loader', 'Runner', 'yamlPage', 'new_report', 'write_excel',
           'HTMLTestRunner', 'send_email', 'read_excel']

# Expose obsolete functions for backwards compatibility


__all__.extend(['find_test_method'])
