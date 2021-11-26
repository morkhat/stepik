# используется 4 версия Selenium
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# вместо path
service = Service(r"C:\Users\morkhat\Downloads\chromedriver_win32 (9)\chromedriver.exe")

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    elements = browser.find_elements(By.XPATH, '//input')
    for element in elements:
        element.send_keys("Мой ответ")

    browser.find_element(By.XPATH, '//button').click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    #browser.close()
    time.sleep(30)
    browser.quit()