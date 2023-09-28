"""
-*- coding: utf-8 -*-
"""
import requests
true= True

def member():
    url = "http://api.test.premom.tech/user/member/v2/page/info"
    header = {
        "apiversion": "43",
        "timezone": "Asia/Shanghai",
        "language": "0",
        "os": "iphone",
        "appversion": "1.36.0",
        "Content-Type": "application/json",
        "authToken":"uta3e220d72102000"
    }
    data = {
        "pageType": "MEMBERSHIP_LANDING_PAGE",
        "zoneIdStr": "Asia/Shanghai",
        "productInfos": [],
        "receipt": "",
        "platform": "GoogleStore"
    }
    res = requests.post(url = url, headers = header, json=data)
    print(res.json())

# member()



from datetime import datetime

current_date = datetime.now().date()
# print(current_date)

import json
from datetime import date

def datetime_encoder(obj):
    if isinstance(obj, (date)):
        return obj.isoformat()

# 示例日期对象
my_date = date.today()

# 序列化为JSON字符串
json_str = json.dumps(my_date, default=datetime_encoder)
print(json_str)
