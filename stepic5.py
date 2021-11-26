# используется 4 версия Selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

try:
    service = Service(r"C:\Users\morkhat\Downloads\chromedriver_win32 (9)\chromedriver.exe")
    browser = webdriver.Chrome(service=service)

    #print(browser.capabilities['browserVersion'])
    #print(browser.capabilities['chrome']['chromedriverVersion'])

    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    data = {'first_name': 'Ivan', 'last_name': 'Petrov', 'email': 'test@gmail.com'}

    element = {'first_name': '//input[@class="form-control first" and @required=""]',
               'last_name': '//input[@class="form-control second" and @required=""]',
               'email': '//input[@class="form-control third" and @required=""]'}

    for key1, key2 in zip(data.keys(), element.keys()):
        browser.find_element(By.XPATH, element[key1]).send_keys(data[key2])

    browser.find_element(By.XPATH, '//button').click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

except Exception as error:
    print(f'Трэйсбэк: {error}')

finally:
    #browser.close()
    time.sleep(15)
    browser.quit()