# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
import openpyxl
wb=openpyxl.load_workbook('D:\AirTestsjmama\手机麻麻自动化文档.xlsx')#打开表
sheet=wb['手机麻麻参数']#读取当前表名为手机麻麻参数,get_sheet_by_name()方法已经弃用
row=sheet.rows
def right():
    for i in row:
        if(i[5].value == '右边的位置'):#判断i(每一行)第5列的位置
            print(i[6].value)#然后输出这一行的第7列的值
