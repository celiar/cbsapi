import json
import requests
import unittest
from IP import ip_tc


class electronicContractSend(unittest.TestCase):
    '''•电子合同申请邮寄-APP接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_tc + "/trade/innovate/electronicContractSend"
        headers = {'Content-Type': 'application/json'}
        #时间戳问题
        data = {
            "orderNo":"PXZCGL130032201905171554380063",
            "receiveName": "张",
            "receivePhone": "15210292934",
            "receiveAddress": "北京",
            "applyTime": 201905230011
        }
        # 19872000001
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
