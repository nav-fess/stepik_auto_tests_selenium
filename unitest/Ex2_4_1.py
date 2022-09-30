from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def test_2_4_1():

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
    click = button.click()

    time.sleep(4)
    browser.quit()

    return click
