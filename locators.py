from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Locate element:
driver.find_element() # By. / value
# Locate by ID:
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.NAME, 'nav-logo-sprites')
# By Xpath
driver.find_element(By.XPATH, "//img[@alt='Shop Studio Pro headphones']")
# By Xpath multiply
driver.find_element(By.XPATH,"//a[@class='nav-a  ' and @tabindex='0' and @id='nav-link-amazonprime']")
# By Xpath text
driver.find_element(By.XPATH,"//a[text='Best Sellers']")
driver.find_element(By.XPATH,"//h1[text()='Your cart is empty']")


