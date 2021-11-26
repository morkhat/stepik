from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import math
import re

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    service = Service(r"C:\Users\morkhat\Downloads\chromedriver_win32 (9)\chromedriver.exe")
    browser = webdriver.Chrome(service=service)

    link0 = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link0)

    if WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "$100")
    ):
        browser.find_element(By.XPATH, '//*[@id="book"]').click()

    x_element = (browser.find_element(By.XPATH, '//*[@id="input_value"]')).text

    (browser.find_element(By.XPATH, '//*[@id="answer"]')).send_keys(calc(x_element))

    (browser.find_element(By.XPATH, '//*[@id="solve"]')).click()

    print((browser.switch_to.alert.text).split(' ')[-1])

except Exception as error:
    print(f'Трэйсбэк: {error}')

finally:
    browser.quit()