import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 4 версия Selenium!!! используется вместо path, в ковычках должен быть прописан путь до хромдрайвера
service = Service(r"C:\Users\morkhat\Downloads\chromedriver_win32 (9)\chromedriver.exe")

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    elements = browser.find_elements(By.XPATH, '//label[contains(text(),"*")]/following-sibling::input')

    for element in elements:
        element.send_keys("Вводим данные")

    time.sleep(10)
    # Отправляем заполненную форму
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(10)
    browser.quit()