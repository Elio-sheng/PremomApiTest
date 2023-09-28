"""
-*- coding: utf-8 -*-
"""
import pytest
import os
from common.logger import logger
from common.read_data import yaml
from api.user import UserService

# BASE_PATH = os.path.dirname(os.path.abspath(__file__)).split("PremomApiTest")[0]
BASE_PATH = os.path.abspath(__file__).split("PremomApiTest")[0] + "PremomApiTest" + "\\"


logger.info(BASE_PATH)

coreTestdata = None
print("####")
print(BASE_PATH)


def get_data(yaml_file_name):
    data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
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
        values = [tuple(v) if isinstance(v, list) else v for v in funcdata['values']]
        logger.info(f"Parameters: {parameters}")
        logger.info(f"Values: {values}")
        metafunc.parametrize(parameters, values)


@pytest.fixture(scope="class", autouse=True)
def core_token():
    json_data = {
        "anonymousId": "",
        "bindAnonymous": "true",
        "email": "t02@premom.com",
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