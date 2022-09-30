from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def test_2_3_2():

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
    click = button.click()

    time.sleep(4)
    browser.quit()

    return click
