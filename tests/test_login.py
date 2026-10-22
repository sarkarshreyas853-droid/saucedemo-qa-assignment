from selenium import webdriver
from selenium.webdriver.common.by import By

def test_valid_login():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    driver.quit()