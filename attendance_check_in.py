# import time and selenium
import time
from selenium import webdriver

# add path for the firefox driver
driver = webdriver.Firefox(
    executable_path=r'D:\\Projects\\Python Projects\\schoolworkspro automation script\\driver\\geckodriver.exe')

# add username and password of your site
username = ""
password = ""
time.sleep(2)

# add url to your website
driver.get("https://admin.schoolworkspro.com/login")
time.sleep(2)

# inputs username and password
input = driver.find_elements_by_tag_name("input")
for i, elem in enumerate(input):
    if i == 0:
        elem.send_keys(username)
    elif i == 1:
        elem.send_keys(password)
    else:
        break
    print(i)
time.sleep(5)

# clicks on log in button
driver.find_element_by_xpath('//button[normalize-space()="Log in"]').click()
time.sleep(5)

# clicks on PUNCH OUT button
driver.find_element_by_xpath('//button[normalize-space()="PUNCH IN"]').click()
time.sleep(5)

driver.close()
