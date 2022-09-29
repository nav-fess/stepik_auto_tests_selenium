from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    baks = WebDriverWait(browser, 11).until(EC. text_to_be_present_in_element((By.ID, "price"), "100"))
       
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()
    
    

    number = browser.find_element(By.CSS_SELECTOR, "#input_value")
    
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(number.text))
 	
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
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
