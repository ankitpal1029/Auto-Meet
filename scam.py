



from dotenv import load_dotenv
import os
load_dotenv()

import schedule
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

mail_address = os.environ.get("email")
password = os.environ.get("password")


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
  
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})

opt.binary_locatioin = "/usr/bin/chromium-browser"
driver = webdriver.Chrome(chrome_options=opt)

action = ActionChains(driver)

def turnOffMicCam():
  
    # turn off Microphone
    time.sleep(2)
    driver.find_element_by_xpath(
        "//div[@class='IYwVEf HotEze uB7U9e nAZzG']//div[@class='oTVIqe BcUQQ']//*[local-name()='svg']").click()
    driver.implicitly_wait(3000)
  
    # turn off camera
    time.sleep(2)
    action.key_down(Keys.CONTROL).send_keys('e').key_up(Keys.CONTROL).perform()
    driver.implicitly_wait(3000)

def AskToJoin():
    # Ask to Join meet
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    # Ask to join and join now buttons have same xpaths

def Glogin(mail_address, password):
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
  
    # input Gmail
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)
  
    # input Password
    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(10)
  
    # go to google home page
    driver.get('https://google.com/')
    driver.implicitly_wait(100)



def job():
    Glogin(mail_address,password)

    driver.get('https://meet.google.com/ich-mjxj-wmk')
    driver.refresh()
    turnOffMicCam()
    AskToJoin()

schedule.every().tuesday.at("11:10").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

