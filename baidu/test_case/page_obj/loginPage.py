from selenium import webdriver

from time import sleep

from selenium.webdriver.common.by import By

from baidu.test_case.models.driver import browser
from baidu.test_case.page_obj.base import Page


class Login(Page):
    """
    用户登录页面
    """
    url = "/"
    baidu_login_button_loc = (By.XPATH, '//*[@id="u1"]/a[7]')
    baidu_login_username_button = (By.XPATH, '//*[@id="TANGRAM__PSP_10__footerULoginBtn"]')

    def baidu_login(self):
        self.find_element(*self.baidu_login_button_loc).click()
        sleep(3)
        self.find_element(*self.baidu_login_username_button).click()

    baidu_login_username = (By.XPATH, '//*[@id="TANGRAM__PSP_10__userName"]')
    baidu_login_password = (By.XPATH, '//*[@id="TANGRAM__PSP_10__password"]')
    baidu_login_button = (By.XPATH, '//*[@id="TANGRAM__PSP_10__submit"]')

    def login_username(self, username):
        self.find_element(*self.baidu_login_username).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.baidu_login_password).send_keys(password)

    def login_button(self):
        self.find_element(*self.baidu_login_button).click()

    def login(self, username, password):
        self.open(self.base_url)
        self.baidu_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()

    login_error_hint_loc = (By.XPATH, '//*[@id="TANGRAM__PSP_10__error"]')
    login_success = (By.XPATH, '//*[@id="s_username_top"]/span')

    def user_error(self):
        return self.find_element(*self.login_error_hint_loc).text

    def password_error(self):
        return self.find_element(*self.login_error_hint_loc).text

    def user_longin_success(self):
        return self.find_element(*self.login_success).text


if __name__ == '__main__':
    driver = browser()
    l = Login(driver)
    l.login('17181711131','kissme11223')


