#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 创建项目目录
import argparse
import os, sys
from HTest.logger import logger
sys.path.append(os.path.dirname(__file__))


def create_scaffold(project_path):
    if os.path.isdir(project_path):
        folder_name = os.path.basename(project_path)
        logger.error(u"Folder {} exists, please specify a new folder name.".format(folder_name))
        return
    logger.info("Start to create new project: {}\n".format(project_path))

    def create_path(path, ptype):
        if ptype == "folder":
            os.makedirs(path)
        elif ptype == "file":
            open(path, 'w').close()
        return "created {}: {}\n".format(ptype, path)

    path_list = [
        (project_path, "folder"),
        (os.path.join(project_path, "testcase"), "folder"),
        (os.path.join(project_path, "testcase", "step"), "folder"),
        (os.path.join(project_path, "testcase", "case"), "folder"),
        (os.path.join(project_path, "testcase", "suit"), "folder"),
        (os.path.join(project_path, "config"), "folder"),
        (os.path.join(project_path, "report"), "folder"),
        (os.path.join(project_path, "logs"), "folder"),
        (os.path.join(project_path, "plugin"), "folder")
    ]

    msg = ""
    for p in path_list:
        msg += create_path(p[0], p[1])

    logger.debug(msg)


def main_HTest():
    """
    UI test: parse command line options and run commands.
    """
    parser = argparse.ArgumentParser(
        description='Automated testing framework based on unittest by Tao.')
    parser.add_argument(
        '-v', '--version', dest='version', action='store_true',
        help="show version")
    parser.add_argument(
        '-s', '--project',
        help="Specify new project name.")
    parser.add_argument(
        '-r', '--testcase',
        help="Run the test case.")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        exit(0)

    else:
        if args.version:
            logger.error("{}".format("0.1.0"))
            exit(0)

        elif args.project:
            project_path = os.path.join(os.getcwd(), args.project)
            create_scaffold(project_path)
            exit(0)

        elif args.testcase and sys.argv[1] == "-r":
            file_suffix = os.path.splitext(sys.argv[2])[1].lower()  # 获取文件后缀名
            file = os.path.join(os.getcwd(), args.testcase)  # 获取执行文件
            print(file)
            if file_suffix in ['.yaml', '.yml']:
                from testcase import get_data
                get_data(file)
                from run_yaml import test_yaml
                test_yaml()
            elif file_suffix == '.py':
                from unittest.main import main
                main(module=None)
            else:
                print("ModuleFoundError: Not supported %s" % file)
            exit(0)

        else:
            logger.error("Please enter correct parameters")
            exit(0)
