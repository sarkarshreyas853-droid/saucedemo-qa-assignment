from selenium import webdriver
from selenium.webdriver.common.by import By


def test_locked_out_user():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com")
    
    
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    message = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
    assert "locked out" in message

    driver.quit()   


