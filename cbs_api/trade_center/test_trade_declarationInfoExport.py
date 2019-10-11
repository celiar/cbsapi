import json
import requests
import unittest
from IP import ip_tc


class declarationInfoExport(unittest.TestCase):
    '''•报单列表数据导出接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_tc + "/trade/exportExcel"
        headers = {'Content-Type': 'application/json'}
        data = {
            "productName": "募集金",
            "customerRealName": "张三",
            "auditState": 3,
            "state": 2,
            "source": 2,
            "employeeName": "李四",
            "orgName": "北京",
            "startArriveDate": 1554283396,
            "endArriveDate": 1554283396,
            "startTradeDate": 1554283397,
            "endTradeDate": 1554283397,
            "startSettlementDate": 1554283396,
            "endSettlementDate": 1554283397,
            "settlementState": 1,
            "parentProductType": 6,
            "productType": 1
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
