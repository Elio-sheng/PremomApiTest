"""
-*- coding: utf-8 -*-
"""
from core.rest_client import RestClient

class EzserverService(RestClient):
    def __init__(self, base_url=None, **kwargs):
        super().__init__(base_url=base_url, **kwargs)

    def input_al(self, **kwargs):   #记录BBT
        return self.request("/ezserver/api/fam/input_al", method="POST", **kwargs)