import json
import requests
import unittest
from IP import ip_pc


class seachProductType(unittest.TestCase):
    '''•根据父类id 查询对应的子类接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_pc + "/product/searchProductType"
        headers = {'Content-Type': 'application/json'}
        data = "123"

        with requests.post(url=url, headers=headers, data=data) as response:
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
