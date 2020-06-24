# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 10:28
# @Author  : grassroadsZ
# @File    : BusinessBase.py
import json

from urllib3.exceptions import ResponseError

from bases.handle_requests import HandleRequest


class BusinessBase(object):
    do_request = HandleRequest()

    def handle_response(self, response):
        if response.status_code == 200:
            try:
                data = json.loads(response.content)
            except json.decoder.JSONDecodeError:
                raise TypeError(f"转换失败, {response} 不是json 对象")
            return data
        else:
            raise ResponseError(f"response 的响应值错误, 响应码为{response.status_code},响应信息为{response.content}")
