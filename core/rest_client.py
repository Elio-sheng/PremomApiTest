# -*- coding: utf-8 -*-

import requests
import json as complexjson
from common.logger import logger
import os
from configparser import ConfigParser

# Get the base path of the current file
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


# Define a class for making REST API requests
class RestClient:
    # 类属性来存储基础 API 地址，默认为 None
    base_url = None

    @classmethod
    def get_base_url(cls):
        # 如果 base_url 为空，则从配置文件中读取
        if cls.base_url is None:
            data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
            config = ConfigParser()
            config.read(data_file_path)
            cls.base_url = config.get('host', 'api_root_url')
        return cls.base_url
    
    def __init__(self, **kwargs):
        # Initialize the RestClient object with the API root URL
        # Create a session object to handle HTTP requests
        self.session = requests.session()
        self.base_url = self.get_base_url()

    def get(self, url, **kwargs):
        # Send a GET request to the specified URL
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        # Send a POST request to the specified URL
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        # Send a PUT request to the specified URL
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        # Send a DELETE request to the specified URL
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        # Send a PATCH request to the specified URL
        return self.request(url, "PATCH", data, **kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        # Log the base URL
        logger.info(self.base_url)

        # Construct the complete URL by appending the URL to the API root URL
        url = self.base_url + url

        # Extract the headers, params, files, and cookies from the kwargs
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("files")
        cookies = dict(**kwargs).get("cookies")

        # Log the details of the request
        self.request_log(url, method, data, json, params, headers, files, cookies)

        if method == "GET":
            # Send a GET request using the session object
            return self.session.get(url, **kwargs)
        if method == "POST":
            # Send a POST request using the requests module
            return requests.post(url, data, json, **kwargs)
        if method == "PUT":
            if json:
                # Convert the JSON object to a string and use it as the data parameter
                data = complexjson.dumps(json)
            # Send a PUT request using the session object
            return self.session.put(url, data, **kwargs)
        if method == "DELETE":
            # Send a DELETE request using the session object
            return self.session.delete(url, **kwargs)
        if method == "PATCH":
            if json:
                # Convert the JSON object to a string and use it as the data parameter
                data = complexjson.dumps(json)
            # Send a PATCH request using the session object
            return self.session.patch(url, data, **kwargs)

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        # Log the API request URL
        logger.info("接口请求地址 ==>> {}".format(url))

        # Log the API request method
        logger.info("接口请求方式 ==>> {}".format(method))

        # Log the API request headers
        logger.info("接口请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))

        # Log the API request params
        logger.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))

        # Log the API request data
        logger.info("接口请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))

        # Log the API request JSON payload
        logger.info("接口请求体 json 参数 ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))

        # Log the API request files (attachments)
        logger.info("接口上传附件 files 参数 ==>> {}".format(files))

        # Log the API request cookies
        logger.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))
