# -*- coding: utf-8 -*-


from core.rest_client import RestClient

class CoreService(RestClient):
    def __init__(self, base_url=None, **kwargs):
        super().__init__(base_url=base_url, **kwargs)


    def AnalysisList(self, **kwargs):   #获取用户周期分析报告列表
        return self.request("/core/cycle/report/get/analysis/list", method="GET", **kwargs)

    def CycleStatus(self, **kwargs):   #获取用户周期状态
        return self.request("/core/cycle/report/get/analysis/getCycleStatus", method="GET", **kwargs)

    def ShareAnalysis(self, **kwargs):   #分享用户周期分析报告
        return self.request("/core/cycle/report/share/analysis/link", method="POST", **kwargs)

    def InseminationAdd(self, **kwargs):   #增加或更新受精记录
        return self.request("/core/insemination/log/addOrUpdate", method="POST", **kwargs)

    def inseminationDataGet(self, **kwargs):   #根据日期，获取受经记录
        return self.request("/core/insemination/log/date/data/get", method="GET", **kwargs)

    def dailyRecordGetSetting(self, **kwargs):   #用户每日记录设置
        return self.request("/core/dailyRecord/get/setting", method="GET", **kwargs)

    def inseminationGetTip(self, **kwargs):   #获取提示文案
        return self.request("/core/insemination/cycle/get/Tip", method="GET", **kwargs)
