from selenium import webdriver
import os

def insert_img(driver, file_name):
    base_dir = str(os.path.dirname(os.path.dirname(__file__)))
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]
    file_path = base + "/report/images/" + file_name
    driver.save_screenshot(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver, 'baidu.jpg')
    driver.quit()
