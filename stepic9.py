import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

try:
    service = Service(r"C:\Users\morkhat\Downloads\chromedriver_win32 (9)\chromedriver.exe")
    browser = webdriver.Chrome(service=service)

    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.txt')

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass

    inputs = ['Aleksey', 'Bychutkin', 'test@gmail.com', file_path]

    for element, value in zip(browser.find_elements(By.XPATH, '//input'), inputs):
        element.send_keys(value)

    browser.find_element(By.XPATH, '//*[@type="submit"]').click()


except Exception as error:
    print(f'Трэйсбэк: {error}')

finally:
    time.sleep(5)
    browser.quit()



