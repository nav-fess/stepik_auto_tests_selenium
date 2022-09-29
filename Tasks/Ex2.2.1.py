from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math



try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    sum = int(num1.text) + int(num2.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))

    #browser.find_element(By.TAG_NAME, "select").click()
    select.select_by_value(str(sum)) 

    print(f"############ SUM = {sum} ############")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    button.click()
    button.click()
    button.click()
    button.click()
    button.click()
    button.click()
    button.click()

    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
