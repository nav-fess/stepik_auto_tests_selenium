from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    fn = browser.find_element(By.NAME, "firstname")
    fn.send_keys("fn")
    ln = browser.find_element(By.NAME, "lastname")
    ln.send_keys("ln")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("email")

    file = browser.find_element(By.NAME, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'upload.txt')
    file.send_keys(file_path)


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






