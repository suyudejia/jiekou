import unittest
import json
from demo import RunMain
import HTMLTestRunner
import mock
from mock_demo import mock_test

class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run =RunMain()
        # self.userid = self.test_01()

    def test_03(self):
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': 1001,

        }
        # mock_data = mock.Mock(return_value=data)
        # self.run.run_main = mock_data
        url = 'http://coding.imooc.com/api/cate'
        res = mock_test(self.run.run_main,data,url,'POST',data)

        # res = self.run.run_main(url,'POST',data)
        print(res)
        print('这是第一个case')

        self.assertEqual(res['errorCode'],1001,'测试失败')

    # @unittest.skip('test_02')
    def test_02(self):

        data = {
            'timestamp': '1507034803124',
            'uid': '5249192',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': '1001',
        }
        url = 'http://coding.imooc.com/api/cate'
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['errorCode'],1003,'测试失败')
        print('这是第二个case')

    def test_01(self):
        data = {
            'timestamp': '1507034803124',
            'uid': '5249192',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode': '1001',
        }
        url = 'http://coding.imooc.com/api/cate'
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['errorCode'], 1003, '测试失败')
        print('这是第二个case')


if __name__ == '__main__':
    filepath = "C:\\Users\\suyu9\\PycharmProjects\\interface\\report\\htmlreport1.html"
    fp = open(filepath,'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_03'))
    suite.addTest(TestMethod('test_02'))

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is first report')
    runner.run(suite)
    unittest.main()
    # unittest.TextTestRunner().run(suite)