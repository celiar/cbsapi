import json
import requests
import unittest
from IP import ip_tc


class productLiquidationAuditExport(unittest.TestCase):
    '''•产品清算审核列表导出接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_tc + "/trade/productLiquidationAuditExport"
        headers = {'Content-Type': 'application/json'}
        data = {
            "productName": "存金宝",
            "productState": 3,
            "productTypeId": 1,
            "parentProductType": 6,
            "liquidationAuditState": 1,
            "yn": "32",
            "profitType": 1

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
