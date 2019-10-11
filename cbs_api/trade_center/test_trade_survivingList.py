import json
import requests
import unittest
from IP import ip_tc


class survivingList(unittest.TestCase):
    '''•产品存续列表接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_tc + "/trade/survivingList"
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "稳金宝",
            "tradeTimeBegin": 1554307200,
            "tradeTimeEnd": 1554307200,
            "productAttribute": 1,
            "customerRealName": "张三",
            "source": 2,
            "employeeRealName": "李四",
            "employeeOrg": "机构",
            "establishTimeBegin": 1554307200,
            "establishTimeEnd": 1554307200,
            "parentProductType": "大类",
            "productType": "小类"
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
