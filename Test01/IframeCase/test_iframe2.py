'''
Created on Jan 11, 2022

@author: Admin
'''
import unittest
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class TestIframe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="E:\\FSoft\\Selenium\\chromedriver_win32\\chromedriver.exe")
        
    def test_iframe_in_python(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/html/html_iframe.asp") 
        self.assertIn("Iframe", driver.title)
        h1element = driver.find_element(By.CSS_SELECTOR,'#main > h1') 
        self.assertIn("HTML Iframe", h1element.text)
        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/iframe'))
        h1element = driver.find_element(By.CSS_SELECTOR,'#main > h1') 
        self.assertIn("HTML Tutorial", h1element.text)
        linkElement=driver.find_element(By.CSS_SELECTOR,'#topnav > div > div > a:nth-child(5)')
        linkElement.click()         
        WebDriverWait(driver, 10)
        print(driver.find_element(By.CSS_SELECTOR,'#main > h1').text)
        self.assertIn("JavaScript Tutorial", driver.find_element(By.CSS_SELECTOR,'#main > h1').text)
        driver.switch_to.default_content()
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()