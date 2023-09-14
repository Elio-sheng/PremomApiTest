from core.rest_client import RestClient

class MiscService(RestClient):
    def __init__(self, base_url, **kwargs):
        super().__init__(base_url, **kwargs)

    def appHomepage(self, **kwargs):   #获取home页面信息
        return self.request("misc/homepage/manager/App/viewModulesNew", method="GET", **kwargs)