
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.alert import Alert

link = "https://suninjuly.github.io/simple_form_find_task.html?first_name=1&last_name=2&firstname=3&firstname=4#"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

    alert = Alert(browser)
    text_from_popup = alert.text
    alert.accept()
    print(text_from_popup)

finally:

    time.sleep(3)

    browser.quit()
