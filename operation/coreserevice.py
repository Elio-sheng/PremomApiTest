"""
-*- coding: utf-8 -*-
"""
import json
import os
from core.result_base import ResultBase
from api.core import CoreService
from common.logger import logger
import re

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
        ResultBase(res, expect_code, expect_msg,
                   expect_msg, res)  # 断言code和message

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
        # logger.info("预期code===>> {}".format(expect_code))
        # logger.info("实际code===>> {}".format(res.status_code))
        # logger.info("预期msg===>> {}".format(expect_msg))
        # logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def ShareAnalysis(self, title, cycleNumber,email,cycleEndNumber,id, except_result, expect_code, expect_msg, core_token):
        header = {
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
        res = core.ShareAnalysis(headers=header, params=json_data)
        logger.info(res)
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

class Insemination():
    def inseminationAddOrUpdate(self, title, id, frozenSperm, noInsemination, noneOfTheAbove, triggerShot, type, expect_code, expect_msg, core_token, get_current_date):
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
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

# class Ezserver():
#     def input_al(self, title, menstruationRecord,expect_code, expect_msg, core_token):
#         header = {
#             "Content-Type": "application/json",
#             "apiVersion": '43',
#             "appVersion": '1.36.0',
#             "authToken": core_token,
#             "os": 'iphone'
#
#         }
#         json_data = {
#                 "param": {
#                     "version": 1
#                 },
#                 "userData": {
#                     "userAverageLuteumLength": 14,
#                     "userAverageCycleLength": 28,
#                     "userAverageMenstruationLength": 5,
#                     "userCycleRegularity": 1,
#                     "userCycleLengthError": 4
#                 },
#                 "daysInput": [{
#                     "cervicalMunusRecord": 0,
#                     "ovulationResultByLH": 0,
#                     "dayOfCycle": 0,
#                     "ovulationResultByUser": 0,
#                     "menstruationRecord": menstruationRecord,
#                     "timestamp": 1696132800,
#                     "BBT": 0,
#                     "impactTempFlag": 0
#                 }, {
#                     "BBT": 0,
#                     "ovulationResultByLH": 0,
#                     "impactTempFlag": 0,
#                     "menstruationRecord": 10,
#                     "dayOfCycle": 0,
#                     "cervicalMunusRecord": 0,
#                     "ovulationResultByUser": 0,
#                     "timestamp": 1696219200
#                 }],
#                 "debug": 0
#         }
#         res = core.InputAl(headers=header, json=json_data)
#         logger.info(res.text)
#         logger.info("预期code===>> {}".format(expect_code))
#         logger.info("实际code===>> {}".format(res.status_code))
#         logger.info("预期msg===>> {}".format(expect_msg))
#         logger.info("实际msg===>> {}".format(res.text))
#         ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message


