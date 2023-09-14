from core.rest_client import RestClient


class UserService(RestClient):
    def __init__(self, base_url, **kwargs):
        super().__init__(base_url, **kwargs)

    def webUserLogin(self, **kwargs):   #Email��¼
        return self.request("/user/user/web/sign/in", method="POST", **kwargs)

    def thirdUserLogin(self, **kwargs):    #��������¼
        return self.request("/user/web/sign/in/third", method="POST", **kwargs)

    def webRegister(self, **kwargs):     #ע��
        return self.request("/user/user/sign/up", method="POST", **kwargs)

    def userDelete(self, **kwargs):   #ɾ���˺�
        return self.request("/user/user/cancellation/account/delete/reason", method="POST", **kwargs)

    def userMyProfile(self, **kwargs):     #��ȡ�û�������Ϣ����ȡprofileҳ��)
        return self.request("/user/profile/get", method="GET", **kwargs)

    def userGuarantee(self, **kwargs):    #������мƻ��ӿ�
        return self.request("/user/guarantee/subscribe", method="POST")
