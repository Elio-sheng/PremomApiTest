"""
-*- coding: utf-8 -*-
"""
import pytest
from api.user import UserService
import os
from common.logger import logger
# from common.read_data import ReadExcel
import os
from common.read_data import yaml
from api.user import UserService

# 获取当前文件所在的目录路径
current_directory = os.path.dirname(os.path.abspath(__file__))
# 获取上一级目录的路径
parent_directory = os.path.dirname(current_directory)
# 获取上上一级目录的路径
grandparent_directory = os.path.dirname(parent_directory)
# 拼接文件路径，跨平台支持
BASE_PATH = os.path.join(grandparent_directory, "data")
logger.info(BASE_PATH)
ezTestdata = None


def get_data(yaml_file_name):
    data_file_path = os.path.join(BASE_PATH, yaml_file_name)
    # logger.info(data_file_path)
    try:
        with open(data_file_path, 'r', encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
            # logger.info(yaml_data)
    except FileNotFoundError:
        pytest.skip(f"File not found: {data_file_path}")
    except Exception as ex:
        # logger.info(yaml_file_name)
        # logger.info(ex)
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
    global ezTestdata
    if not ezTestdata:
        # Fetch testdata from YAML file
        ezTestdata = get_data("ezserver_test_data.yml")

    classname = metafunc.cls.__name__
    funcname = metafunc.function.__name__
    funcdata = ezTestdata.get(classname)[funcname]
    if funcdata:
        parameters = funcdata['parameters']
        # Convert argument lists to tuples
        values = [
            tuple(v) if isinstance(v, list) else v for v in funcdata['values']
        ]
        logger.info(f"Parameters: {parameters}")
        logger.info(f"Values: {values}")
        metafunc.parametrize(parameters, values)


@pytest.fixture(scope="session", autouse=True)
def ez_token():
    json_data = {
        "anonymousId": "",
        "bindAnonymous": "true",
        "email": "test776@premom.com",
        "password": "123456",
        "phoneID": "decbb1ef-e41c-4cbd-9265-902415f00504",
        "platform": "iPhone XR 13.3",
        "timeZone": "+0800"
    }
    header = {"Content-Type": "application/json"}
    userservice = UserService()
    res = userservice.webUserLogin(json=json_data, headers=header)
    token = res.headers.get("authToken")
    return token


# # 获取当前文件所在的目录路径
# current_directory = os.path.dirname(os.path.abspath(__file__))
# # 获取上一级目录的路径
# parent_directory = os.path.dirname(current_directory)
# # 获取上上一级目录的路径
# grandparent_directory = os.path.dirname(parent_directory)
# # 拼接文件路径，跨平台支持
# BASE_PATH = os.path.join(grandparent_directory, "data")
# logger.info(BASE_PATH)
#
# # 定义一个 pytest fixture 函数，用于加载 Excel 数据
#
# @pytest.fixture(scope="module", autouse=True)
# def excel_data():
#     # 指定 Excel 文件路径
#     excel_file_path = os.path.join(
#         BASE_PATH, "AutoPytestExecl.xlsx")  # 请替换为你的 Excel 文件路径
#
#     # logger.info(BASE_PATH)
#     # 创建 ReadExcel 类的实例
#     excel_reader = ReadExcel(excel_file_path)
#
#     # 读取 Excel 数据（示例中使用 "ceshi" 工作表）
#     sheet_name = "input_al"  # 请替换为你的工作表名字
#     data = excel_reader.read_excel(sheet_name)
#     # logger.info(data)
#     # 返回读取到的数据，供测试函数使用
#     yield data
