"""
-*- coding: utf-8 -*-
"""
import os
from datetime import datetime, date
from common.logger import logger

class DateTime(object):
    @staticmethod
    def get_current_date():
        """获取当前日期"""
        try:
            current_date = date.today()
        except Exception as e:
            raise e
        else:
            return str(current_date)

    @staticmethod
    def get_current_time():
        """获取当前时间"""
        try:
            time = datetime.now()
            current_time = time.strftime('%H:%M:%S')
        except Exception as e:
            raise e
        else:
            return current_time

    @staticmethod
    def get_current_time_to_datetime():
        """获取当前时间并转化成时间戳"""
        pass


# if __name__ == '__main__':
#     logger.info(DateTime.get_current_date())
#     logger.info(DateTime.get_current_time())
