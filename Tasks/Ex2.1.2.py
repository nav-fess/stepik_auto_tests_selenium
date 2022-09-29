from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    box = browser.find_element(By.CSS_SELECTOR, "#treasure")
    number = box.get_attribute("valuex")
    
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    print(f"############ number = {number} ############")
    answer.send_keys(calc(number))
 	
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    button.click()
    button.click()
    button.click()
    button.click()
    button.click()
    button.click()
    button.click()

#    email = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
 #   email.send_keys("email")		

#    time.sleep(2)
    
    # Отправляем заполненную форму
#    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
