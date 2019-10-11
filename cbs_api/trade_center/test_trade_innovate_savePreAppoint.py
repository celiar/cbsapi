import json
import requests
import unittest
from IP import ip_tc


class savePreAppoint(unittest.TestCase):
    '''•保存预约信息接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_tc + "/trade/innovate/savePreAppoint"
        headers = {'Content-Type': 'application/json'}
        data = {
            "id": 1,
            "order_no": "ASC123243",
            "customer_id": 12,
            "customer_certificates_type": 0,
            "customer_certificates_no": "1232323",
            "customer_mobile": "1234567890",
            "customer_state": 3,
            "customer_real_name": "马克",
            "customer_front_image": "http://test.puxinasset.com/7a0079f7-00e8-4a4f-9af1-9603d493f6b8?e=1555662942&token=LF4EFQrhdFR-Adabi7lNMchxnG2V0koEdlYBBLqm:JNKbbueRb6k-ehpsJGAgEZAu6Ns=",
            "customer_back_image": "http://test.puxinasset.com/7a0079f7-00e8-4a4f-9af1-9603d493f6b8?e=1555662942&token=LF4EFQrhdFR-Adabi7lNMchxnG2V0koEdlYBBLqm:JNKbbueRb6k-ehpsJGAgEZAu6Ns=",
            "employee_id": 1,
            "employee_idcard_no": "AS12232",
            "product_id": 1,
            "pre_amount": 10000.00,
            "pre_time": 1436864169,
            "remark": "预约",
            "create_time": 1436864169,
            "modify_time": 1436864169,
            "accept_time": 1436864169
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
