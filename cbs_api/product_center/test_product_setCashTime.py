import json
import requests
import unittest
from IP import ip_pc


class setCashTime(unittest.TestCase):
    '''•产品设置兑付日期接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_pc + "/product/setCashTime"
        headers = {'Content-Type': 'application/json'}
        data = {
            "productId": 2,
            "cashTime": 1554220800
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
