# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 17:45
# @Author  : grassroadsZ
# @File    : settings.py

import os

# 项目根路径
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# 一级目录
BASES_DIR = os.path.join(PROJECT_DIR, "bases")
BUSINESS_DIR = os.path.join(PROJECT_DIR, "business")
DATA_DIR = os.path.join(PROJECT_DIR, "data")
RESULTS_DIR = os.path.join(PROJECT_DIR, "results")
CASE_DIR = os.path.join(PROJECT_DIR, "test_cases")

if __name__ == '__main__':
    print(f"项目根路径为:{PROJECT_DIR}")
    print(f"基础依赖为:{BASES_DIR}")
    print(f"业务目录为:{BUSINESS_DIR}")
    print(f"数据目录为:{DATA_DIR}")
    print(f"结果目录为:{RESULTS_DIR}")
    print(f"用例目录为:{CASE_DIR}")
