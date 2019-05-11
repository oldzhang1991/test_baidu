import unittest

import pytest, random, sys, time

from baidu.test_case.models.func11 import insert_img
from baidu.test_case.models.myunit import MyTest
from baidu.test_case.page_obj.loginPage import Login

sys.path.append("./models")
sys.path.append("./page_obj")


class TestLogin(MyTest):

    def user_longin_verify(self, username='', password=''):
        Login(self.driver).login(username, password)

    def test_longin1(self):
        """用户名密码为空"""
        self.user_longin_verify()
        po = Login(self.driver)
        self.assertEqual(po.user_error(), "请您输入手机/邮箱/用户名")
        self.assertEqual(po.password_error(), "请您输入手机/邮箱/用户名")
        insert_img(self.driver, "user_pwd_empty.jpg")

    def test_longin2(self):
        """用户名正确密码为空"""
        self.user_longin_verify(username='17181711131')
        po = Login(self.driver)
        self.assertEqual(po.password_error(),"请您输密码")
        insert_img(self.driver, "password_empty.jpg")

    def test_longin3(self):
        """密码正确用户名为空"""
        self.user_longin_verify(password="kissme11223")
        po = Login(self.driver)
        self.assertEqual(po.user_error(),"请您输入手机/邮箱/用户名")
        insert_img(self.driver, "user_empty.jpg")

    def test_longin4(self):
        """用户名密码不匹配"""
        self.user_longin_verify(username='17181711131', password='dasdadsassds')
        po = Login(self.driver)
        self.assertEqual(po.user_error(), "用户名或密码有误，请重新输入或找回密码")
        insert_img(self.driver, "user_pwd_error.jpg")


if __name__ == '__main__':
    unittest.main()