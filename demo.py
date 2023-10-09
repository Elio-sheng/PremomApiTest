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
import datetime


def datetime_encoder(obj):
    if isinstance(obj, (date)):
        return obj.isoformat()

# 示例日期对象
my_date = date.today()

# 序列化为JSON字符串
json_str = json.dumps(my_date, default=datetime_encoder)
# print(json_str)

now=datetime.date.today()
# print(now)

from datetime import date, datetime

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


nowTime = json.dumps(now, cls=ComplexEncoder)
# print(nowTime)

import os
from datetime import datetime, date
class DateTime(object):
    @staticmethod
    def get_current_date():
        """获取当前日期"""
        try:
            current_date = date.today()
        except Exception as e:
            raise e
        else:
            return json.dumps(str(current_date))

    @staticmethod
    def get_current_time():
        """获取当前时间"""
        try:
            time = datetime.now()
            current_time = time.strftime('%H:%M:%S')
        except Exception as e:
            raise e
        else:
            return json.dumps(current_time)

# if __name__ == '__main__':
#     print(DateTime.get_current_date())
#     print(DateTime.get_current_time())

