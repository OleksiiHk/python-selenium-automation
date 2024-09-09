from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from target_search import expected_result

# Get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open Target website
driver.get('https://www.target.com/')

# Navigate to Sign In page
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(5)
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(5)
# Actual Result
actual_result = driver.find_element(By.XPATH, "//h1/span").text

# Expected Result
expected_result = 'Sign into your Target account'

assert expected_result == actual_result, f'Expected "{expected_result}" but got "{actual_result}"'

# Check if login form is present
login_present = driver.find_element(By.ID, 'login')

if login_present:
    print('Login form is present')

driver.quit()

