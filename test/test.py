#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-13 10:26
# @Author  : zhangzhen
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import requests
from urllib import parse
import pandas as pd
import json

from logists.csv_utils import columns_mapper_entity


def test_1():
    filename = '18518067686'
    data = [['15522453452', '2018-08-21 12:32:21', '', '短信', '1分42秒']]
    print(filename, data)
    rs = columns_mapper_entity(filename, data)
    print(rs)


def test_post_api():
    url = 'http://127.0.0.1:1234/litemind/csv2graph'
    postData = {
        "filename": '18518067686的话单.csv',
        "data": [['15522453452', '2018-08-21 12:32:21', '', '短信', '1分42秒']],
    }
    res = requests.post(url, json=postData)
    rsJson = json.loads(res.text)
    print(rsJson)


def test_post_api1():
    url = 'http://d65.mlamp.cn:1234/litemind/csv2graph'
    postData = {
        "filename": '18518067686的话单.csv',
        "data": [
            ['号码', '时间', '第三列', '类型', '时长'],
            ['15522453452', '2018-08-21 12:32:21', '', '短信', '1分42秒'],
            ['15522453452', '2018-08-21 12:32:21', '', '短信', '1分42秒']],
    }
    res = requests.post(url, json=postData)
    rsJson = json.loads(res.text)
    print(rsJson)


def test_post_api2():
    url = 'http://d65.mlamp.cn:1234/litemind/csv2graph'
    postData = {
        "filename": '18518067686的话单.csv',
        "data": [
            ['号码', '时间', '第三列', '类型', '时长'],
            ['15522453452', '2018-08-21 12:32:21', '', '短信', '1分42秒'],
            ['15522453452', '2018-08-21 12:32:21', '', '短信', '1分42秒']],
    }
    res = requests.post(url, json=postData)
    print(res.text)
    # rsJson = json.loads(res.text)
    # print(rsJson)


def test_post_api3():
    url = 'http://d65.mlamp.cn:1234/litemind/csv2graph'

    filename = "../data/demo.xls"
    filename = "../data/2018年9月份话单(1).xls"
    filename = "../data/13035885069(话单数据).xls"
    filename = "../data/13035885069.xls"
    # filename = "13018866666的话单.csv"
    # filename = "./data/13018866666的话单.csv"
    filename = "../data/本机与对方号码都有2.xlsx"
    filename = "../data/18435109165.xls"
    # filename = "../data/13567488934标准的移动通话详单(1).xlsx"
    # filename = "../data/本机与对方号码都有2.xlsx"
    dat_csv = pd.read_excel(filename, header=None)
    titles = list(dat_csv.columns)
    data = []
    for i, r in dat_csv.iterrows():
        row = []
        for t in titles:
            if pd.notna(r[t]):
                row.append(str(r[t]))
            else:
                row.append(None)
        data.append(row)
    # rs = columns_mapper_entity(filename, data)

    print(data)
    postData = {
        "filename": filename,
        "data": data
    }

    res = requests.post(url, json=postData)
    # print(res.text)
    rsJson = json.loads(res.text)
    print(rsJson)


def test_exec_file():
    filename = "../data/demo.xls"
    filename = "../data/2018年9月份话单(1).xls"
    # filename = "13035885069(话单数据).xls"
    # filename = "13018866666的话单.csv"
    # filename = "./data/13018866666的话单.csv"
    filename = "./data/本机与对方号码都有2.xlsx"
    # filename = "./data/18435109165.xls"
    filename = "./data/13567488934标准的移动通话详单(1).xlsx"
    dat_csv = pd.read_excel(filename, header=None)
    titles = list(dat_csv.columns)
    data = []
    for i, r in dat_csv.iterrows():
        row = []
        for t in titles:
            if pd.notna(r[t]):
                row.append(str(r[t]))
            else:
                row.append(None)
        data.append(row)
    rs = columns_mapper_entity(filename, data)
    print(rs)
