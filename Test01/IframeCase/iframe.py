'''
Created on Jan 11, 2022

@author: Admin
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="E:\\FSoft\\Selenium\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.w3schools.com/howto/howto_js_element_iframe.asp")
assert "iframe" in driver.title
element = driver.find_element_by_css_selector('button.w3-red')
element.send_keys(Keys.RETURN) 
# try:
#     h1element = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH,"//h1[@class='learntocodeh1']")))
#     print("Hide failed")
# except:
#     print("H1 was hidden")
driver.close()