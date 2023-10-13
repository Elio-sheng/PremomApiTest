"""
-*- coding: utf-8 -*-
"""
from core.result_base import ResultBase
from api.ezserver import EzserverService
from common.logger import logger
from common.read_data import ReadExcel

class Ezserver:

    def InputAl(self,title, BBT, menstruationRecord, expect_code, expect_msg, ez_token):
        header = {
            "Content-Type": "application/json",
            "authToken": ez_token
        }
        json_data = {
             "daysInput": [{
              "ovulationResultByUser": 0,
              "ovulationResultByLH": 0,
              "menstruationRecord": 10,
              "impactTempFlag": 0,
              "BBT": 0,
              "cervicalMunusRecord": 0,
              "timestamp": 1690862400,
              "dayOfCycle": 0
             }, {
              "impactTempFlag": 0,
              "ovulationResultByUser": 0,
              "BBT": 0,
              "timestamp": 1690948800,
              "menstruationRecord": 10,
              "dayOfCycle": 0,
              "cervicalMunusRecord": 0,
              "ovulationResultByLH": 0
             }, {
              "BBT": 0,
              "timestamp": 1691035200,
              "ovulationResultByLH": 0,
              "impactTempFlag": 0,
              "dayOfCycle": 0,
              "ovulationResultByUser": 0,
              "menstruationRecord": 10,
              "cervicalMunusRecord": 0
             }, {
              "ovulationResultByUser": 0,
              "ovulationResultByLH": 0,
              "dayOfCycle": 0,
              "impactTempFlag": 0,
              "menstruationRecord": 10,
              "cervicalMunusRecord": 0,
              "timestamp": 1691121600,
              "BBT": 0
             }, {
              "menstruationRecord": 10,
              "ovulationResultByUser": 0,
              "impactTempFlag": 0,
              "cervicalMunusRecord": 0,
              "BBT": 0,
              "dayOfCycle": 0,
              "timestamp": 1691208000,
              "ovulationResultByLH": 0
             }, {
              "dayOfCycle": 0,
              "menstruationRecord": 10,
              "cervicalMunusRecord": 0,
              "impactTempFlag": 0,
              "ovulationResultByUser": 0,
              "BBT": 0,
              "timestamp": 1693540800,
              "ovulationResultByLH": 0
             }, {
              "BBT": 0,
              "menstruationRecord": 10,
              "impactTempFlag": 0,
              "dayOfCycle": 0,
              "cervicalMunusRecord": 0,
              "ovulationResultByUser": 0,
              "timestamp": 1693627200,
              "ovulationResultByLH": 0
             }, {
              "ovulationResultByUser": 0,
              "BBT": 0,
              "ovulationResultByLH": 0,
              "impactTempFlag": 0,
              "menstruationRecord": 10,
              "timestamp": 1693713600,
              "dayOfCycle": 0,
              "cervicalMunusRecord": 0
             }, {
              "cervicalMunusRecord": 0,
              "timestamp": 1693800000,
              "ovulationResultByLH": 0,
              "impactTempFlag": 0,
              "ovulationResultByUser": 0,
              "dayOfCycle": 0,
              "BBT": 0,
              "menstruationRecord": 10
             }, {
              "impactTempFlag": 0,
              "ovulationResultByUser": 0,
              "timestamp": 1693886400,
              "dayOfCycle": 0,
              "menstruationRecord": 10,
              "BBT": 0,
              "ovulationResultByLH": 0,
              "cervicalMunusRecord": 0
             }, {
              "cervicalMunusRecord": 0,
              "menstruationRecord": menstruationRecord,
              "timestamp": 1696651200,
              "ovulationResultByLH": 0,
              "ovulationResultByUser": 0,
              "BBT": BBT,
              "dayOfCycle": 0,
              "impactTempFlag": 0
             }],
             "debug": 0,
             "userData": {
              "userAverageLuteumLength": 14,
              "userCycleLengthError": 4,
              "userCycleRegularity": 1,
              "userAverageMenstruationLength": 5,
              "userAverageCycleLength": 28
             },
                "param": {
                "version": 1
                 }
            }
        res = EzserverService().input_al(headers=header,json=json_data)
        logger.info(res)
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message


    def addSignsRecords_json(self, title, notes, expect_code, expect_msg, ez_token):
        header = {
            "Content-Type": "application/json",
            "authToken": ez_token
        }
        json_data = {
            "records": [{
                "editDate": "2023-10-12 18:23:16",
                "homePageChartMessage": "",
                "LHSurge": 0,
                "pregnancyWeightUnit": 0,
                "dailyLogs": {
                    "sleepTime": 0,
                    "others": 0,
                    "aidedInsemination": 0,
                    "cervicalMucus": 4,
                    "exercise": 0,
                    "cervicalTexture": 2,
                    "moods": 0,
                    "cervicalAmount": 0,
                    "ferning": 0,
                    "miscarriageBloodColors": 0,
                    "miscarriageTexture": 0,
                    "confirmBbtSpike": 0,
                    "exerciseTime": 0,
                    "notes": notes,
                    "symptoms": 4096,
                    "periodTexture": 0,
                    "cervicalOpenness": 2,
                    "dietarySupplement": 3,
                    "periodBloodColors": 0,
                    "hadSex": 49,
                    "cervicalPosition": 2,
                    "symptomLv": ",,,,,,,,,,,,Moderate,,,,,,,,,,,,"
                },
                "pregnancyWeight": "0.0",
                "homePagePaperResult": "Low",
                "papers": [],
                "inWhichPeriod": 999,
                "homePagePregancySuccessValue": 0,
                "confirmBbtSpike": 0,
                "temperatures": [],
                "dayOfCycle": 0,
                "confirmOvulation": 1,
                "homePageChartTitle": "",
                "periodProperty": 128,
                "recordID": "7ABEC963-2C63-4F16-B612-FBF4241F0FE8",
                "bbtSpike": 0,
                "recordDate": "2023-10-12 12:00:00",
                "pdgPositive": 0,
                "homePageOvulation": -1
            }],
            "authToken": ez_token
        }
        res = EzserverService().addSignsRecords_json(headers=header, json=json_data)
        logger.info(res)
        logger.info("预期msg===>> {}".format(expect_msg))
        logger.info("实际msg===>> {}".format(res.text))
        ResultBase(res, expect_code, expect_msg, expect_msg, res)  # 断言code和message