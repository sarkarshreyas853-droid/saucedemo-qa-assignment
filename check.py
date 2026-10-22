from selenium import webdriver
driver = webdriver.Edge()
driver.get("https://www.saucedemo.com")
input("Press Enter to close")
driver.quit()
