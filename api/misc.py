# -*- coding: utf-8 -*-

from core.rest_client import RestClient


class MiscService(RestClient):

    def __init__(self, base_url=None, **kwargs):
        super().__init__(base_url=base_url, **kwargs)

    def appHomepage(self, **kwargs):  # 获取home页面信息
        return self.request("/misc/homepage/manager/App/viewModulesNew",
                            method="GET",
                            **kwargs)

    def getReminder(self, **kwargs):  # 获取Reminder的数据
        return self.request("/misc/reminder/get", method="GET", **kwargs)
