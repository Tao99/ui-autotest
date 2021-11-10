#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os
import unittest
import glob
from Project.config import setting


def create_by():
    with open("../config/case_template", encoding='utf-8') as f:
        content = f.read()
    all_file = glob.glob(setting.TEST_CASE_YAML + os.sep + '*.yaml')
    for file in all_file:
        class_name = os.path.split(file)[-1].replace('.yaml', '').capitalize()
        print(class_name)
        py_content = content % (class_name, file)
        print(py_content)
        py_path = os.path.join(setting.TEST_CASE_PATH, class_name.lower() + '.py')
        print(py_path)
        open(py_path, 'w', encoding='utf-8').write(py_content)


def run_all_case():
    test_suite = unittest.TestSuite()
    all_py = unittest.defaultTestLoader.discover(setting.TEST_CASE_PATH, '*.py')
    [test_suite.addTests(case) for case in all_py]
    f = open("../../Project/report/report.html", 'wb')
#   runner = HTMLTestRunner.HTMLTestRunner(steam=f, )


if __name__ == '__main__':
    create_by()
