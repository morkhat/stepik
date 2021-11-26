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

    robotCheckbox = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script('return arguments[0].scrollIntoView(true);', robotCheckbox)
    robotCheckbox.click()

    robotsRule = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', robotsRule)
    robotsRule.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

except Exception as error:
    print(f'Трэйсбэк: {error}')

finally:
    time.sleep(5)
    browser.quit()