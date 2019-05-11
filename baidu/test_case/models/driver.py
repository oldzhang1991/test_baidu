from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def browser(browser='Chrome'):
    if browser is 'Chrome':
        driver = webdriver.Chrome()
    elif browser is 'ff':
        driver = webdriver.Firefox()
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get('http://www.baidu.com')
    dr.find_element(By.XPATH, '//*[@id="u1"]/a[7]').click()
    sleep(3)
    dr.quit()