import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    service = Service(r"C:\Users\morkhat\Downloads\chromedriver_win32 (9)\chromedriver.exe")
    browser = webdriver.Chrome(service=service)

    link0 = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link0)

    browser.find_element(By.XPATH, '//button').click()

    browser.switch_to.alert.accept()

    time.sleep(0.5)

    x = int(browser.find_element(By.ID, 'input_value').text)

    browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))

    browser.find_element(By.XPATH, '//button').click()

except Exception as error:
    print(f'Трэйсбэк: {error}')

finally:
    time.sleep(5)
    browser.quit()