from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test(self):
        self.driver.get("http://html5geek.azurewebsites.net/")
        self.driver.find_element(By.LINK_TEXT, "Vuejs test page").click()
