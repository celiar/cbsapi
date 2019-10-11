import json
import requests
import unittest
from IP import ip_wa


class contractriskquestion(unittest.TestCase):
    '''•合同风险测评答题接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_wa + "/innovate/contractriskquestion"
        headers = {'Content-Type': 'application/json', 'clientId':'2'}
        data = {
            "orderNo": "PXZCGL1100061805280001",
            "signTime": "2019-01-01",
            "age": "1",
            "education": "1",
            "job": "1",
            "marriage": "1",
            "childrenEdu": "2",
            "childrenJob": "2",
            "station": "1",
            "salary": "1",
            "residence": "2",
            "asset": "2",
            "investment": "3",
            "investmentPer": "4",
            "tradeCenterQ1": "1",
            "tradeCenterQ2": "2",
            "tradeCenterQ3": "3",
            "tradeCenterQ4": "2",
            "tradeCenterQ5": "1",
            "riskQuestion1": "1",
            "riskQuestion2": "21",
            "riskQuestion3": "3",
            "riskQuestion4": "4",
            "riskQuestion5": "5",
            "riskQuestion6": "5",
            "riskQuestion7": "4",
            "riskQuestion8": "3",
            "riskQuestion9": "2",
            "riskQuestion10": "1",
            "riskQuestion11": "1",
            "risklevel": "保守型"
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
