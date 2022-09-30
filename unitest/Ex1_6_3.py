from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

def test_1_6_3():

    link = "http://suninjuly.github.io/find_xpath_form"


    browser = webdriver.Chrome()
    browser.get(link)
   
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("I")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("P")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("S")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("R")

    button = browser.find_element(By.XPATH, "//button[@type='submit']") 
    click = button.click()


    time.sleep(4)
    browser.quit()

    return click
