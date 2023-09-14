"""
-*- coding: utf-8 -*-
"""
import requests


def home():
    url = "http://api.test.premom.tech/misc/homepage/manager/App/viewModulesNew?pageName=TTCHomepage"
    header = {
        "appVersion":"1.35.0",
        "Content-Type":"application/x-www-form-urlencoded",
        "authToken":"uta2d28249b502000"
    }
    res = requests.get(url = url, headers = header)
    print(res.text)

home()
