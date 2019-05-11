class Page(object):

    baidu_url = 'https://www.baidu.com'

    def __init__(self, selenium_driver, base_url = baidu_url, parent=None):

        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def __open(self, url):

        self.driver.get(url)
        assert self.on_page(), '所在网站不是%s' % url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self, url):
        return self.__open(url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)