from core.rest_client import RestClient


class UserService(RestClient):
    def __init__(self, base_url, **kwargs):
        super().__init__(base_url, **kwargs)

    def webUserLogin(self, **kwargs):   #Email登录
        return self.request("/user/user/web/sign/in", method="POST", **kwargs)

    def thirdUserLogin(self, **kwargs):    #第三方登录
        return self.request("/user/web/sign/in/third", method="POST", **kwargs)

    def webRegister(self, **kwargs):     #注册
        return self.request("/user/user/sign/up", method="POST", **kwargs)

    def userDelete(self, **kwargs):   #删除账号
        return self.request("/user/user/cancellation/account/delete/reason", method="POST", **kwargs)

    def userMyProfile(self, **kwargs):     #获取用户档案信息（获取profile页面)
        return self.request("/user/profile/get", method="GET", **kwargs)

    def userGuarantee(self, **kwargs):    #加入包孕计划接口
        return self.request("/user/guarantee/subscribe", method="POST")
