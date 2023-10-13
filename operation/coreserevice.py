"""
-*- coding: utf-8 -*-
"""
import json
import os
from core.result_base import ResultBase
from api.core import CoreService
from common.logger import logger
import re
from common.mysql_operate import db

core = CoreService()


class Report():
    def AnalysisList(self, title,  except_result, expect_code, expect_msg, core_token):
        header = {
            "apiVersion": '42',
            "appVersion": '1.35.0',
            "authToken": core_token,
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'

        }
        res = core.AnalysisList(headers=header)
        logger.info(res)


        #
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg,expect_msg, res)  # 断言code和message

    def CycleStatus(self, title, cycleNumber, except_result, expect_code, expect_msg, core_token):
        header = {
            "apiVersion": '42',
            "appVersion": '1.35.0',
            "authToken": core_token,
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'

        }
        json_data = {"cycleNumber": cycleNumber}
        res = core.CycleStatus(headers=header, params=json_data)
        logger.info(res)
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def ShareAnalysis(self, title, cycleNumber,email,cycleEndNumber,id, except_result, expect_code, expect_msg, core_token):
        header = {
            "Content-Type": "application/json",
            "apiVersion": '42',
            "appVersion": '1.35.0',
            "authToken": core_token,
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'

        }
        json_data = {"cycleNumber": cycleNumber,
                     "email": email,
                     "cycleEndNumber": cycleEndNumber,
                     "id": id

                     }
        res = core.ShareAnalysis(headers=header, json=json_data)
        logger.info(res)
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def ComparisonList(self, title,  except_result, expect_code, expect_msg, core_token):
        header = {
            "apiVersion": '43',
            "appVersion": '1.36.0',
            "authToken": core_token,
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'

        }
        res = core.ComparisonList(headers=header)
        logger.info(res)


        #
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg,expect_msg, res)  # 断言code和message

    def ShareComparison(self, title, cycleNumber, email, cycleEndNumber, id, except_result, expect_code, expect_msg, core_token):
        header = {
            "Content-Type": "application/json",
            "apiVersion": '43',
            "appVersion": '1.36.0',
            "authToken": core_token,
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'

        }
        json_data = {"cycleNumber": cycleNumber,
                     "email": email,
                     "cycleEndNumber": cycleEndNumber,
                     "id": id

                     }
        res = core.ShareAnalysis(headers=header, json=json_data)
        logger.info(res)
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message



class Insemination():
    def inseminationAddOrUpdate(self, title, id, frozenSperm, noInsemination, noneOfTheAbove, triggerShot, type, expect_code, expect_msg, core_token, get_current_date):
        """增加或更新受精记录"""
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "authToken":core_token
        }
        json_data = {
            "id": id,
            "frozenSperm": frozenSperm,
            "noInsemination": noInsemination,
            "noneOfTheAbove": noneOfTheAbove,
            "time": get_current_date,
            "triggerShotDate":get_current_date,
            "triggerShot": triggerShot,
            "type": type
        }
        res = core.InseminationAdd(headers=header, json=json_data)
        logger.info(res.text)
        # logger.info("预期code===>> {}".format(expect_code))
        # logger.info("实际code===>> {}".format(res.status_code))
        # logger.info("预期msg===>> {}".format(expect_msg))
        # logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message
        sql = 'DELETE FROM core.insemination_log WHERE user_id = 26332287 AND time LIKE"2023-10-1%";'
        sql2 = 'select * from core.insemination_log WHERE user_id = 26332287;'
        sql_res = db.select_db(sql)
        sql_res2 = db.select_db(sql2)
        logger.info(sql_res2)
        logger.info(sql_res)


    def inseminationDataGet(self, title, recordDate, expect_code, expect_msg, core_token):
        """根据日期，获取受经记录"""
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "authToken": core_token
        }
        data = {
            "recordDate":recordDate
        }
        res = core.inseminationDataGet(headers=header, params=data)
        logger.info(res.text)
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        # ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message


    def dailyRecordGetSetting(self, title, expect_code, expect_msg, core_token):
        """用户每日记录设置"""
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "authToken": core_token
        }
        res = core.dailyRecordGetSetting(headers=header)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def inseminationGetTip(self, title, editCycle, editDate, expect_code, expect_msg, core_token):
        """获取提示文案"""
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "authToken": core_token
        }
        data = {
            "editCycle":editCycle,
            "editDate":editDate
        }
        res = core.inseminationGetTip(headers=header,params=data)
        # logger.info(res.text)
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def inseminationLogSexKeepOrChangeBtn(self, title, keepLogSex, expect_code, expect_msg, core_token):
        """保留或更换home页面LogSex按钮"""
        header = {
            "Content-Type": "application/json",
            "authToken":core_token
        }
        json_data = {
            "keepLogSex":keepLogSex,
            "authToken": core_token
        }
        res = core.inseminationLogSexKeepOrChangeBtn(headers=header, params=json_data)
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        # logger.info("预期msg===>> {}".format(expect_msg))
        # logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def dailyRecordUpdateSetting(self, title, enable, order, settingType, expect_code, expect_msg, core_token):
        """更新用户每日记录设置"""
        header = {
            "Content-Type": "application/json",
            "authToken": core_token
        }
        json_data = {
            "items": [
                {
                    "enable": enable,
                    "name": "",
                    "order": order,
                    "settingType": settingType
                }
            ]
        }
        res = core.dailyRecordUpdateSetting(headers=header, json=json_data)
        # logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def dailyRecordMomentGet(self, title, expect_code, expect_msg, core_token, get_current_date):
        """获取用户Moment分享-每日记录数据"""
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "authToken": core_token
        }
        json_data = {
            "queryDay":get_current_date
        }
        res = core.dailyRecordMomentGet(headers=header, params=json_data)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def BBTPopupPageInfo(self, title, expect_code, expect_msg, core_token):
        """BBT操作视频弹窗信息"""
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "authToken": core_token
        }
        res = core.BBTPopupPageInfo(headers=header)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def prePregnancyGet(self, title, expect_code, expect_msg, core_token):
        """根据用户获取孕前信息记录"""
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "authToken": core_token
        }
        res = core.prePregnancyGet(headers=header)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message