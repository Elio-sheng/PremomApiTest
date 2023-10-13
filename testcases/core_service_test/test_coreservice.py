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
    @allure.title("获取用户周期分析报告状态")
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


    @allure.story("获取用户周期分析报告-CM and Positioning Detail/Mood and Symptom Detail")
    @allure.title("成功获取用户周期分析报告-CM and Positioning Detail/Mood and Symptom Detail")
    def test_coreservice_CervicalAndMoodAndSymptom(self, title, expect_code, expect_msg,get_userId):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.CervicalAndMoodAndSymptom(title, expect_code, expect_msg, get_userId)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("获取用户周期分析报告-9-Cycle Guarantee")
    @allure.title("成功获取用户分析报告-9-Cycle Guarantee")
    def test_coreservice_AnalysisGuarantee(self, title, expect_code, expect_msg,get_userId):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.AnalysisGuarantee(title, expect_code, expect_msg, get_userId)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("获取用户周期分析报告-Overview/LH Pattern")
    @allure.title("成功获取用户分析报告-Overview/LH Pattern")
    def test_coreservice_AnalysisOverview(self, title, expect_code, expect_msg,get_userId):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.AnalysisOverview(title, expect_code, expect_msg, get_userId)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("获取用户周期分析报告-Ovulation Tracking")
    @allure.story("成功获取用户周期分析报告-Ovulation Tracking")
    def test_coreservice_AnalysisOvulation(self, title, expect_code, expect_msg,get_userId):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.AnalysisOvulation(title, expect_code, expect_msg, get_userId)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("获取用户周期分析报告-Peak Fertility")
    def test_coreservice_AnalysisPeakFertility(self, title, expect_code, expect_msg,get_userId):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.AnalysisPeakFertility(title, expect_code, expect_msg, get_userId)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("获取用户周期分析报告-Cycle Summary")
    def test_coreservice_AnalysisSummary(self, title, expect_code, expect_msg,get_userId):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.AnalysisSummary(title, expect_code, expect_msg, get_userId)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("获取用户周期分析报告-用户档案数据")
    def test_coreservice_AnalysisPeakUser(self, title, expect_code, expect_msg,get_userId):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.AnalysisPeakUser(title, expect_code, expect_msg, get_userId)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("获取用户Cycle at a Glance-Intercourse Timing")
    def test_coreservice_GlanceIntercourseTiming(self, title, expect_code, expect_msg,core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.GlanceIntercourseTiming(title, expect_code, expect_msg, core_token)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("获取用户Cycle at a Glance-Predict/Confirm Ovulation")
    def test_coreservice_GlanceOvulation(self, title, expect_code, expect_msg, core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.GlanceOvulation(title, expect_code, expect_msg, core_token)
        logger.info(result)
        logger.info("*************** 结束执行用例 ***************")

class TestInsemination():
    def test_coreservice_InseminationAddOrUpdate(self, title, id, frozenSperm, noInsemination, noneOfTheAbove, triggerShot, type, expect_code, expect_msg, core_token, get_current_date):
        logger.info("*************** 开始执行用例 ***************")
        result = Insemination().inseminationAddOrUpdate(title, id, frozenSperm, noInsemination, noneOfTheAbove, triggerShot, type, expect_code, expect_msg, core_token, get_current_date)
        logger.info(result)
        logger.info("*************** 结束执行用例 ***************")

    def test_coreservice_inseminationDataGet(self, title, recordDate, expect_code, expect_msg, core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Insemination().inseminationDataGet(title, recordDate, expect_code, expect_msg, core_token)
        logger.info(result)
        logger.info("*************** 结束执行用例 ***************")

    def test_coreservice_dailyRecordGetSetting(self, title, expect_code, expect_msg, core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Insemination().dailyRecordGetSetting(title,  expect_code, expect_msg, core_token)
        logger.info(result)
        logger.info("*************** 结束执行用例 ***************")


    def test_coreservice_inseminationGetTip(self, title, editCycle, editDate, expect_code, expect_msg, core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Insemination().inseminationGetTip(title, editCycle, editDate, expect_code, expect_msg, core_token)
        logger.info(result)
        logger.info("*************** 结束执行用例 ***************")





