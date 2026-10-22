from selenium import webdriver
from selenium.webdriver.common.by import By

def test_checkout():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Shreyas")
    driver.find_element(By.ID, "last-name").send_keys("Sarkar")
    driver.find_element(By.ID, "postal-code").send_keys("703601")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    message = driver.find_element(By.CSS_SELECTOR, '[data-test="complete-header"]').text
    assert "Thank you" in message
    driver.quit()   