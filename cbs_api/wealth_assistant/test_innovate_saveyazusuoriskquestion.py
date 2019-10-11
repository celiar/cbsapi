import json
import requests
import unittest
from IP import ip_wa

'''
•调用接口前进行电话号码前端验证
•更多返回错误代码请看首页的错误代码描述
-跟cbs进行同步用的接口方式，没有走mq
tb_electronic_contract

'''
class saveyazusuoriskquestion(unittest.TestCase):
    '''•亚租所合同风险测评答题接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_wa + "/innovate/saveyazusuoriskquestion"
        headers = {'Content-Type': 'application/json', 'clientId':'2'}
        data = {
            "orderNo": "PXZCGL1100061805280001",
            "yajiaosuoQ1": "A",
            "yajiaosuoQ2": "A",
            "yajiaosuoQ3": "A",
            "yajiaosuoQ4": "A",
            "yajiaosuoQ5": "B",
            "yajiaosuoQ6": "C",
            "yajiaosuoQ7": "A",
            "yajiaosuoQ8": "A",
            "yajiaosuoQ9": "A",
            "yajiaosuoQ10": "A",
            "yajiaosuoQ11": "A",
            "yajiaosuoQ12": "A",
            "yajiaosuoQ13": "A",
            "yajiaosuoQ14": "A",
            "yajiaosuoQ15": "D",
            "score":"1",
            "riskType": "C1-保守型",
            "risklevel": "R1 R2 R3",
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
