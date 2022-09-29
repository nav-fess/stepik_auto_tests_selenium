from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
        

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    number = browser.find_element(By.CSS_SELECTOR, "#input_value")
    
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(number.text))
 	
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
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
