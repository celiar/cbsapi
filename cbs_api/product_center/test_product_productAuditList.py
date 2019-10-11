import json
import requests
import unittest
from IP import ip_pc


class productAuditList(unittest.TestCase):
    '''•产品审核列表接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_pc + "/product/productAuditList"
        headers = {'Content-Type': 'application/json'}
        data = {
            "productName": "稳金宝",
            "productTypeId": 1,
            "auditState": "2",
            "productState": 3,
            "productSource": 4,
            "type": "4",
            "parentProductType": "4",
            "productType": "4",
            "index": 2,
            "startOnlineDate": 1555567322,
            "endOnlineDate": 1555653722,
            "startEstablishDate": 1555567322,
            "endEstablishDate": 1555653722,
            "startApplyDate": 1555567322,
            "endApplyDate": 1555653722
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
