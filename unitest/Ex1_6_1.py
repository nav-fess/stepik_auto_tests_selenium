from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

def test_1_6_1():

        link = " http://suninjuly.github.io/find_link_text"
        browser = webdriver.Chrome()
        browser.get(link)
        link = browser.find_element(By.LINK_TEXT, "224592")
        link.click()

        
        input1 = browser.find_element(By.NAME, "first_name")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")

        #time.sleep(2)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        click = button.click()
        time.sleep(4)
        # закрываем браузер после всех манипуляций
        browser.quit()    
        
        return click

