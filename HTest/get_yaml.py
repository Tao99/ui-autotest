#!/usr/bin/env python3.7
# _*_ coding:utf-8 _*_
# 读取yaml文件
import pprint
import yaml


class Getyaml:
    def __init__(self, filepath):
        self.path = filepath

    def get_yaml(self):
        """
        读取yaml文件
        :return: Dict
        order by taolei
        """
        f = open(self.path, encoding='utf-8')
        data = yaml.load(f, Loader=yaml.FullLoader)
        f.close()
        return data

    def write_yaml(self, data):
        """
        写入yaml文件
        :param data: [{'database': 'Hs-api', 'port': 21020}, {'url': 'www.baidu.com'}]
        """
        with open(self.path, encoding='utf-8', mode='w') as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    def alldata(self):
        data = self.get_yaml()
        return data

    def caselen1(self):
        data = self.alldata()
        length = len(data)
        return length

    def caselen(self, j):
        data = self.alldata()
        length = len(data[j]['test']['testcase'])
        return length

    def get_title(self, j):
        data = self.alldata()
        return data[j]['test']['testinfo'][0]['title']

    def get_id(self, j):
        data = self.alldata()
        return data[j]['test']['testinfo'][0]['id']

    def get_element_info(self, j, i):
        data = self.alldata()
        return data[j]['test']['testcase'][i]['element_info']

    def get_find_type(self, j, i):
        data = self.alldata()
        return data[j]['test']['testcase'][i]['find_type']

    def get_operate_type(self, j, i):
        data = self.alldata()
        return data[j]['test']['testcase'][i]['operate_type']

    def get_info(self, j, i):
        data = self.alldata()
        return data[j]['test']['testcase'][i]['info']

    def get_send_content(self, j, i):
        data = self.alldata()
        if self.get_operate_type(j, i) == 'send_key':
            return data[j]['test']['testcase'][i]['send_content']
        else:
            pass


if __name__ == '__main__':
    f = "../Project/test_py/login_case.yml"
    data = Getyaml(f).get_yaml()
    pprint.pprint(data)
    pprint.pprint(data.text)
    print(Getyaml(f).caselen1())
    print(f)
