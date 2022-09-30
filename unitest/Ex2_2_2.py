from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def test_2_2_2():

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fn = browser.find_element(By.CSS_SELECTOR, "#input_value")
    
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(fn.text))

    browser.execute_script("window.scrollBy(0, 100);")    

 	
    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    click = button.click()

    time.sleep(3)
    browser.quit()

    return click






