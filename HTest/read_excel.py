#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# order by taolei
import xlrd

# 读取全部数据
class ReadExcel:
    def __init__(self, filename, sheet_name="Sheet1"):
        self.data = xlrd.open_workbook(filename)
        self.table = self.data.sheet_by_name(sheet_name)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def get_data(self):
        data = []
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                data.append(s)
                j += 1
        return data


if __name__ == "__main__":
    filepath = "../Project/test_py/login_data.xls"
    data = ReadExcel(filepath)
    print(data.get_data())
