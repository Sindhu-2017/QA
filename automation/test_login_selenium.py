from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username=driver.find_element(By.ID,"user-name")

username.send_keys("standard_user")

password=driver.find_element(By.ID,"password")

password.send_keys("secret_sauce")

driver.find_element(By.ID,"login-button").click()

products=driver.find_element(By.CLASS_NAME,"title")

print(products.text)

assert products.text == "Products"

driver.save_screenshot("login_result.png")

driver.quit()

