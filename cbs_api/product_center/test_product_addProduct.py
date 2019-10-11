import json
import requests
import unittest
from IP import ip_pc


class addProduct(unittest.TestCase):
    '''•新增产品接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_pc + "/product/addProduct"
        headers = {'Content-Type': 'application/json'}
        data = {
            "onlineTime": 1561614360,
            "auditTime": 1577425559,
            "productInnovate": {
                "code": "test",
                "name": "测试002"
            },
            "productInnovateOther": {
                "profitType": 1,
                "payInterestWay":""
            },
            "productInnovateProfitRule": [
                {
                    "minAmount": 22,
                    "maxAmount": 22
                },
                {
                    "minAmount": 33,
                    "maxAmount": 33
                }
            ],
            "productInnovateRakeBack": [
                {
                    "positionName": "测试",
                },
                {
                    "positionName": "测试2"
                }
            ],
            "productContract": [
                {
                    "templetKey": "productCode",
                    "templetValue": "55555555"
                }
            ]

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
