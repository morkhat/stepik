import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    service = Service(r"C:\Users\morkhat\Downloads\chromedriver_win32 (9)\chromedriver.exe")
    browser = webdriver.Chrome(service=service)

    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = int(browser.find_element(By.ID, 'input_value').text)

    answer = browser.find_element(By.ID, 'answer')
    browser.execute_script('return arguments[0].scrollIntoView(true);', answer)
    answer.send_keys(str(calc(x)))

    for selector in ['//*[@id="robotCheckbox"]', '//*[@id="robotsRule"]', '//*[@type="submit"]']:
        element = browser.find_element(By.XPATH, selector)
        browser.execute_script('return arguments[0].scrollIntoView(true);', element)
        element.click()


except Exception as error:
    print(f'Трэйсбэк: {error}')

finally:
    #print(By.mro())
    time.sleep(5)
    browser.quit()