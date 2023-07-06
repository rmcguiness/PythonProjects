from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ACCOUNT_EMAIL = "ryanmcguiness123@gmail.com"
ACCOUNT_PASSWORD = "Rm122798!"
PHONE = "732-675-8146"

# INITIALIZE DRIVER
chrome_driver_path = "/Users/ryanmcguiness/Documents/ChromeDriver/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3616981067&distance=25&f_AL=true&f_E=2&f_JT=F&f_SB2=4&geoId=103644278&keywords=software%20engineer&refresh=true")
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    ) 
sign_in = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in.click()
time.sleep(5)

# LOGIN
email_field = driver.find_element(By.id, 'username')
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.id, 'password')
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(5)

# Fetch all job listings on page
all_listing = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')

for listing in all_listing:
    print(listing.accessible_name)
    listing.click()
    time.sleep(2)
    # Apply to single job
    try:
        apply_btn = driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')
        apply_btn.click()
        time.sleep(5)

        phone = driver.find_element(By.CLASS_NAME, 'fb-single-line-text--input')
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
    
        #Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print('No application Button, skipped')
        continue

time.sleep(5)
driver.quit()