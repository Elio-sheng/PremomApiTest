"""
-*- coding: utf-8 -*-
"""
import requests


def home():
    url = "http://api.test.premom.tech/misc/homepage/manager/App/viewModulesNew?pageName=TTCHomepage"
    header = {
        "appVersion":"1.35.0",
        "Content-Type":"application/x-www-form-urlencoded",
        "authToken":"uta38c7f1ef902000"
    }
    res = requests.get(url = url, headers = header)
    print(res.text)

home()
