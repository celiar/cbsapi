import json
import requests
import unittest
from IP import ip_tc


class profitAccountChange(unittest.TestCase):
    '''•收益账户变更申请接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_tc + "/trade/saveLiquChangeCardUpload"
        headers = {'Content-Type': 'application/json'}
        data = {
            "employeeName":"张云浩",
            "frontImage":"",
            "productId":111,
            "city":"莆田市",
            "searchType":1,
            "bankBranchName":"莆田分行",
            "bankName":"浦发银行",
            "employeeId":"E1079BA8453000000",
            "bankProofUrl":"o_1dbcno10e72gsfgv89dk91kgug.pdf",
            "cardNo":"622909143251257219",
            "auditState":0,
            "changeApplicationUrl":"o_1dbcnocptopi12133ch1gc11e4fl.pdf",
            "backImage":"",
            "tradeAmount":0,
            "province":"福建省",
            "createTime":0,
            "yn":0,
            "customerId":"CB69D783897800000",
            "id":0,
            "isChange":0,
            "createDate":12222
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
