import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

try:
    service = Service(r"C:\Users\morkhat\Downloads\chromedriver_win32 (9)\chromedriver.exe")
    browser = webdriver.Chrome(service=service)

    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    # Найти на ней элемент-картинку/ Взять у этого элемента значение атрибута valuex
    valuex = browser.find_element(By.XPATH, '//*[@id="treasure"]').get_attribute('valuex')

    # Посчитать математическую функцию от x, Ввести ответ в текстовое поле.
    browser.find_element(By.XPATH, '//*[@id="answer"]').send_keys(str(log(abs(12 * sin(int(valuex))))))

    # Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!".
    # Нажать на кнопку Отправить.
    for selector in ['//*[@id="robotCheckbox"]', '//*[@id="robotsRule"]', '//*[@type="submit"]']:
        browser.find_element(By.XPATH, selector).click()

except Exception as error:
    print(f'Трэйсбэк: {error}')

finally:
    #browser.close()
    time.sleep(5)
    browser.quit()