"""
-*- coding: utf-8 -*-
"""
import pytest
from common.logger import logger
from operation.miscserevice import Misc
from api.user import UserService

misc_request = Misc()


class TestMisc():
    def test_miscservice_homepage(self, title, pageName, except_result, expect_code, expect_msg, misc_token):
        logger.info("*************** 开始执行用例 ***************")
        result = misc_request.homepage(
            title, pageName, except_result, expect_code, expect_msg, misc_token)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")
