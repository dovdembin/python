from selenium import webdriver
from selenium.webdriver.common.by import By

# ====================================================================
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")
logo = driver.find_element(By.CLASS_NAME, "python-logo")

driver.quit()
# ================================================================