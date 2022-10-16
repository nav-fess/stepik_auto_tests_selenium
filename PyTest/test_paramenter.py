from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



@pytest.mark.parametrize('page', ["236895", "236896","236897","236898","236899","236904","236903","236905"])
def test_parameter(browser,page):

    link = f"https://stepik.org/lesson/{page}/step/1"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    answer = math.log(int(time.time()))
      

    fn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
    fn.send_keys(answer)
 

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))) 
    click = button.click()
    

    string = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".smart-hints__hint"))) 
    #string = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    

    assert "Correct!" == string.text, "Is not correct"


if __name__ == "__main__":
    test_parameter()
