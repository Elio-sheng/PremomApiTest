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

    def ComparisonList(self, **kwargs):  # 获取周期比较报告列表
        return self.request("/core/cycle/report/get/comparison/list", method="GET", **kwargs)

    def ShareComparison(self, **kwargs):  # 分享用户周期比较报告
        return self.request("/core/cycle/report/share/comparison/link", method="POST", **kwargs)

    def CervicalAndMoodAndSymptom(self, **kwargs):  # 获取用户周期分析报告-CM and Positioning Detail/Mood and Symptom Detail
        return self.request("/core/cycle/report/get/analysis/cervicalAndMoodAndSymptom", method="GET", **kwargs)

    def AnalysisGuarantee(self, **kwargs):  # 获取用户周期分析报告-9-Cycle Guarantee
        return self.request("/core/cycle/report/get/analysis/guarantee", method="GET", **kwargs)

    def AnalysisOverview(self, **kwargs):  # 获取用户周期分析报告-Overview/LH Pattern
        return self.request("/core/cycle/report/get/analysis/overview", method="GET", **kwargs)

    def AnalysisOvulation(self, **kwargs):  # 获取用户周期分析报告-Ovulation Tracking
        return self.request("/core/cycle/report/get/analysis/ovulation", method="GET", **kwargs)

    def AnalysisPeakFertility(self, **kwargs):  # 获取用户周期分析报告-Peak Fertility
        return self.request("/core/cycle/report/get/analysis/peakFertility", method="GET", **kwargs)

    def AnalysisSummary(self, **kwargs):  # 获取用户周期分析报告-Cycle Summary
        return self.request("/core/cycle/report/get/analysis/summary", method="GET", **kwargs)

    def AnalysisPeakUser(self, **kwargs):  # 获取用户周期分析报告-用户档案数据
        return self.request("/core/cycle/report/get/analysis/user", method="GET", **kwargs)

    def GlanceIntercourseTiming(self, **kwargs):  # 获取用户Cycle at a Glance-Intercourse Timing
        return self.request("/core/cycle/report/get/glance/intercourseTiming", method="GET", **kwargs)

    def GlanceOvulation(self, **kwargs):  # 获取用户Cycle at a Glance-Predict/Confirm Ovulation
        return self.request("/core/cycle/report/get/glance/ovulation", method="GET", **kwargs)



