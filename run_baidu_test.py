from HTMLTestRunner import HTMLTestRunner
import unittest
import time, os

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './baidu/report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='百度登录自动化测试报告',
        description='环境: windows 10    浏览器:Chrome'
    )
    discover = unittest.defaultTestLoader.discover('./baidu/test_case', pattern='*_test.py')
    runner.run(discover)
    fp.close()