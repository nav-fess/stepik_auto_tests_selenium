from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_1_6_2():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("load")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    click = button.click()

    time.sleep(7)
    browser.quit()
    
    return click
