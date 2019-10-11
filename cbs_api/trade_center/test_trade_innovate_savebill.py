import json
import requests
import unittest
from IP import ip_tc


class innovateSavebill(unittest.TestCase):
    '''•顾问报单保存接口'''

    def test_01(self):
        '''正常测试'''
        url = ip_tc + "/trade/innovate/savebill"
        headers = {'Content-Type': 'application/json'}
        data = {
            "oper_type":0,
            "employee_id" : 1,
            "customer_id" : 1053,
            "contact_adress" : "北京市海淀区北太平庄",
            "mobile" : "1234567890",
            "product_id" :1,
            "card_no" : "3333333333333",
            "order_no" : "43333333333",
            "trade_amount" : 1200000.00,
            "trade_time" : 1555652296,
            "trade_way" : 2,
            "signature_page_url" : "",
            "transaction_voucher_url" : "",
            "assets_proof_url" :"",
            "create_time" : 1523618260300,
            "idcard_front_image" : "http://test.puxinasset.com/7a0079f7-00e8-4a4f-9af1-9603d493f6b8?e=1555662942&token=LF4EFQrhdFR-Adabi7lNMchxnG2V0koEdlYBBLqm:JNKbbueRb6k-ehpsJGAgEZAu6Ns=",
            "idcard_back_image" :"http://test.puxinasset.com/7a0079f7-00e8-4a4f-9af1-9603d493f6b8?e=1555662942&token=LF4EFQrhdFR-Adabi7lNMchxnG2V0koEdlYBBLqm:JNKbbueRb6k-ehpsJGAgEZAu6Ns=",
            "email" : "123@123.com",
            "customerCardInfo": {
                "card_no" : "",
                "bank_name" : "",
                "province" :"",
                "city" : "",
                "bank_branch_name" : "",
                "front_image" : "",
                "back_image" : ""
            },
            "billOther": {
                "other_accessory_url" : "",
                "other_accessory2_url" : "",
                "other_accessory3_url" :"",
                "other_accessory4_url" : "",
                "other_accessory5_url" : "",
                "other_accessory6_url" : "",
                "other_accessory7_url" : "",
                "other_accessory8_url" : "",
                "other_accessory9_url" : "",
                "signature_page2_url" : "",
                "signature_page3_url" : "",
                "signature_page4_url" : "",
                "signature_page5_url" : "",
                "signature_page6_url" : "",
                "signature_page7_url" : "",
                "signature_page8_url" : "",
                "signature_page9_url" : ""
            }
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
