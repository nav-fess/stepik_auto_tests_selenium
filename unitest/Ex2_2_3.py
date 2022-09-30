from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def test_2_2_3():

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
    click = button.click()

    time.sleep(3)
    browser.quit()

    return click






