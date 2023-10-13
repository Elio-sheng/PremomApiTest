"""
-*- coding: utf-8 -*-
"""
import allure
import pytest
from common.logger import logger
from operation.coreserevice import Report, Insemination
from api.user import UserService

Core_request = Report()
@allure.epic("项目名称：premom核心功能接口测试报告")
@allure.feature("core服务接口")
class TestReport():
    @allure.story("获取用户周期分析报告列表")
    def test_coreservice_AnalysisList(self, title,  except_result, expect_code, expect_msg, core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.AnalysisList( title, except_result, expect_code, expect_msg, core_token)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("获取用户周期分析报告状态")
    def test_coreservice_CycleStatus(self, title, cycleNumber, except_result, expect_code, expect_msg,core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.CycleStatus( title, cycleNumber, except_result, expect_code, expect_msg, core_token)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("分享用户周期分析报告列表")
    def test_coreservice_ShareAnalysis(self, title, cycleNumber,email,cycleEndNumber,id, except_result, expect_code, expect_msg,core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.ShareAnalysis(title, cycleNumber,email,cycleEndNumber,id, except_result, expect_code, expect_msg, core_token)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("获取用户周期比较报告列表")
    def test_coreservice_ComparisonList(self, title,  except_result, expect_code, expect_msg, core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.ComparisonList( title, except_result, expect_code, expect_msg, core_token)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("分享用户周期比较报告")
    def test_coreservice_ShareComparison(self, title, cycleNumber,email,cycleEndNumber,id, except_result, expect_code, expect_msg,core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.ShareAnalysis(title, cycleNumber,email,cycleEndNumber,id, except_result, expect_code, expect_msg, core_token)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")


#
# class TestInsemination():
#     def test_coreservice_InseminationAddOrUpdate(self, title, id, frozenSperm, noInsemination, noneOfTheAbove, triggerShot, type, expect_code, expect_msg, core_token, get_current_date):
#         logger.info("*************** 开始执行用例 ***************")
#         result = Insemination().inseminationAddOrUpdate(title, id, frozenSperm, noInsemination, noneOfTheAbove, triggerShot, type, expect_code, expect_msg, core_token, get_current_date)
#         logger.info(result)
#         logger.info("*************** 结束执行用例 ***************")
#
#     def test_coreservice_inseminationDataGet(self, title, recordDate, expect_code, expect_msg, core_token):
#         logger.info("*************** 开始执行用例 ***************")
#         result = Insemination().inseminationDataGet(title, recordDate, expect_code, expect_msg, core_token)
#         logger.info(result)
#         logger.info("*************** 结束执行用例 ***************")
#
#     def test_coreservice_dailyRecordGetSetting(self, title, expect_code, expect_msg, core_token):
#         logger.info("*************** 开始执行用例 ***************")
#         result = Insemination().dailyRecordGetSetting(title,  expect_code, expect_msg, core_token)
#         logger.info(result)
#         logger.info("*************** 结束执行用例 ***************")
#
#
#     def test_coreservice_inseminationGetTip(self, title, editCycle, editDate, expect_code, expect_msg, core_token):
#         logger.info("*************** 开始执行用例 ***************")
#         result = Insemination().inseminationGetTip(title, editCycle, editDate, expect_code, expect_msg, core_token)
#         logger.info(result)
#         logger.info("*************** 结束执行用例 ***************")
#
#
#
#
    def test_coreservice_inseminationGetTip(self, title, editCycle, editDate, expect_code, expect_msg, core_token):
        """获取提示文案"""
        logger.info("*************** 开始执行用例 ***************")
        result = Insemination().inseminationGetTip(title, editCycle, editDate, expect_code, expect_msg, core_token)
        logger.info(result)
        logger.info("*************** 结束执行用例 ***************")

    def test_coreservice_inseminationLogSexKeepOrChangeBtn(self, title, keepLogSex, expect_code, expect_msg, core_token):
        """保留或更换home页面LogSex按钮"""
        logger.info("*************** 开始执行用例 ***************")
        result = Insemination().inseminationLogSexKeepOrChangeBtn(title, keepLogSex, expect_code, expect_msg, core_token)
        logger.info(result)
        logger.info("*************** 结束执行用例 ***************")

    def test_coreservice_dailyRecordUpdateSetting(self, title, enable, order, settingType, expect_code, expect_msg, core_token):
        """更新用户每日记录设置"""
        logger.info("*************** 开始执行用例 ***************")
        result = Insemination().dailyRecordUpdateSetting(title, enable, order, settingType, expect_code, expect_msg, core_token)
        logger.info(result)
        logger.info("*************** 结束执行用例 ***************")

    def test_coreservice_dailyRecordMomentGet(self, title, expect_code, expect_msg, core_token, get_current_date):
        """获取用户Moment分享-每日记录数据"""
        logger.info("*************** 开始执行用例 ***************")
        result = Insemination().dailyRecordMomentGet(title, expect_code, expect_msg, core_token, get_current_date)
        logger.info(result)
        logger.info("*************** 结束执行用例 ***************")

    def test_coreservice_BBTPopupPageInfo(self, title, expect_code, expect_msg, core_token):
        """BBT操作视频弹窗信息"""
        logger.info("*************** 开始执行用例 ***************")
        result = Insemination().BBTPopupPageInfo(title, expect_code, expect_msg, core_token)
        logger.info(result)
        logger.info("*************** 结束执行用例 ***************")

    def test_coreservice_prePregnancyGet(self, title, expect_code, expect_msg, core_token):
        """根据用户获取孕前信息记录"""
        logger.info("*************** 开始执行用例 ***************")
        result = Insemination().prePregnancyGet(title, expect_code, expect_msg, core_token)
        logger.info(result)
        logger.info("*************** 结束执行用例 ***************")
