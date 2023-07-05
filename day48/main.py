from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_driver_path = "/Users/ryanmcguiness/Documents/ChromeDriver/chromedriver"

service = ChromeService(executable_path=chrome_driver_path)

driver  = webdriver.Chrome(service=service)

driver.get("https://www.python.org")

price = driver.find_element(By.ID, "priceblock_ourprice")

print(print.text)


# driver.close()
driver.quit()