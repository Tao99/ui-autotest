#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 创建项目目录
import argparse
import os, sys
from logger import logger
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
        (os.path.join(project_path, "testcase", "suite"), "folder"),
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
        '-s', '--startproject',
        help="Specify new project name")

    args = parser.parse_args()

    if args.version:
        logger.error("{}".format("0.0.2"))
        exit(0)

    if args.startproject:
        project_path = os.path.join(os.getcwd(), args.startproject)
        create_scaffold(project_path)
        exit(0)
        return project_path

    else:
        logger.error("Please specify new project name first")
        exit(0)
