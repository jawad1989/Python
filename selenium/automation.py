"""
http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_webpage():
    with open('test.html', mode='a') as my_file:
        text = my_file.write(chrome_browser.page_source)


chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
chrome_browser.maximize_window()

# check title
assert 'Selenium Easy ' in chrome_browser.title

# get button inner html 
show_message_button = chrome_browser.find_element_by_class_name("btn-default")
print(show_message_button.get_attribute('innerHTML'))

# add message in text and click button
# user_button  = chrome_browser.find_element_by_css_selector("#get-input > .btn")
# print(user_button)

assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id("user-message")
user_message.clear()
user_message.send_keys('Im extra cool')

show_message_button.click()


# verify output message
output_message = chrome_browser.find_element_by_id("display")
assert 'Im extra cool' in output_message.text

# to close
# chrome_browser.close()
# chrome_browser.close()
# chrome_browser.quit()