#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-10 17:35
# @Author  : zhangzhen
# @Site    : 
# @File    : unit_test.py
# @Software: PyCharm
from logists.csv_utils import columns_mapper_entity
filename = "2018年6月份联通话单.xlsx"
filename = "13567488934标准的移动通话详单(1).xlsx"

data = [['话单起始时间', '对方IMSI', '小区', '对方区号', '本机号码', '呼叫类型', '通话地点区号', '本机IMEI', '通话时长（秒）', '对方号码', '通话开始时间', '本机IMSI', '通话地', '联系人姓名', '通话类型', '通话结束时间', '蜂窝号', '对方归属地'], ['6/2/18', '460090002045256', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '22分16秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/2/18 14:09', '460090002045276', '0311', '张浩然', '本地通话', '6/2/18 14:31', '25622', '河北石家庄'], ['6/4/18', '460090002043276', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '9秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/4/18 13:36', '460090002045276', '0311', '王明杰', '本地通话', '6/4/18 13:36', '53692', '河北石家庄'], ['6/4/18', '460060002045276', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '12秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/4/18 18:17', '460090002045276', '0311', '孙立成', '本地通话', '6/4/18 18:17', '23688', '河北石家庄'], ['6/4/18', '460090002045243', '12546', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '15秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/4/18 19:33', '460090002045276', '0311', '李丽辉', '本地通话', '6/4/18 19:33', '41972', '河北石家庄'], ['6/4/18', '460090002043276', '12546', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '1分2秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/4/18 19:34', '460090002045276', '0311', '刘志远', '本地通话', '6/4/18 19:35', '13538', '河北石家庄'], ['6/4/18', '460090002044234', '12546', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '30秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/4/18 20:31', '460090002045276', '0311', '张骏驰', '本地通话', '6/4/18 20:31', '10731', '河北石家庄'], ['6/6/18', '460090002049080', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '3分4秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/6/18 8:14', '460090002045276', '0311', '刘玉泽', '本地通话', '6/6/18 8:17', '43692', '河北石家庄'], ['6/6/18', '460090002079700', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '2秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/6/18 17:29', '460090002045276', '0311', '王旭', '本地通话', '6/6/18 17:30', '63692', '河北石家庄'], ['6/6/18', '460090002003435', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '1分13秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/6/18 18:36', '460090002045276', '0311', '孙涛', '本地通话', '6/6/18 18:36', '33358', '河北石家庄'], ['6/7/18', '460090002025151', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '23秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/7/18 11:47', '460090002045276', '0311', '张杰', '本地通话', '6/7/18 11:47', '25622', '河北石家庄'], ['6/7/18', '460090002051515', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '1分9秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/7/18 11:48', '460090002045276', '0311', '刘子璇', '本地通话', '6/7/18 11:49', '35621', '河北石家庄'], ['6/7/18', '460090002098451', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '57秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/7/18 11:49', '460090002045276', '0311', '吴天磊', '本地通话', '6/7/18 11:50', '25622', '河北石家庄'], ['6/7/18', '460090002054789', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '19秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/7/18 12:32', '460090002045276', '311', '孙修杰', '本地通话', '6/7/18 12:32', '33358', '河北石家庄'], ['6/7/18', '460090002010581', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '45秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/7/18 16:46', '460090002045276', '0311', '钱明轩', '本地通话', '6/7/18 16:46', '25622', '河北石家庄'], ['6/7/18', '460090002023441', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '22秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/7/18 16:52', '460090002045276', '0311', '蔡国源', '本地通话', '6/7/18 16:52', '35621', '河北石家庄'], ['6/8/18', '460090002043525', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '49秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/8/18 20:13', '460090002045276', '0311', '崔宏博', '本地通话', '6/8/18 20:13', '33358', '河北石家庄'], ['6/9/18', '460090002015019', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '8分37秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/9/18 19:59', '460090002045276', '0311', '金鑫', '本地通话', '6/9/18 19:59', '20791', '河北石家庄'], ['6/10/18', '460090002078155', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '21秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/10/18 18:54', '460090002045276', '0311', '傅俊明', '本地通话', '6/10/18 18:54', '63692', '河北石家庄'], ['6/11/18', '460090002081515', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '41秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/11/18 8:04', '460090002045276', '0311', '谷建明', '本地通话', '6/11/18 8:04', '13742', '河北石家庄'], ['6/11/18', '460090002069154', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '1分13秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/11/18 18:13', '460090002045276', '0311', '刘靖童', '本地通话', '6/11/18 18:13', '33358', '河北石家庄'], ['', '', '', ''], ['', '', '', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], ['']]
data = [['话单起始时间', '对方IMSI', '小区', '对方区号', '本机号码', '呼叫类型', '通话地点区号', '本机IMEI', '通话时长（秒）', '对方号码', '通话开始时间', '本机IMSI', '通话地', '联系人姓名', '通话类型', '通话结束时间', '蜂窝号', '对方归属地'], ['6/2/18', '460090002045256', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '22分16秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/2/18 14:09', '460090002045276', '0311', '张浩然', '本地通话', '6/2/18 14:31', '25622', '河北石家庄'], ['6/4/18', '460090002043276', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '9秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/4/18 13:36', '460090002045276', '0311', '王明杰', '本地通话', '6/4/18 13:36', '53692', '河北石家庄'], ['6/4/18', '460060002045276', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '12秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/4/18 18:17', '460090002045276', '0311', '孙立成', '本地通话', '6/4/18 18:17', '23688', '河北石家庄'], ['6/4/18', '460090002045243', '12546', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '15秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/4/18 19:33', '460090002045276', '0311', '李丽辉', '本地通话', '6/4/18 19:33', '41972', '河北石家庄'], ['6/4/18', '460090002043276', '12546', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '1分2秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/4/18 19:34', '460090002045276', '0311', '刘志远', '本地通话', '6/4/18 19:35', '13538', '河北石家庄'], ['6/4/18', '460090002044234', '12546', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '30秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/4/18 20:31', '460090002045276', '0311', '张骏驰', '本地通话', '6/4/18 20:31', '10731', '河北石家庄'], ['6/6/18', '460090002049080', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '3分4秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/6/18 8:14', '460090002045276', '0311', '刘玉泽', '本地通话', '6/6/18 8:17', '43692', '河北石家庄'], ['6/6/18', '460090002079700', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '2秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/6/18 17:29', '460090002045276', '0311', '王旭', '本地通话', '6/6/18 17:30', '63692', '河北石家庄'], ['6/6/18', '460090002003435', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '1分13秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/6/18 18:36', '460090002045276', '0311', '孙涛', '本地通话', '6/6/18 18:36', '33358', '河北石家庄'], ['6/7/18', '460090002025151', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '23秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/7/18 11:47', '460090002045276', '0311', '张杰', '本地通话', '6/7/18 11:47', '25622', '河北石家庄'], ['6/7/18', '460090002051515', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '1分9秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/7/18 11:48', '460090002045276', '0311', '刘子璇', '本地通话', '6/7/18 11:49', '35621', '河北石家庄'], ['6/7/18', '460090002098451', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '57秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/7/18 11:49', '460090002045276', '0311', '吴天磊', '本地通话', '6/7/18 11:50', '25622', '河北石家庄'], ['6/7/18', '460090002054789', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '19秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/7/18 12:32', '460090002045276', '311', '孙修杰', '本地通话', '6/7/18 12:32', '33358', '河北石家庄'], ['6/7/18', '460090002010581', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '45秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/7/18 16:46', '460090002045276', '0311', '钱明轩', '本地通话', '6/7/18 16:46', '25622', '河北石家庄'], ['6/7/18', '460090002023441', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '22秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/7/18 16:52', '460090002045276', '0311', '蔡国源', '本地通话', '6/7/18 16:52', '35621', '河北石家庄'], ['6/8/18', '460090002043525', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '49秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/8/18 20:13', '460090002045276', '0311', '崔宏博', '本地通话', '6/8/18 20:13', '33358', '河北石家庄'], ['6/9/18', '460090002015019', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '8分37秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/9/18 19:59', '460090002045276', '0311', '金鑫', '本地通话', '6/9/18 19:59', '20791', '河北石家庄'], ['6/10/18', '460090002078155', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '21秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/10/18 18:54', '460090002045276', '0311', '傅俊明', '本地通话', '6/10/18 18:54', '63692', '河北石家庄'], ['6/11/18', '460090002081515', '1806', '0311', '18646648267', '被叫', '0311', '38 498507 055812 1', '41秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/11/18 8:04', '460090002045276', '0311', '谷建明', '本地通话', '6/11/18 8:04', '13742', '河北石家庄'], ['6/11/18', '460090002069154', '1806', '0311', '18646648267', '主叫', '0311', '38 498507 055812 1', '1分13秒', 'CHOOSE(RANDBETWEEN(1,3),1515204,1589525,1390522)&TEXT(RANDBETWEEN(0,10^4-1),"0000")', '6/11/18 18:13', '460090002045276', '0311', '刘靖童', '本地通话', '6/11/18 18:13', '33358', '河北石家庄'], ['', '', '', ''], ['', '', '', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], ['', ''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], [''], ['']]
data = [['本机号码', '起始时间', '通信地点', '通信方式', '对方号码', '通信时长', '通信类型', '套餐优惠', '实收通信费(元)'], ['1.5152042908E10', '2017-12-01 14:39:01', '北京', '主叫', '1.581125653E10', '32秒', '本地主叫本地', '语音38元套餐', '0.0'], ['1.5152048084E10', '2017-12-01 14:44:15', '北京', '被叫', '1.7701261029E10', '52秒', '国内被叫', '', '0.0'], ['1.3905228345E10', '2017-12-01 16:01:52', '北京', '主叫', '1.7701261029E10', '01分13秒', '本地主叫本地', '语音38元套餐', '0.0'], ['1.5895252163E10', '2017-12-01 16:03:25', '北京', '被叫', '1.7701261029E10', '01分22秒', '国内被叫', '', '0.0'], ['1.5152043422E10', '2017-12-05 17:30:08', '北京', '被叫', '1.095078001E9', '01分25秒', '国内被叫', '', '0.0'], ['1.5895253853E10', '2017-12-05 21:18:14', '北京', '主叫', '1.8310308983E10', '36秒', '本地主叫本地', '语音38元套餐', '0.0'], ['1.5895253805E10', '2017-12-06 19:35:22', '北京', '主叫', '1.3811117584E10', '44秒', '本地主叫本地', '语音38元套餐', '0.0'], ['1.3905225315E10', '2017-12-06 19:47:56', '北京', '主叫', '1.8911900032E10', '02分49秒', '本地主叫本地', '语音38元套餐', '0.0'], ['1.515204315E10', '2017-12-06 20:02:52', '北京', '被叫', '1.8911900032E10', '33秒', '国内被叫', '', '0.0']]
data = [['起始时间', '通信地点', '通信方式', '对方号码', '通信时长', '通信类型', '套餐优惠', '实收通信费(元)'], ['2017-12-01 14:39:01', '北京', '主叫', '8.61581125653E12', '32秒', '本地主叫本地', '语音38元套餐', '0.0'], ['2017-12-01 14:44:15', '北京', '被叫', '1.7701261029E10', '52秒', '国内被叫', '', '0.0'], ['2017-12-01 16:01:52', '北京', '主叫', '1.7701261029E10', '01分13秒', '本地主叫本地', '语音38元套餐', '0.0'], ['2017-12-01 16:03:25', '北京', '被叫', '1.7701261029E10', '01分22秒', '国内被叫', '', '0.0'], ['2017-12-05 17:30:08', '北京', '被叫', '1.095078001E9', '01分25秒', '国内被叫', '', '0.0'], ['2017-12-05 21:18:14', '北京', '主叫', '1.8310308983E10', '36秒', '本地主叫本地', '语音38元套餐', '0.0'], ['2017-12-06 19:35:22', '北京', '主叫', '1.3811117584E10', '44秒', '本地主叫本地', '语音38元套餐', '0.0'], ['2017-12-06 19:47:56', '北京', '主叫', '1.8911900032E10', '02分49秒', '本地主叫本地', '语音38元套餐', '0.0'], ['2017-12-06 20:02:52', '北京', '被叫', '1.8911900032E10', '33秒', '国内被叫', '', '0.0']]

rs = columns_mapper_entity(filename, data)
print(rs)