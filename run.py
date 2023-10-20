# -*- coding: utf-8 -*-
import os

import pytest


if __name__ == "__main__":
    pytest.main()
    # os.system("allure generate ./temps -o ./report --clean")#打印报告
    # allure generate命令，固定的
    # ./ temp临时的json格式报告的路径
    # -o输出output
    # ./ report生成的allure报告路径
    # --clean清空report文件夹下原来的报告