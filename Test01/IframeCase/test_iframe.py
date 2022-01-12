'''
Created on Jan 11, 2022

@author: Admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestIframe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="E:\\FSoft\\Selenium\\chromedriver_win32\\chromedriver.exe")
        
    def test_iframe_in_python(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_js_element_iframe.asp")
        self.assertIn("iframe", driver.title)
        element = driver.find_element_by_css_selector('button.w3-red')
        element.send_keys(Keys.RETURN)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()