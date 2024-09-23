from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com/')


@given('Open the Target Circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@given('Open https://help.target.com/help')
def open_target(context):
    context.driver.get('https://help.target.com/help')


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@when('Search for a {item}')
def search_product(context, item):
    # print(item)
    # Search field => enter tea
    context.driver.find_element(By.ID, 'search').send_keys(item)
    # Search button => click
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)

@when('Click Sign In')
def click_sign_in(context):
    # context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-test='@web/AccountLink']"))).click()


@when('From right side navigation menu, click Sign In')
def click_sign_in_second(context):
    # context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-test='accountNav-signIn']"))).click()


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount) # '6' => 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


@then('Verify header is shown')
def verify_header(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_utilityHeaderContainer']")


@then('Verify that there are {numbers} benefit cells')
def verify_benefit_cells(context, numbers):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='slingshot-components']")
    assert len(links) == int(numbers), f'Expected {numbers} links but got {len(links)}'


# Example with multiple variables:
# @when('Login as {username} and {pw}')
# def search_product(context, username, pw):
#     context.driver.find_element(By.ID, 'username').send_keys(username)
#     context.driver.find_element(By.ID, 'password').send_keys(pw)


# @when('Click on the product in the search results')
# def click_product(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[alt='Starbucks Unsweetened Medium Roast Iced Coffee - 48 fl oz']").click()
#     sleep(5)



@then('Verify "Target Help" header is displayed')
def verify_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[style*='flex-grow: 2']")


@then('Verify "search help" input field and "track an order" button are displayed')
def search_help_and_track(context):
    context.driver.find_element(By.CSS_SELECTOR, "[name*='j_id0:j_id2:j_id32:']")


@then('Verify header has {numbers} buttons')
def verify_benefit_cells(context, numbers):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class='grid_6']")
    assert len(links) == int(numbers), f'Expected {numbers} links but got {len(links)}'


@then('Verify "contact us" and "holiday help" sections are displayed')
def search_help_and_track(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='grid_4 boxSmallr txtAC bigbox2']")


@then('Verify "Browse all Help pages" text is displayed')
def search_help_and_track(context):
    context.driver.find_element(By.ID, "j_id0:j_id2:j_id41:j_id42:form1")


