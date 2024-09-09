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

driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fcustomer-preferences%2Fedit%3Fie%3DUTF8%26preferencesReturnUrl%3D%252Fcustomer-preferences%252Fedit%253Fie%253DUTF8%2526preferencesReturnUrl%253D%25252Fref%25253Dap_frn_logo%2526ref_%253Dtopnav_lang%26ref_%3Dnav_ya_signin&prevRID=76PAEDNHNM0AKVPZ80QD&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(10)

driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")

driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

driver.find_element(By.CSS_SELECTOR, "[autocomplete='email']")

driver.find_element(By.CSS_SELECTOR, "#ap_password")

driver.find_element(By.CSS_SELECTOR, "#ap_password_context_message_section")

driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")

driver.find_element(By.CSS_SELECTOR, "#continue")

driver.find_element(By.CSS_SELECTOR, "div#legalTextRow [href*='condition_of_use']")

driver.find_element(By.CSS_SELECTOR, "div#legalTextRow [href*='privacy_notice']")

driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")