"""
-*- coding: utf-8 -*-
"""
import pytest
import os
from common.logger import logger
from common.mysql_operate import db
from common.read_data import yaml
from api.user import UserService
import json
# from common.get_time import DateTime
from datetime import datetime, date



# 获取当前文件所在的目录路径
current_directory = os.path.dirname(os.path.abspath(__file__))
# 获取上一级目录的路径
parent_directory = os.path.dirname(current_directory)
# 获取上上一级目录的路径
grandparent_directory = os.path.dirname(parent_directory)
# 拼接文件路径，跨平台支持
BASE_PATH = os.path.join(grandparent_directory, "data")
logger.info(BASE_PATH)


coreTestdata = None


def get_data(yaml_file_name):
    data_file_path = os.path.join(BASE_PATH, yaml_file_name)
    logger.info(data_file_path)
    try:
        with open(data_file_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
    except FileNotFoundError:
        pytest.skip(f"File not found: {data_file_path}")
    except Exception as ex:
        logger.info(yaml_file_name)
        logger.info(ex)
        pytest.skip(f"Error loading YAML file: {ex}")
    else:
        return yaml_data


def pytest_generate_tests(metafunc):
    """Parameterize the tests from a YAML file.

    The YAML file structure should be like this:
        TestXXX:                        # Class
          test_soco_xxx:                # Function
            parameters: paramA, paramB  # Parameter list
            values:
              - [valA1, valA2]          # Test cases
              - [valA2, valB2]
    """
    global coreTestdata
    if not coreTestdata:
        # Fetch testdata from YAML file
        coreTestdata = get_data("coreservice_test_data.yml")

    classname = metafunc.cls.__name__
    funcname = metafunc.function.__name__
    funcdata = coreTestdata.get(classname)[funcname]
    if funcdata:
        parameters = funcdata['parameters']
        # Convert argument lists to tuples
        values = [tuple(v) if isinstance(v, list)
                  else v for v in funcdata['values']]
        logger.info(f"Parameters: {parameters}")
        logger.info(f"Values: {values}")
        metafunc.parametrize(parameters, values)


@pytest.fixture(scope="module", autouse=True)
def core_token():
    json_data = {
        "anonymousId": "",
        "bindAnonymous": "true",
        "email": "t999@premomtest.com",
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
    logger.info(token)
    return token

@pytest.fixture(scope="class", autouse=True)
def get_current_date():
    """获取当前日期"""
    try:
        current_date = date.today()
    except Exception as e:
        raise e
    else:
        return str(current_date)

@pytest.fixture(scope="class", autouse=True)
def get_userId():
    sql = 'select user_id from ezhome.all_login WHERE email = \'t999@premomtest.com\';'
    sql_res = db.select_db(sql)
    uid = str(sql_res[0]['user_id'])

    return uid
