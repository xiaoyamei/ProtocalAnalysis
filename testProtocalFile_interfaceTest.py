import unittest
import pyexcel
from protocalAnalysis import protocal_dict
import HTMLTestRunner

# 获取excel内的测试用例
testCaseList = pyexcel.get_records(file_name='protocalTestCases.xlsx')


class ProtoTestClass(unittest.TestCase):
    def testProtoFunc(self):
        for i in testCaseList:
            with self.subTest(msg=i['协议说明']):
                self.data = i['协议数据']
                self.expected = i['协议解析']
                self.actually = protocal_dict[i['协议帧']](self.data)
                self.message = "ErrorMessage:\n==期望结果==：\n{}\n==实际结果==：\n{}\nMessageEnd".format(self.expected, self.actually)
                self.assertEqual(self.expected, self.actually, self.message)


if __name__ == "__main__":
    with open('testReport.html', 'w') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="协议接口测试报告", description="用例执行情况")
        unittest.main(verbosity=2, testRunner=runner)

