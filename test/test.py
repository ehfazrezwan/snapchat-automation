import json
import os
import time
import random

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

desired_cap = {
    "deviceName": "2e18809a",
    "platformName": "Android",
    "appPackage": "com.snapchat.android",
    "appActivity": "com.snapchat.android.LandingPageActivity",
    # "appWaitActivity": "com.snapchat.android.LandingPageActivity"
}

selectors_path = os.path.join(os.getcwd(), 'selectors.json')

with open(selectors_path) as f:
    selectors = json.load(f)

driver = webdriver.Remote(
    command_executor='http://localhost:4723/wd/hub', desired_capabilities=desired_cap)
driver.implicitly_wait(15)

try:
    login_button = driver.find_element_by_xpath(selectors['login_button'])
    if login_button.text == "Log In":
        login_button.click()
    else:
        login_button = driver.find_element_by_xpath(selectors['login_button2'])
        if login_button.text == "Log In":
            login_button.click()
except:
    login_button = driver.find_element_by_xpath(selectors['login_button2'])
    if login_button.text == "Log In":
        login_button.click()

driver.find_element_by_xpath(selectors['username']).send_keys("ehfazr")
driver.find_element_by_xpath(selectors['password']).send_keys("Chromagame3@")
driver.hide_keyboard()
driver.find_element_by_xpath(selectors['submit_pwd']).click()

time.sleep(5)

driver.find_element_by_xpath(selectors['permissions']).click()
driver.find_element_by_xpath(selectors['system_perm']).click()
driver.find_element_by_xpath(selectors['system_perm']).click()
time.sleep(2)
driver.find_element_by_xpath(selectors['system_perm']).click()
time.sleep(2)
# driver.find_element_by_xpath(selectors['avatar']).click()
# driver.find_element_by_xpath(selectors['friends_list']).click()
# driver.find_element_by_xpath(selectors['more_friends']).click()

# # Time to add some friends!
# friend = driver.find_element_by_xpath(selectors['first_friend'])
# actions = TouchAction(driver)

# i = random.randint(10, 20)

# for x in range(i):
#   actions.long_press(friend)
#   actions.perform()
#   time.sleep(1)
#   driver.find_element_by_xpath(selectors['accept_friend']).click()
#   t = random.randint(10, 15)
#   time.sleep(t)

driver.find_element_by_xpath(selectors['goto_chats']).click()
time.sleep(20)
driver.find_element_by_xpath(selectors['first_chat']).click()
time.sleep(2)
# Check if chat input exists

bool_check = False

while not bool_check:
    try:
        driver.find_element_by_xpath(selectors['chat_input']).send_keys("Hello")
        driver.press_keycode(66)
        bool_check = True
    except:
        try:
            driver.find_element_by_xpath(selectors['red_snap']).click()
            bool_check = False
        except:
            try:
                driver.find_element_by_xpath(selectors['purple_snap']).click()
                bool_check = False
            except:
                time.sleep(2)
                driver.find_element_by_xpath(selectors['first_chat']).click()
                bool_check = False
                break
        time.sleep(2)
        driver.find_element_by_xpath(selectors['first_chat']).click()
        bool_check = False
