# используется 4 версия Selenium
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# вместо path
service = Service(r"C:\Users\morkhat\Downloads\chromedriver_win32 (9)\chromedriver.exe")

link = "http://suninjuly.github.io/find_link_text"

mask = str(math.ceil(math.pow(math.pi, math.e)*10000))

data = {'first_name':'Ivan', 'last_name':'Petrov', 'city':'Smolensk','country':'Russia'}

element = {'first_name':'//input[@name="first_name"]','last_name':'//input[@name="last_name"]',
           'city':'//input[@class="form-control city"]','country':'//input[@id="country"]'}


try:
    browser = webdriver.Chrome(service=service)
    browser.get(link)
    browser.find_element(By.LINK_TEXT, mask).click()

    for key1, key2 in zip(data.keys(), element.keys()):
        browser.find_element(By.XPATH, element[key1]).send_keys(data[key2])

    browser.find_element(By.XPATH, '//button').click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    #browser.close()
    time.sleep(30)
    browser.quit()