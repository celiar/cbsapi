import HTMLTestReportCN
import time
import unittest
# from sendEmail import *


suite = unittest.defaultTestLoader.discover(start_dir='./cbs_api', pattern='test*.py')
path = time.strftime('%Y_%m_%d_%H.%M.%S', time.localtime(time.time()))
fm = open('./reports/%s cbs系统拆分的接口测试报告.html' % path, 'wb')
HTMLTestReportCN.HTMLTestRunner(stream=fm, title='CBS产品和交易中心|电子合同接口测试', tester='王延晓', description='财富助手相关的接口测试', verbosity=2).run(suite)
fm.close()

# test_dir = "./reports/"
# new_report = new_report(test_dir)
# send_email(new_report)