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

# By SCC, By ID
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")

# By SCC, By Class
driver.find_element(By.CSS_SELECTOR, ".nav-input")
driver.find_element(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")

# By SCC, by tag & class(es)
driver.find_element(By.CSS_SELECTOR, "input.nav-input.nav-progressive-attribute")

# By SCC, by tag & ID & class
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input.nav-progressive-attribute")

# By CSS, attributes
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, ".nav-input[tabindex='0'][placeholder='Search Amazon']")

# By CSS, attribute, partial match
driver.find_element(By.CSS_SELECTOR, "[href*='notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "[classes*='search']")
driver.find_element(By.CSS_SELECTOR, "[id*='search']")
# By SCC, parent <> child, separate by space
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='privacy']")
driver.find_element(By.CSS_SELECTOR, ".a-box-inner #legalTextRow [href*='privacy']")