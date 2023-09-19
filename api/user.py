# -*- coding: utf-8 -*-

from core.rest_client import RestClient


class UserService(RestClient):
    def __init__(self, base_url=None, **kwargs):
        super().__init__(base_url=base_url)

    def webUserLogin(self, **kwargs):   
        return self.request("/user/user/web/sign/in", method="POST", **kwargs)

    def thirdUserLogin(self, **kwargs):    
        return self.request("/user/web/sign/in/third", method="POST", **kwargs)

    def webRegister(self, **kwargs):     
        return self.request("/user/user/sign/up", method="POST", **kwargs)

    def userDelete(self, **kwargs):  
        return self.request("/user/user/cancellation/account/delete/reason", method="POST", **kwargs)

    def userMyProfile(self, **kwargs):   
        return self.request("/user/profile/get", method="GET", **kwargs)

    def userGuarantee(self, **kwargs):    
        return self.request("/user/guarantee/subscribe", method="POST")
