import json
import requests
import unittest
from IP import ip_pc


class contractTemplateSettingController(unittest.TestCase):
    '''•合同模板设置参数接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_pc + "/product/contractTemplate/settingController"
        headers = {'Content-Type': 'application/json'}
        data = {
            "templet_id": 1,
            "key": "product_name",
            "name": "产品名称",
            "type": "String",
            "is_required": 1,
            "length": "30",
            "regular_expression": "",
            "order": "",
            "groups": "",
            "is_personal": 1
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
