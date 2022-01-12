'''
Created on Jan 12, 2022

@author: Admin
'''
# import the libs
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# create the initial window
driver = webdriver.Chrome(executable_path="E:\\FSoft\\Selenium\\chromedriver_win32\\chromedriver.exe")
# go to the home page
driver.get('https://www.geeksforgeeks.org/')

# storing the current window handle to get back to dashboard
main_page = driver.current_window_handle

# wait for page to load completely
sleep(5)

# click on the sign in tab
driver.find_element(By.CLASS_NAME,'header-main__signup').click()

sleep(5)

# click to log in using facebook
driver.find_element(By.XPATH,'//*[@id="fblogin"]').click()

# changing the handles to access login page
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle
        
# change the control to signin page    
#driver.switch_to.window(login_page)

# user input for email and password
# print('Enter email id : ', end ='')
# email = input().strip()
# print('Enter password : ', end ='')
# password = input().strip()

email = "blue0703t@gmail.com"
password = "blue123456"

# enter the email
driver.find_element(By.XPATH,'//*[@id ="email"]').send_keys(email)

# enter the password
driver.find_element(By.XPATH,'//*[@id ="pass"]').send_keys(password)

# click the login button
driver.find_element(By.XPATH,'//*[@id ="u_0_0"]').click()



# change control to main page
#driver.switch_to.window(main_page)

sleep(10)
# print user name
name=driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/header/div[2]/div/div/div/div/span').text
print('Your user name is : {}'.format(name))

# closing the window
driver.quit()
