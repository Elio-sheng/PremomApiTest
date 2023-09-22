"""
-*- coding: utf-8 -*-
"""
import json
import os
from core.result_base import ResultBase
from api.misc import MiscService
from common.logger import logger

misc = MiscService()

class Misc:

    def homepage(self, title, pageName, except_result, expect_code, expect_msg, misc_token):
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "appversion": "1.36.0",
            "apiversion": "43",
            "timezone": "Asia/Shanghai",
            "language": "0",
            "os": "iphone",
            "authtoken": misc_token
        }
        data = {"pageName":pageName}
        res = misc.appHomepage(headers=header, params=data)
        # logger.info(res)
        # logger.info("预期code===>> {}".format(expect_code))
        # logger.info("实际code===>> {}".format(res.status_code))
        # logger.info("预期msg===>> {}".format(expect_msg))
        # logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message
