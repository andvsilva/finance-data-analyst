import os
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth ## https://pypi.org/project/selenium-stealth/
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

#driver.get('https://www.google.com')
driver.get('https://login.contaazul.com/?_ga=2.78443218.737391194.1676223898-1924661478.1676223898&_gl=1*ys6rip*_ga*MTkyNDY2MTQ3OC4xNjc2MjIzODk4*_ga_0ZF31QJEMG*MTY3NjIyMzgyNi42LjEuMTY3NjIyNTEwNy42MC4wLjA.#/')
time.sleep(3)

#search = driver.find_element_by_name("q")
#search.send_keys("house")
#search.send_keys(Keys.ENTER)

# login and password inputs:
email = driver.find_element('xpath','/html/body/div[4]/div/div[1]/div/div/div[2]/div/div/div[3]/div/div/form/div/div/div[1]/div/div/div[1]/input')
password = driver.find_element('xpath', '/html/body/div[4]/div/div[1]/div/div/div[2]/div/div/div[3]/div/div/form/div/div/div[2]/div/div/div[1]/input')

# insert - email and password
email.send_keys("your_email@gmail.com")
time.sleep(2)
password.send_keys("your_password_here")
time.sleep(3)

# click on the button to login
button_enter = driver.find_element('xpath','/html/body/div[4]/div/div[1]/div/div/div[2]/div/div/div[3]/div/div/form/div/div/div[4]/div/div/span/button')
button_enter.click()

time.sleep(10)
#driver.close()