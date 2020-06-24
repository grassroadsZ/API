import json

import requests


class HandleRequest(object):
    """
    对request请求进行封装
    """
    header = None

    def __init__(self):
        """"创建请求会话"""
        self.my_session = requests.Session()

    def send_request(self, method, path, data=None, is_json=False, **kwargs):
        method = method.lower()

        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                print(e)
                data = eval(data)

        if method == "get":
            res = self.my_session.request(method, path, params=data, headers=self.header, **kwargs)

        elif method == "post":
            if is_json:
                res = self.my_session.request(method, path, json=data, headers=self.header, **kwargs)
            else:
                res = self.my_session.request(method, path, data=data, headers=self.header, **kwargs)
        elif method == "put":
            res = self.my_session.request(method, path, data=data, headers=self.header, **kwargs)
        elif method == "delete":
            res = self.my_session.request(method, path, headers=self.header, **kwargs)

        else:
            res = None
            print("不支持{}的请求方法".format(method))
        return res

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.my_session.close()


do_request: HandleRequest()
