"""
-*- coding: utf-8 -*-
"""
from core.rest_client import RestClient


class EzserverService(RestClient):

    def __init__(self, base_url=None, **kwargs):
        super().__init__(base_url=base_url, **kwargs)

    def input_al(self, **kwargs):  # 算法
        return self.request("/ezserver/api/fam/input_al",
                            method="POST",
                            **kwargs)

    def addSignsRecords_json(self, **kwargs):  # 算法
        return self.request("/easerver/sync/addSignsRecords.json",
                            method="POST",
                            **kwargs)

    def replaceAlgorithmData(self, **kwargs):  # 算法
        return self.request("/ezserver/api/cycle/replaceAlgorithmData",
                            method="POST",
                            **kwargs)

    def window_policy(self, **kwargs):  # 算法
        return self.request("/ezserver/api/window/policy",
                            method="POST",
                            **kwargs)
