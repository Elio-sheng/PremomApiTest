# -*- coding: utf-8 -*-
import pytest

from common.logger import logger
from operation.userservice import User, Member

userInstance = User()

class TestLogin():

    def test_userservice_login(self, title, anonymousId, bindAnonymous, email, password, phoneID, platform, timeZone, except_result, expect_code, expect_msg):
        # Print a message to indicate the start of the test case
        logger.info("*************** 开始执行用例 ***************")

        # Call the webUserLogin function with the provided parameters
        result = userInstance.webUserLogin(title, anonymousId, bindAnonymous, email, password, phoneID, platform, timeZone, except_result, expect_code,expect_msg)

        # Log the expected result, code, and message

        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    # def test_userservice_register(self, title, email, password, OSType, lastName, firstName, expect_result, expect_code, expect_msg):
    #     # Print a message to indicate the start of the test case
    #     logger.info("*************** 开始执行用例 ***************")
    #     # Call the webUserRegister function with the provided parameters
    #     result = userInstance.webRegister(title, email, password, OSType, lastName, firstName, expect_result, expect_code, expect_msg)
    #     # Log the expected result, code, and message
    #     logger.info(result)
    #     # Print a message to indicate the end of the test case
    #     logger.info("*************** 结束执行用例 ***************")

    # def test_userservice_myProfile(self, title, except_result, expect_code,expect_msg,userToken):
    #     # Print a message to indicate the start of the test case
    #     logger.info("*************** 开始执行用例 ***************")
    #     # Call the webUserDelete function with the provided parameters
    #     result = User().myProfile(title, except_result, expect_code,expect_msg,userToken)
    #     logger.info(result)
    #     # Print a message to indicate the end of the test case
    #     logger.info("*************** 结束执行用例 ***************")
    # @pytest.mark.skip
    # def test_userservice_delete(self, title, reasonType, appsflyerId, except_result, expect_code, expect_msg, userToken):
    #     # Print a message to indicate the start of the test case
    #     logger.info("*************** 开始执行用例 ***************")
    #     logger.info(userToken)
    #     # Call the webUserDelete function with the provided parameters
    #     result = User().userDelete(title, reasonType, appsflyerId, except_result, expect_code, expect_msg, userToken)
    #     logger.info(result)
    #     # Print a message to indicate the end of the test case
    #     logger.info("*************** 结束执行用例 ***************")

    def test_userservice_guarantee(self, title, addFreeTestsActivity, params, except_result, expect_code, expect_msg):
        # Print a message to indicate the start of the test case
        logger.info("*************** 开始执行用例 ***************")
        result = userInstance.userGuarantee(title, addFreeTestsActivity, params, except_result, expect_code, expect_msg)
        # Log the expected result, code, and message
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")




# class TestMember():
#     def test_userservice_ismember(self, title,except_result, expect_code, expect_msg,global_token):
#         # Print a message to indicate the start of the test case
#         logger.info("*************** 开始执行用例 ***************")
#         # Call the webUserLogin function with the provided parameters
#         result = Member().ismember(title, except_result, expect_code,expect_msg,global_token)
#
#         # Log the expected result, code, and message
#
#         logger.info(result)
#         # Print a message to indicate the end of the test case
#         logger.info("*************** 结束执行用例 ***************")