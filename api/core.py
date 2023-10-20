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

    def inseminationLogSexKeepOrChangeBtn(self, **kwargs):  # 保留或更换home页面LogSex按钮
        return self.request("/core/insemination/cycle/logSex/button/keepOrChange", method="POST", **kwargs)

    def dailyRecordUpdateSetting(self, **kwargs):   #更新用户每日记录设置
        return self.request("/core/dailyRecord/update/setting", method="POST", **kwargs)

    def dailyRecordMomentGet(self, **kwargs):   #获取用户Moment分享-每日记录数据
        return self.request("/core/dailyRecord/moment/get", method="GET", **kwargs)

    def BBTPopupPageInfo(self, **kwargs):  # BBT操作视频弹窗信息
        return self.request("/core/bbt/popup/page/info", method="GET", **kwargs)

    def getOneLastBBT(self, **kwargs):  # 查询最后一个非预测周期的最后一条录入BBT数据
        return self.request("/core/bbt/internal/getOneLastBBT", method="GET", **kwargs)

    def hasBBTRecordInCycle(self, **kwargs):  # 查询周期时间范围内是否有基础体温记录
        return self.request("/core/bbt/internal/hasBBTRecordInCycle", method="GET", **kwargs)

    def prePregnancyGet(self, **kwargs):  # 根据用户获取孕前信息记录
        return self.request("/core/pre/pregnancy/get", method="GET", **kwargs)

    def prePregnancySave(self, **kwargs):  # 保存孕前信息记录
        return self.request("/core/pre/pregnancy/save", method="POST", **kwargs)

    def mooeGet(self, **kwargs):  # 获取用户心情记录
        return self.request("/core/mood/get", method="GET", **kwargs)

    def medicineGalleryGet(self, **kwargs):  # 获取用户药品记录
        return self.request("/core/medicine/gallery/get", method="GET", **kwargs)

    def medicineGalleryUpdate(self, **kwargs):  # 更新用户药品记录
        return self.request("/core/medicine/gallery/update", method="POST", **kwargs)

    def medicineGet(self, **kwargs):  # 获取用户服药记录
        return self.request("/core/medicine/get", method="GET", **kwargs)

    def medicineUpdate(self, **kwargs):  # 更新用户服药记录
        return self.request("/core/medicine/update", method="POST", **kwargs)

    def noteGet(self, **kwargs):  # 获取用户每日记录笔记
        return self.request("/core/note/get", method="GET", **kwargs)

    def symptomGet(self, **kwargs):  # 获取用户症状记录
        return self.request("/core/symptom/get", method="GET", **kwargs)

    def spermDataGet(self, **kwargs):  # 根据日期，获取精子记录
        return self.request("/core/sperm/prep/date/data/get", method="GET", **kwargs)

    def spermLogAdd(self, **kwargs):  # 增加精子记录
        return self.request("/core/sperm/prep/log/add", method="POST", **kwargs)

    def spermLogDelete(self, **kwargs):  # 删除精子记录
        return self.request("/core/sperm/prep/log/delete", method="POST", **kwargs)

    def spermLogGet(self, **kwargs):  # 获取用户精子准备记录，根据主键id
        return self.request("/core/sperm/prep/log/get/{id}", method="GET", **kwargs)

    def spermLogHistoryGet(self, **kwargs):  # 获取用户精子历史数据列表
        return self.request("/core/sperm/prep/log/history/get", method="GET", **kwargs)

    def spermLogUpdate(self, **kwargs):  # 保存精子编辑记录
        return self.request("/core/sperm/prep/log/update", method="POST", **kwargs)

    def semenAnalysisDelete(self, **kwargs):  # 通过ID删除精液记录详情
        return self.request("/core/semenAnalysis/delete", method="GET", **kwargs)

    def semenAnalysisGetDetailByDate(self, **kwargs):  # 通过日期获取用户精液记录详情，格式(yyyy-MM-dd)
        return self.request("/core/semenAnalysis/getDetailByDate", method="GET", **kwargs)

    def semenAnalysisGetDetailById(self, **kwargs):  # 通过ID获取用户精液记录详情
        return self.request("/core/semenAnalysis/getDetailById", method="GET", **kwargs)

    def semenAnalysisQueryPage(self, **kwargs):  # 分页查询精液记录列表
        return self.request("/core/semenAnalysis/queryPage", method="GET", **kwargs)

    def semenAnalysisUpdate(self, **kwargs):  # 新增/更新Semen Analysis信息,如果要删除fallopianTube和results，把对应的值设置为空即可
        return self.request("/core/semenAnalysis/update", method="POST", **kwargs)

    def bloodDataGet(self, **kwargs):  # 根据日期，获取血液记录
        return self.request("/core/blood/date/data/get", method="GET", **kwargs)

    def bloodLogAdd(self, **kwargs):  # 增加血液记录
        return self.request("/core/blood/test/log/add", method="POST", **kwargs)

    def bloodLogDelete(self, **kwargs):  # 删除血液记录
        return self.request("/core/blood/test/log/delete", method="POST", **kwargs)

    def bloodLogGet(self, **kwargs):  # 获取用户血液测试记录，根据主键id
        return self.request("/core/blood/test/log/get/{id}", method="GET", **kwargs)

    def bloodLogHistoryGet(self, **kwargs):  # 获取用户血液历史数据列表
        return self.request("/core/blood/test/log/history/get", method="GET", **kwargs)

    def bloodLogUpdate(self, **kwargs):  # 保存血液编辑记录
        return self.request("/core/blood/test/log/update", method="POST", **kwargs)

    def stripCheckinDismiss(self, **kwargs):  # 忽略用户试纸打卡
        return self.request("/core/strip/checkin/dismiss", method="POST", **kwargs)

    def stripCheckinGet(self, **kwargs):  # 查询用户试纸打卡信息
        return self.request("/core/strip/checkin/get", method="GET", **kwargs)

    def stripGet(self, **kwargs):  # 用户试纸数据
        return self.request("/core/strip/get", method="GET", **kwargs)

    def stripPostGet(self, **kwargs):  # 查询用户指定周期在社区发帖的试纸文案信息
        return self.request("/core/strip/post/get", method="GET", **kwargs)

    def stripUsedLogoTestStrip(self, **kwargs):  # 查询周期范围内是否使用过品牌试纸
        return self.request("/core/strip/usedLogoTestStrip", method="GET", **kwargs)

    def exerciseGet(self, **kwargs):  # 获取用户锻炼记录
        return self.request("/core/exercise/get", method="GET", **kwargs)

    def iuiTypeDataGet(self, **kwargs):  # 获取iui录入的各个类型的数据
        return self.request("/core/iui/type/data/get", method="GET", **kwargs)

    def iuiInseminationMedicationInf(self, **kwargs):  # 通过药物主键id获取受精药物记录信息
        return self.request("/core/insemination/medication/inf/{id}", method="GET", **kwargs)

    def iuiInseminationMedicationListGet(self, **kwargs):  # 用户获取受精药物记录列表
        return self.request("/core/insemination/medication/list/get", method="GET", **kwargs)

    def iuiInseminationMedicationLogAdd(self, **kwargs):  # 增加或更新受精药物记录
        return self.request("/core/insemination/medication/log/add", method="POST", **kwargs)

    def iuiGetSimpleData(self, **kwargs):  # 获取用户周期简单数据,用于insemination cycle功能判断
        return self.request("/core/cycle/iui/get/simple/data", method="GET", **kwargs)

    def iuiUltrasoundDelete(self, **kwargs):  # 删除超声波记录，根据主键id
        return self.request("/core/ultrasound/delete/{id}", method="POST", **kwargs)

    def iuiUltrasoundGet(self, **kwargs):  # 获取用户超声波记录，根据日期
        return self.request("/core/ultrasound/get", method="GET", **kwargs)

    def iuiUltrasoundGetById(self, **kwargs):  # 获取用户B超记录，根据主键id
        return self.request("/core/ultrasound/get/{id}", method="GET", **kwargs)

    def iuiUltrasoundHistoryGet(self, **kwargs):  # 获取用户B超历史数据列表
        return self.request("/core/ultrasound/history/get", method="GET", **kwargs)

    def iuiUltrasoundLogUpdate(self, **kwargs):  # 编辑超声波记录
        return self.request("/core/ultrasound/log/update", method="POST", **kwargs)

    def iuiUltrasoundSave(self, **kwargs):  # 增加或更新超声波数据
        return self.request("/core/ultrasound/save", method="POST", **kwargs)

    def getIuiHistoryBtn(self, **kwargs):  # 判断用户是否有IUI History按钮
        return self.request("/core/iui/internal/getIuiHistoryBtn", method="GET", **kwargs)

    def getLabResultsBtn(self, **kwargs):  # 判断用户是否有Lab Results按钮
        return self.request("/core/iui/internal/getLabResultsBtn", method="GET", **kwargs)
