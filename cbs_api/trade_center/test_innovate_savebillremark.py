import json
import requests
import unittest
from IP import ip_tc


class savebillremark(unittest.TestCase):
    '''顾问报单备注保存接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_tc + "/trade/innovate/savebillremark"
        headers = {'Content-Type': 'application/json'}
        data = {
            "billId": 2,
            "remark": "发电公司的供电所覆盖色如果第三方公司的风格斯蒂芬告"
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
