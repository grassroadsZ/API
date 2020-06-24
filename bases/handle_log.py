# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 17:45
# @Author  : grassroadsZ
# @File    : settings.py

"""日志记录模块"""

import time
from loguru import logger
import os

from settings import RESULTS_DIR

LOG_PATH = os.path.join(RESULTS_DIR, 'log')
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
T = time.strftime("%Y_%m_%d")


class Logging(object):
    __instance = None
    logger.add(os.path.join(LOG_PATH, f"interface_log_{T}.txt"), rotation="500MB", encoding="utf-8", enqueue=True,
               retention="10 days")

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Logging, cls).__new__(cls, *args, **kwargs)

        return cls.__instance

    def info(self, msg):
        return logger.info(msg)

    def debug(self, msg):
        return logger.debug(msg)

    def warning(self, msg):
        return logger.warning(msg)

    def error(self, msg):
        return logger.error(msg)


log = Logging()
if __name__ == '__main__':
    log.info("中文test")
    log.debug("中文test")
    log.warning("中文test")
    log.error("中文test")

    # 格式化字符串
    logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')
    n1 = "cool"
    n2 = [1, 2, 3]
    logger.info(f'If you are using Python {n1}, prefer {n2} of course!')
