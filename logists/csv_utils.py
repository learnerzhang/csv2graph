#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-13 14:54
# @Author  : zhangzhen
# @Site    : 
# @File    : csv_utils.py.py
# @Software: PyCharm
import pandas as pd
import collections
import logging
import time
import re

logger = logging.getLogger(__name__)


def get_phone_num(txt):
    # type: (Text) -> Text
    """
    从文本中抽取第一个手机号码
    :param txt:
    :return:
    """
    re_str = "((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18[0-9])|166|198|199|(147))\\d{8}"
    pattern = re.compile(re_str)
    target = list(pattern.finditer(txt))
    if target:
        return target[0].group()
    return None


def convertcol2dats(data, titleRegStr):
    """
    转化数据格式
    :param data:
    [ [d11, d12, ...],[d21,d22,...]...]
    :return:
    {
        c1: [d11, d21,...]
        c2: [d21, d22,...]
    }
    """
    col2dats = collections.defaultdict(list)
    # 取第一行做表头判断
    valid_head = collections.Counter([containsTitleKey(d, titleRegStr) for d in data[0] if d]).most_common(1)[0]
    # print(valid_head)
    if isinstance(valid_head[0], bool):
        origin_titles = data[0]
        data = data[1:]
    else:
        origin_titles = []

    titles = list(range(0, len(data[0])))
    for dat in data:
        for i, (col, val) in enumerate(zip(titles, dat)):
            col2dats[col].append(val)
    return origin_titles, titles, col2dats


def containsTitleKey(txt, regStr):
    """
    判断是否为表头
    :param txt:
    :return:
    """
    keyword_pattern = re.compile(regStr)
    tartget = keyword_pattern.search(txt)
    if tartget:
        return True
    else:
        return txt


def get_ent_type(txt):
    # type: (Text) -> Text
    """
    根据字段判断所属类型
    :param txt:
    :return:
    """
    if txt is None:
        return "null"
    rules_pool = {
        "sjhm": "((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18[0-9])|166|198|199|(147))\\d{8}",
        "thsc": "((([1-5][0-9])|[1-9])秒)",
        "thlx": "(主叫|短信)",
        "jzh": "(SAIE)",
        "thsj": "(([0-1][0-9]|(2[0-4])):([0-5][0-9]):([0-5][0-9]))",
        "lddw": "(黑龙江|吉林|辽宁|江苏|山东|安徽|河北|河南|湖北|湖南|江西|陕西|山西|四川|青海|海南|广东|贵州|浙江|福建|台湾|甘肃|云南|内蒙古|宁夏|新疆|西藏|广西|北京|上海|天津|重庆|香港|澳门)"
    }
    # 匹配手机号

    for key, val in rules_pool.items():
        pattern = re.compile(val)
        target = pattern.search(txt)
        if target:
            return key
    return 'unk'


def title_mapper_entity(title, col2dats):
    col2ent = {col: None for col in title}  # 列对应的实体
    ent2cols = collections.defaultdict(set)
    for c_title, dats in col2dats.items():
        # 判断该列是否存在对应的实体
        tmp_tpyes = []
        for col_txt in dats:
            # 根据 txt 判断col 的类型
            ent_type = get_ent_type(col_txt)  # 获取该txt的实体类型
            tmp_tpyes.append(ent_type)

        # 需要判断 第二多的列
        typ = collections.Counter(tmp_tpyes).most_common(2)  # 统计每列识别的类型, 选取最多
        if len(typ) > 1:
            typ0, num0 = typ[0][0], typ[0][1]
            typ1, num1 = typ[1][0], typ[1][1]
            # TODO compare the nums
            if typ0 == 'unk':
                _typ = typ1
            else:
                _typ = typ0
        else:
            _typ = typ[0][0]
        col2ent[c_title] = _typ  # col -> ent
        ent2cols[_typ].add(c_title)  # ent -> cols
    return col2ent, ent2cols


def validate_format(bjhm, ent2cols, col2dats):
    """验证表单的是否异常
        1、包含两列手机号, 一列时间
        2、文件名吧包含手机号、文件存在一列手机号, 一列时间
        3、其他均为异常文件
    """

    def valid_c1():
        return len(ent2cols['sjhm']) == 2

    def valid_c2():
        row_key = list(ent2cols['sjhm'])[0]
        col_sjhm_txt = collections.Counter(col2dats[row_key]).most_common(1)[0]
        if bjhm and bjhm not in col_sjhm_txt[0]:
            return True
        else:
            return False

    if 'sjhm' in ent2cols and 'thsj' in ent2cols and len(ent2cols['thsj']) >= 1:
        if valid_c1() or valid_c2():
            return True
    return False


def columns_mapper_entity(filename, data):
    """
    :param filename:
        185xxxxx.csv/张三的表单.csv
    :param data:
        [
            [c1,c2,...],
            ["185xxx","xxx",...],
            ["185xxx","xxx",...],
            ["185xxx","xxx",...],
            ....
        ]
    :return:
        {
            'entities':
                {'sjhm': ['手机号码'],
                'thsc': ['通话时长'],
                'thlx': ['通话类型'],
                'jzh': ['基站号'],
                'lddw': ['通话定位'],
                'thkssj': ['通话开始时间', '通话结束时间'],
                'thjssj': ['通话开始时间', '通话结束时间']
                },
            'origin_titles': [],  ---原始表头, 不存在为空
            'titles': [手机号码','第二列','通话时长','通话类型','基站号','通话开始时间','通话结束时间','通话定位','第九列','第十列'] ---新解析表头
        }
    """

    title_template = {
        'sjhm': '手机号码',
        'bjhm': '本机号码',
        'dfhm': '对方号码',
        'thlx': '通话类型',
        'thsc': '通话时长',
        'thsj': '通话时间',
        'sj': '时间',
        'thkssj': '通话开始时间',
        'thjssj': '通话结束时间',
        'lddw': '通话定位',
        'jzh': '基站号',
        'unk': '未知',
    }
    # 获取主叫号码
    bjhm = get_phone_num(filename)  # 从文件名提前手机号,可能为None

    # 转化文件名
    origin_titles, titles, col2dats = convertcol2dats(data, titleRegStr="(时间|号码|定位|类型)")
    # print(col2dats)
    # # col -> ent # ent -> cols
    col2ent, ent2cols = title_mapper_entity(titles, col2dats)
    # print(col2ent)
    # print(ent2cols)
    # 验证数据是否正确

    try:
        assert validate_format(bjhm, ent2cols, col2dats)
    except AssertionError:
        # print("数据格式不正确, 返回文件格式异常错误")
        logging.warning("数据格式不正确, 返回文件格式异常错误")
        return {'code': 202, 'msg': '话单数据格式异常'}

    need_deal_ent = ['sjhm', 'thsj']
    entities = {e: list(cs) for e, cs in ent2cols.items() if len(cs) == 1 and e not in need_deal_ent}

    # Step 0 处理手机号
    cols_sjhm = list(ent2cols['sjhm'])
    fileinfo = {'bjhm': bjhm if bjhm else ""}  # 文件名信息
    if len(cols_sjhm) == 2:
        col1, col2 = cols_sjhm[0], cols_sjhm[1]
        c1, c2 = subject_object_phone(col1, col2, col2dats, bjhm)
        col2ent[c1], col2ent[c2] = 'bjhm', 'dfhm'
        ent2cols['bjhm'].add(c1)
        ent2cols['dfhm'].add(c2)
        entities.update({'bjhm': [col1, col2]})
        entities.update({'dfhm': [col2, col1]})
        fileinfo.update({'isUseed': False})
    else:
        col = cols_sjhm[0]
        col2ent[col] = 'dfhm'
        ent2cols['dfhm'] = col
        entities.update({'bjhm': ['文件名']})
        entities.update({'dfhm': cols_sjhm})
        fileinfo.update({'isUseed': True})

    # Step 1 处理通话时间
    cols_thsj = list(ent2cols['thsj'])
    # print("通话时间", cols_thsj)
    if len(cols_thsj) == 2:
        col1, col2 = cols_thsj[0], cols_thsj[1]
        rs = compare_time(col1, col2, col2dats)
        if rs == 1:
            col2ent[col1], col2ent[col2] = 'thkssj', 'thjssj'
            ent2cols['thkssj'].add(col1)
            ent2cols['thjssj'].add(col2)
            entities.update({'thkssj': [col1, col2]})
            entities.update({'thjssj': [col2, col1]})
        else:  # None, -1, 0
            col2ent[col2], col2ent[col1] = 'thkssj', 'thjssj'
            ent2cols['thkssj'].add(col2)
            ent2cols['thjssj'].add(col1)
            entities.update({'thjssj': [col1, col2]})
            entities.update({'thkssj': [col2, col1]})
    else:
        col = cols_thsj[0]
        ent2cols['thkssj'].add(col)
        ent2cols['thjssj'].add(col)
        entities.update({'thkssj': cols_thsj})
        entities.update({'thjssj': cols_thsj})

    # Step 3 基站号
    if len(ent2cols['jzh']) == 0 and origin_titles:
        for i, title in enumerate(origin_titles):
            if isinstance(containsTitleKey(title, regStr="(基站)"), bool):
                ent2cols['jzh'].add(i)
                col2ent[i] = title
                titles[i] = title
                entities.update({'jzh': [title]})

    # 标准化
    tilte_dict = {}
    # print(col2ent)
    for k, v in col2ent.items():
        # print(k, v)
        # print(k, v, title_template[v])
        if v == 'unk' or v == 'null':
            tilte_dict[k] = '第%s列' % num2chinese(k + 1)
        elif v in title_template:
            tilte_dict[k] = title_template[v]

    # print(tilte_dict)
    for k, vals in entities.items():
        opts = []
        for val in vals:
            if val in tilte_dict:
                opts.append(tilte_dict[val])
            else:
                opts.append(val)
        # print(opts)
        entities[k] = opts

    # 返回新定义格式
    _entities = {title_template[k]:v  for k, v in entities.items()}

    _titles = []
    for t in titles:
        if t in tilte_dict:
            _titles.append(tilte_dict[t])
        elif isinstance(t, int):
            _titles.append("第%s列" % num2chinese(t + 1))
        else:
            _titles.append(t)

    logging.info("[*] entities:{}| origin_titles:{}| title:{}".format(_entities, origin_titles, _titles))
    return {
        'code': 200,
        'data': {
            'entities': _entities,
            'fileinfo': fileinfo,
            'origin_titles': origin_titles,
            'titles': _titles
        }
    }


def subject_object_phone(col1, col2, col_dat, bjhm):
    """
    判断col1,col2 两列中那个是主叫号码和被叫号码
    :param col1:
    :param col2:
    :param col_dat:
    :param zjhm:
    :return:
    """
    phone_col1s = []
    phone_col2s = []
    for e1, e2 in zip(col_dat[col1], col_dat[col2]):
        phone_col1s.append(e1)
        phone_col2s.append(e2)
    col1_phone, col1_num = collections.Counter(phone_col1s).most_common(1)[0]
    col2_phone, col2_num = collections.Counter(phone_col2s).most_common(1)[0]
    # print(col1, col2)
    # print(col1_num, col2_num)
    if bjhm:
        """根据文件名来确认本机号码"""
        if bjhm == col1_phone:
            return col1, col2
        else:
            return col2, col1
    else:
        if col1_num >= col2_num:
            return col1, col2
        else:
            return col2, col1


def num2chinese(num):
    num2chi = {
        0: '零',
        1: '一',
        2: '二',
        3: '三',
        4: '四',
        5: '五',
        6: '六',
        7: '七',
        8: '八',
        9: '九',
        10: '十',
        11: "十一",
        12: "十二",
        13: "十三",
        14: "十四",
        15: "十五",
        16: "十六",
        17: "十七",
        18: "十八",
        19: "十九",
        20: "二十",
        21: "二十一",
        22: "二十二",
        23: "二十三",
        24: "二十四",
    }
    return num2chi[num]


def compare_time(col1, col2, col_dat, specific_row=None):
    """
    比较col1, col2两列的时间的大小, col1 < col2: 1; col1 = col2: 0; col1 > col2: -1
    specific_row: 是否具体制定某一行
    :param col1:
    :param col2:
    :param col_dat:
    :param specific_row:
    :return:
    """
    _ent1, _ent2 = None, None
    rs = []

    for i, (e1, e2) in enumerate(zip(col_dat[col1], col_dat[col2])):
        if specific_row and specific_row < len(col_dat[col1]) + 1:
            if i + 1 == specific_row:
                _ent1, _ent2 = e1, e2
                break
        else:
            if e1 and e2:
                _ent1, _ent2 = e1, e2
                # 比较时间大小
                t1 = date2timestamp(_ent1)
                t2 = date2timestamp(_ent2)
                if t1 is None or t2 is None:
                    continue
                if t1 < t2:
                    rs.append(1)
                elif t1 > t2:
                    rs.append(-1)
                else:
                    rs.append(0)
    if len(rs) == 0:
        return None
    else:
        return collections.Counter(rs).most_common(1)[0][0]


def date2timestamp(date):
    # type: (Text) -> Float
    # 格式化时间
    format_time = date
    # 时间
    try:
        ts = time.strptime(format_time, "%Y-%m-%d %H:%M:%S")
        # 格式化时间转时间戳
        return time.mktime(ts)
    except ValueError:
        return None


if __name__ == '__main__':
    filename = "13018866666的话单.csv"
    # filename = "13018811509的话单.csv"
    # filename = "demo.xls"
    dat_csv = pd.read_csv(filename, header=None)
    # dat_csv = pd.read_excel(filename, header=None)
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
