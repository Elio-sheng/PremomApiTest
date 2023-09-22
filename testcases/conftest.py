# -*- coding: utf-8 -*-

import pytest
from api.user import UserService

@pytest.fixture(scope="session", autouse=True)
def global_token():
    json_data = {
      "anonymousId": "",
      "bindAnonymous": "true",
      "email": "test510@premom.com",
      "password": "123456",
      "phoneID": "decbb1ef-e41c-4cbd-9265-902415f00504",
      "platform": "iPhone XR 13.3",
      "timeZone": "+0800"
    }
    header = {
        "Content-Type": "application/json"
    }
    userservice = UserService()
    res = userservice.webUserLogin(json=json_data, headers=header)
    token = res.headers.get("authToken")
    return token