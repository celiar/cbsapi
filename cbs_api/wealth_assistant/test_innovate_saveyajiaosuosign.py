import json
import requests
import unittest
from IP import ip_wa


class saveyajiaosuosign(unittest.TestCase):
    '''亚租所电子签名保存接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_wa + "/innovate/saveyajiaosuosign"
        headers = {'Content-Type': 'application/json', 'clientId':'2'}
        data = {
            "orderNo": "PX1238123947",
            "customerId": "1",
            "signPicture": "马克吐温",
            "investorProtocol": "马克吐温",
            "operatortProtocol": "马克吐温",
            "reviewerProtocol": "马克吐温",
            "guaranteeProtocol": "马克吐温",
            "riskevaluateProtocol": "马克吐温",
            "signTime":"2019-01-01"
        }

        with requests.post(url=url, headers=headers, data=json.dumps(data)) as response:
            code = response.status_code
            response_time = response.elapsed.microseconds / 1000
            return_data = response.text
            print("返回数据:%s" % return_data)
            # print(data)
            # print(response.headers)
            print("请求地址:%s" % response.url)
            print("状态码:%d" % code)
            print("响应时间:%s毫秒" % response_time)
            # time.sleep(1)
            self.assertEqual(code, 200, "状态码错误")
            print("成功")
