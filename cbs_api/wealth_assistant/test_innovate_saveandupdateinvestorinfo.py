import json
import requests
import unittest
from IP import ip_wa


class saveandupdateinvestorinfo(unittest.TestCase):
    '''•保存/修改投资者基本信息接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_wa + "/innovate/saveandupdateinvestorinfo"
        headers = {'Content-Type': 'application/json', 'clientId':'2'}
        data = {
            "orderNo": "PXZCGL1100061805280001",
            "nationality": "中国",
            "profession": "律师",
            "duty": "律师",
            "telephone": "010-99999999",
            "postcode": "000001",
            "email": "123@sina.com",
            "address": "北京市北京市北京市北京市",
            "relation": "1",
            "relationDesc": "ASDC1",
            "beneficiary": "0",
            "beneficiaryDesc": "ASDC1",
            "poorRecord": "0",
            "poorRecordDesc": "ASDC1",
            "sex": "1",
            "age": "45"
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
