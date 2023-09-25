"""
-*- coding: utf-8 -*-
"""
import pytest
from common.logger import logger
from operation.coreserevice import Report
from api.user import UserService

Core_request = Report()
class TestReport():
    def test_coreservice_AnalysisList(self, title,  except_result, expect_code, expect_msg,core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.AnalysisList( title, except_result, expect_code, expect_msg, core_token)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")
    def test_coreservice_CycleStatus(self, title, cycleNumber, except_result, expect_code, expect_msg,core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.CycleStatus( title, cycleNumber, except_result, expect_code, expect_msg, core_token)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")
    def test_coreservice_ShareAnalysis(self, title, cycleNumber,email,cycleEndNumber,id, except_result, expect_code, expect_msg,core_token):
        logger.info("*************** 开始执行用例 ***************")
        result = Core_request.ShareAnalysis(title, cycleNumber,email,cycleEndNumber,id, except_result, expect_code, expect_msg, core_token)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")