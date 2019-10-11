import json
import requests
import unittest
from IP import ip_wa


class savebankcard(unittest.TestCase):
    '''保存/更新银行卡接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_wa + "/innovate/savebankcard"
        headers = {'Content-Type': 'application/json', 'clientId':'2'}
        data = {
            "signTime":"2019-01-01",
            "orderNo": "PXZCGL2904991904180001",
            "bindBankId": "123",
            "customerId": 1,
            "cardNo": "123123708090001",
            "bankName": "中国银行",
            "province": "北京",
            "city":"北京",
            "area":"区",
            "bankBranchName":"大望路支行",
            "frontImage": "https://qiniu.puxinasset.com/FornQJckwIfU36IRCyrJQQYnKZci",
            "backImage": "https://qiniu.puxinasset.com/FornQJckwIfU36IRCyrJQQYnKZci",
            "bankCode": "CMB"
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
