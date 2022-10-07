import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_registration():

    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fn = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
    fn.send_keys("first name")

    ln = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
    ln.send_keys("last name")
 	

    email = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
    email.send_keys("email")		

    time.sleep(2)
    

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
  
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    time.sleep(4)
    browser.quit()
   
    assert "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    test_registration()






