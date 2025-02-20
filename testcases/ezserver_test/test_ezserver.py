"""
-*- coding: utf-8 -*-
"""
import pytest
from common.logger import logger
from operation.ezserver import Ezserver


class TestEzserver:
    # @pytest.mark.parametrize("url, data", excel_data)
    def test_ezserver_input_al(self, title, BBT, menstruationRecord,
                               expect_code, expect_msg, ez_token):
        logger.info("*************** 开始执行用例 ***************")
        res = Ezserver().InputAl(title, BBT, menstruationRecord, expect_code,
                                 expect_msg, ez_token)
        logger.info(res)
        logger.info("*************** 结束执行用例 ***************")

    def test_ezserver_addSignsRecords_json(self, title, notes, expect_code,
                                           expect_msg, ez_token):
        logger.info("*************** 开始执行用例 ***************")
        res = Ezserver().addSignsRecords_json(title, notes, expect_code,
                                              expect_msg, ez_token)
        logger.info(res)
        logger.info("*************** 结束执行用例 ***************")
