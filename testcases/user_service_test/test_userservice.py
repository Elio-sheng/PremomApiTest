from common.logger import logger
from operation.userservice import User
import pytest


class TestLogin():
    @pytest.mark.skip
    def test_userservice_login(self, title, anonymousId, bindAnonymous, email, password, phoneID, platform, timeZone, expect_result, expect_code, expect_msg):
        # Print a message to indicate the start of the test case
        logger.info("*************** 开始执行用例 ***************")
        # Call the webUserLogin function with the provided parameters
        result = User().webUserLogin(title, anonymousId, bindAnonymous, email, password, phoneID, platform, timeZone, expect_result, expect_code,expect_msg)

        # Log the expected result, code, and message

        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")


    @pytest.mark.run(order=1)
    def test_userservice_register(self, title, email, password, OSType, lastName, firstName, expect_result, expect_code, expect_msg):
        # Print a message to indicate the start of the test case
        logger.info("*************** 开始执行用例 ***************")
        # Call the webUserRegister function with the provided parameters
        result = User().webRegister(title, email, password, OSType, lastName, firstName, expect_result, expect_code, expect_msg)
        # Log the expected result, code, and message
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

    @pytest.mark.run(order=3)
    def test_userservice_delete(self, title, reasonType, appsflyerId, expect_result, expect_code, expect_msg):
        # Print a message to indicate the start of the test case
        logger.info("*************** 开始执行用例 ***************")
        # Call the webUserDelete function with the provided parameters
        result = User().userDelete(title, reasonType, appsflyerId, expect_result, expect_code, expect_msg)
        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

