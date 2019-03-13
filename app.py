#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-13 10:18
# @Author  : zhangzhen
# @Site    : 
# @File    : app.py
# @Software: PyCharm
from flask import Flask, request, Response
import json

from logists.csv_utils import columns_mapper_entity

app = Flask(__name__)


@app.route("/")
def index():
    text = {"code": 200, "text": "hi, default request"}
    return Response(json.dumps(text), mimetype='application/json')


@app.route("/litemind/csv2graph", methods=['POST'])
def columns2entities():
    print(request.args)
    filename = request.json.get("filename")
    data = request.json.get("data", [])
    print(filename, data)
    # 校验参数的正确性
    if filename and isinstance(data, list) and len(data) > 0 and isinstance(data[0], list):
        # 执行csv2graph解析
        reJson = columns_mapper_entity(filename, data)
        return Response(json.dumps(reJson), mimetype='application/json')
    else:
        return Response(json.dumps({'code': '201', 'msg': '接口参数异常'}))


if __name__ == "__main__":
    app.run(debug=True, port=1234)
