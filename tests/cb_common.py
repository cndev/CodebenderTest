from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


start_url = 'http://localhost'
username = 'USERNAME'
password = 'PASSWORD'


def css(css, driver, wait=10):
    element = WebDriverWait(driver, wait).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css))
    )
    return driver.find_element_by_css_selector(css)

def login(driver):
    css('#login', driver).click()
    css('#username', driver).send_keys(username)
    css('#password', driver).send_keys(password)
    css('#_submit', driver).click()
