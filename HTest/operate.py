#!/usr/bin/env python3.7
# _*_ coding:utf-8 _*_
import os
import time
import unittest
from selenium.webdriver.common.by import By
from HTest.get_yaml import Getyaml
from ddt import ddt, data, unpack
from selenium import webdriver
from HTest import setting, BasePage
from .logger import logger


url = setting.URL
path_case = os.path.join(setting.TEST_CASE_YAML_CASE)
path_suit = os.path.join(setting.TEST_CASE_YAML_SUIT)
data_suit = Getyaml(path_suit).get_yaml().get("main-list")
data_case = Getyaml(path_case).get_yaml().get("case-list")


@ddt
class yamlPage(unittest.TestCase):
    """
    value = value.split(',')[0].replace("'", "")
    修改用例名过长的问题
    在ddt.py中的mk_test_name方法中添加在倒数第三行
    order by taolei
    """
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.BasePage = BasePage(self.driver)
        self.driver.get(url)
        time.sleep(1)

    @data(*data_suit)
    @unpack
    def test_yml(self, args, username, password, check):
        logger.debug("测试的用例是:{0} ; 用户名: {1} ; 密码: {2}".format(args, username, password))
        for i in range(1, len(data_case)):          
            if data_case[i][0] == "hs-input":
                if data_case[i][1] == "id":
                    if "username" in data_case[i][3]:
                        self.BasePage.input(By.ID, data_case[i][2], text=username)
                    if "password" in data_case[i][3]:
                        BasePage.input(By.ID, data_case[i][2], text=password)
                if data_case[i][1] == "name":
                    if "username" in data_case[i][3]:
                        self.BasePage.input(By.NAME, data_case[i][2], text=username)
                    if "password" in data_case[i][3]:
                        self.BasePage.input(By.NAME, data_case[i][2], text=password)
                if data_case[i][1] == "xpath":
                    if "username" in data_case[i][3]:
                        self.BasePage.input(By.XPATH, data_case[i][2], text=username)
                    if "password" in data_case[i][3]:
                        self.BasePage.input(By.XPATH, data_case[i][2], text=password)
            if data_case[i][0] == 'hs-click':
                if data_case[i][1] == "id":
                    self.BasePage.click(By.ID, data_case[i][2])
                if data_case[i][1] == "name":
                    self.BasePage.click(By.NAME, data_case[i][2])
                if data_case[i][1] == "xpath":
                    self.BasePage.click(By.XPATH, data_case[i][2])
                time.sleep(3)
        logger.info("该条测试用例的执行结果是: " + check)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
