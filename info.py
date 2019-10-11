"""

脚本编写:王延晓
日期:2019年04月15日下午
项目:CBS分拆产品中心和交易中心及电子合同的接口自动化测试

设备号：
三星NOTE8 ce091719ec20a33f047e
华为荣耀9i 37KRX18B05013659
小米8 6300e251
红米5A 1877d8c6

---------------------------------------------------------------------------
reports是测试报告目录，测试报告的标题为产生报告时间

testcase
    data_center 数据中心-交易查询服务-电子合同接口
    product_center CBS拆分产品中心接口
    trade_center CBS拆分交易中心接口
    wealth_assistant 普信财富助手-iPad-客户服务-电子合同接口

checkphone 用于调用接口前进行电话号码前端验证

IP 内的文件修改后可以作用全局,修改接口ip地址只需要修改ip内的变量即可

runtest 运行测试用例，通过unittest加载测试用例

sendEmail 自动发送测试报告，可在runtest配置发送请求




---------------------------------------------------------------------------


类名称命名：
类总是使用驼峰格式命名，以test_开头便于管理用例的执行。
类名应该简明，精确，并足以从中理解类所完成的工作。
常见的一个方法是使用表示类型或者特性的其后缀，例如:SQLEngine ，MimeTypes
对于基类而言，可以使用一个 Base 或者 Abstract 前缀
不要滥用 *args 和 **kwargs，可能会破坏函数的健壮性


----------------------------------------------------------------------------


类名内注释 -- 报告中显示测试接口名
方法名内注释 -- 报告中显示测试用例名


"""