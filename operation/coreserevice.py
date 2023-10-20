"""
-*- coding: utf-8 -*-
"""
import requests
import json
import os
from core.result_base import ResultBase
from api.core import CoreService
from common.logger import logger
import re
from common.mysql_operate import db

core = CoreService()

#测试cycle report模块接口
class Report():
    #获取用户周期分析报告列表
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

    # 获取用户周期状态
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

    # 分享用户周期分析报告
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

    #获取周期比较报告列表
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

    # 分享用户周期比较报告
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

    # 获取用户周期分析报告-CM and Positioning Detail/Mood and Symptom Detail
    def CervicalAndMoodAndSymptom(self, title, expect_code, expect_msg, get_userId):
        header = {
            "apiVersion": '43',
            "appVersion": '1.36.0',
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'
        }

        json_data = {"userId": get_userId,
                     "cycleNumber": '1'
                     }


        res = core.CervicalAndMoodAndSymptom(headers=header, params=json_data)
        logger.info(res)

        #
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg,expect_msg, res)  # 断言code和message

    # 获取用户周期分析报告-9-Cycle Guarantee
    def AnalysisGuarantee(self, title, expect_code, expect_msg, get_userId):
        header = {
            "apiVersion": '43',
            "appVersion": '1.36.0',
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'
        }

        json_data = {"userId": get_userId,
                     "cycleNumber": '1'
                     }


        res = core.AnalysisGuarantee(headers=header, params=json_data)
        logger.info(res)

        #
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg,expect_msg, res)  # 断言code和message

    # 获取用户周期分析报告-Overview/LH Pattern
    def AnalysisOverview(self, title, expect_code, expect_msg, get_userId):
        header = {
            "apiVersion": '43',
            "appVersion": '1.36.0',
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'
        }

        json_data = {"userId": get_userId,
                     "cycleNumber": '1'
                     }


        res = core.AnalysisOverview(headers=header, params=json_data)
        logger.info(res)

        #
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg,expect_msg, res)  # 断言code和message


    # 获取用户周期分析报告-Ovulation Tracking
    def AnalysisOvulation(self, title, expect_code, expect_msg, get_userId):
        header = {
            "apiVersion": '43',
            "appVersion": '1.36.0',
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'
        }

        json_data = {"userId": get_userId,
                     "cycleNumber": '1'
                     }


        res = core.AnalysisOvulation(headers=header, params=json_data)
        logger.info(res)

        #
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg,expect_msg, res)  # 断言code和message


    #获取用户周期分析报告-Peak Fertility
    def AnalysisPeakFertility(self, title, expect_code, expect_msg, get_userId):
        header = {
            "apiVersion": '43',
            "appVersion": '1.36.0',
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'
        }

        json_data = {"userId": get_userId,
                     "cycleNumber": '1'
                     }


        res = core.AnalysisPeakFertility(headers=header, params=json_data)
        logger.info(res)

        #
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg,expect_msg, res)  # 断言code和message


    #  获取用户周期分析报告-Cycle Summary
    def AnalysisSummary(self, title, expect_code, expect_msg, get_userId):
        header = {
            "apiVersion": '43',
            "appVersion": '1.36.0',
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'
        }

        json_data = {"userId": get_userId,
                     "cycleNumber": '1'
                     }


        res = core.AnalysisSummary(headers=header, params=json_data)
        logger.info(res)

        #
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg,expect_msg, res)  # 断言code和message


    # 获取用户周期分析报告-用户档案数据
    def AnalysisPeakUser(self, title, expect_code, expect_msg, get_userId):
        header = {
            "apiVersion": '43',
            "appVersion": '1.36.0',
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'
        }

        json_data = {"userId": get_userId,
                     "cycleNumber": '1'
                     }


        res = core.AnalysisPeakUser(headers=header, params=json_data)
        logger.info(res)

        #
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg,expect_msg, res)  # 断言code和message


    # 获取用户Cycle at a Glance-Intercourse Timing
    def GlanceIntercourseTiming(self, title, expect_code, expect_msg, core_token):
        header = {
            "apiVersion": '43',
            "appVersion": '1.36.0',
            "authToken": core_token,
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'

        }

        res = core.GlanceIntercourseTiming(headers=header)
        logger.info(res)

        #
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg,expect_msg, res)  # 断言code和message


    # 获取用户Cycle at a Glance-Predict/Confirm Ovulation
    def GlanceOvulation(self, title, expect_code, expect_msg, core_token):
        header = {
            "apiVersion": '43',
            "appVersion": '1.36.0',
            "authToken": core_token,
            "language": '0',
            "os": 'iphone',
            "timezone": 'Asia/Shanghai'
        }



        res = core.GlanceOvulation(headers=header)
        logger.info(res)

        #
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg,expect_msg, res)  # 断言code和message


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



    def inseminationDataGet(self, title, get_current_date, expect_code, expect_msg, core_token):
        """根据日期，获取受经记录"""
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "authToken": core_token
        }
        data = {
            "recordDate":get_current_date
        }
        res = core.inseminationDataGet(headers=header, params=data)
        logger.info(res.text)
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        # logger.info("预期msg===>> {}".format(expect_msg))
        # logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message
        sql = 'SELECT id FROM core.insemination_log WHERE user_id = 26774415 and time like "2023-10-2%" LIMIT 1;'   #查询当前使劲按生成的受精记录
        sql_res = db.select_db(sql)
        assert res.json()['id'] in str(sql_res[0]["id"])   #断言当前生成的记录id：返回的id=数据库存的id
        delete_sql = 'DELETE FROM core.insemination_log WHERE user_id = 26774415 AND time LIKE"2023-10-2%";'    #删除用户受精记录
        # log_sql = 'select * from core.insemination_log WHERE user_id = 26774415;'   #查看用户受精记录
        delete_sql_res = db.select_db(delete_sql)
        # log_sql_res = db.select_db(log_sql)


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

    def prePregnancySave(self, title, height, heightUnit, weight, weightUnit, expect_code, expect_msg, core_token):
        """保存孕前信息记录"""
        header = {
            "Content-Type": "application/json",
            "authToken": core_token
        }
        json_data = {
            "height": height,
            "heightUnit": heightUnit,
            "weight": weight,
            "weightUnit": weightUnit
        }
        res = core.prePregnancySave(headers=header, json=json_data)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def mooeGet(self, title, recordDate, expect_code, expect_msg, core_token):
        """获取用户心情记录"""
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "authToken": core_token
        }
        json_data = {
            "recordDate":recordDate
        }
        res = core.mooeGet(headers=header, params=json_data)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def medicineGalleryGet(self, title, expect_code, expect_msg, core_token):
        """获取用户药品记录"""
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "authToken": core_token
        }
        res = core.medicineGalleryGet(headers=header)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def medicineGalleryUpdate(self, title, category, categoryOrder, deleted, intakeNumber, medicineId,
                                    name, order, reminder, reminderTime, type, expect_code, expect_msg, core_token):
        """更新用户药品记录"""
        header = {
            "Content-Type": "application/json",
            "authToken": core_token
        }
        json_data = {
            "category": category,
            "categoryOrder": categoryOrder,
            "deleted": deleted,
            "intakeNumber": intakeNumber,
            "medicineId": medicineId,
            "name": name,
            "order": order,
            "reminder": reminder,
            "reminderTime": reminderTime,
            "type": type
        }
        res = core.medicineGalleryUpdate(headers=header, json=json_data)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def medicineGet(self, title, recordDate, expect_code, expect_msg, core_token):
        """获取用户服药记录"""
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "authToken": core_token
        }
        json_data = {
            "recordDate":recordDate
        }
        res = core.medicineGet(headers=header, params=json_data)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def medicineUpdate(self, title, category, categoryName, categoryOrder, enable, medicineId, name, order,
                       recordDate, expect_code, expect_msg, core_token):
        """更新用户服药记录"""
        header = {
            "Content-Type": "application/json",
            "authToken": core_token
        }
        json_data = {
            "items": [
                {
                    "category": category,
                    "categoryName": categoryName,
                    "categoryOrder": categoryOrder,
                    "enable": enable,
                    "medicineId": medicineId,
                    "name": name,
                    "order": order
                }
            ],
            "recordDate": recordDate
        }
        res = core.medicineUpdate(headers=header, json=json_data)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def noteGet(self, title, recordDate, expect_code, expect_msg, core_token):
        """获取用户每日记录笔记"""
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "authToken": core_token
        }
        json_data = {
            "recordDate":recordDate
        }
        res = core.noteGet(headers=header, params=json_data)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def spermLogAdd(self, title, images, progressiveMotility, spermCount, time, totalMotility,
                    expect_code, expect_msg, core_token):
        """增加精子记录"""
        header = {
            "Content-Type": "application/json",
            "authToken": core_token
        }
        json_data = {
            "images": [images],
            "progressiveMotility":progressiveMotility,
            "spermCount":spermCount,
            "time":time,
            "totalMotility":totalMotility
        }
        res = core.spermLogAdd(headers=header, json=json_data)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message
        logger.info(res.json()["id"])
        sql = 'SELECT id FROM core.sperm_prep WHERE user_id = "26774415" AND time LIKE "2023-10-17%";'
        result = db.select_db(sql)
        # logger.info(result)
        assert res.json()["id"] == str(result[0]["id"])  #断言数据库


    def spermDataGet(self, title, recordDate, expect_code, expect_msg, core_token):
        """根据日期，获取精子记录"""
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "authToken": core_token
        }
        json_data = {
            "recordDate":recordDate
        }
        res = core.spermDataGet(headers=header, params=json_data)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message
        del_sql = 'DELETE FROM core.sperm_prep WHERE user_id = 26774415 AND time LIKE "2023-10-17%";'  # 清数据
        del_res = db.select_db(del_sql)

    def spermLogHistoryGet(self, title, page, size, expect_code, expect_msg, core_token):
        """获取用户精子历史数据列表"""
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "authToken": core_token
        }
        json_data = {
            "page":page,
            "size":size
        }
        res = core.spermLogHistoryGet(headers=header, params=json_data)
        logger.info(res.text)
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message

    def spermLogGet(self, title, id, expect_code, expect_msg, core_token):
        """根据主键id，获取用户精子准备记录"""
        header = {
            "Content-Type":"application/json",
            "apiVersion":"25",
            "appVersion":"1.15.0",
            "Accept":"*/*",
            "authToken":core_token
        }
        json_data = {
            "id":id
        }
        res = core.spermLogGet(headers=header, params=json_data)
        logger.info(res.text)
        logger.info("url===>> {}".format(res.url))
        logger.info("预期code===>> {}".format(expect_code))
        logger.info("实际code===>> {}".format(res.status_code))
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message