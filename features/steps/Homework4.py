from selenium.webdriver.common.by import By
from behave import given, when, then


BESTSELLERS_LINKS = (By.CSS_SELECTOR, "a[href*='zg_bs_tab']")
CUSTOMERSERVICE_LINKS = (By.CSS_SELECTOR, "a[href*='?ref_=nav_cs_customerservice']")


@when('Click on Best Sellers option')
def bestsellers_click(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='?ref_=nav_cs_bestsellers']").click()


@then('User sees five links present')
def five_links_present(context):
    bestsellers_links = context.driver.find_elements(*BESTSELLERS_LINKS)
    print(bestsellers_links)
    print('\nLink count: ', len(bestsellers_links))
    assert len(bestsellers_links) == 5, f'Expected 5 links, but got {len(bestsellers_links)}'


@when('Input kettlebells into the search field')
def adding_coffee_to_cart(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('kettlebells')


@when('Click on magnifying glass icon')
def clicking_on_mag_glass(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click on first kettlebells displayed')
def clicking_on_first_ketts(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='Sporzon-Kettlebell']").click()


@when('Add kettlebells to cart')
def adding_ketts_to_cart(context):
    context.driver.find_element(By. ID, 'add-to-cart-button').click()


@then('Verify that kettlebells were added to cart')
def verifying_ketts_in_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-count')
    expected_ketts_in_cart = '1'
    actual_ketts_in_cart = context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-1").text
    assert expected_ketts_in_cart == actual_ketts_in_cart, f'Expected {expected_ketts_in_cart} kettlebells but actually got {actual_ketts_in_cart}'


@when('Click on Customer Service option')
def open_customer_service_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='ref_=nav_cs_customerservice']").click()


@then('Verify the presence of Welcome to Amazon Customer Service header')
def verify_customer_service_header(context):
    customer_service_header = context.driver.find_element(By.XPATH, "//h1[text()='Welcome to Amazon Customer Service']")
    assert customer_service_header, f'Expected Customer Service Header, but element not present'


@then('Verify the presence of the Customer Service Clickable table')
def verify_customer_service_clickable_table(context):
    customer_service_clickable_table = context.driver.find_element(By.CSS_SELECTOR, '.issue-card-container')
    assert customer_service_clickable_table, f'Expected Customer Service Clickable table, but element not present'


@then('Verify the presence of the Search our help library header')
def verify_help_library_header(context):
    help_library_header = context.driver.find_element(By.XPATH, "//h2[text()='Search our help library']")
    assert help_library_header, f'Expected Search our library header, but element not present'


@then('Verify the presence of the Search our help library input field')
def verify_help_library_input_field(context):
    help_library_input_field = context.driver.find_element(By.ID, 'hubHelpSearchInput')
    assert help_library_input_field, f'Expected Help Library Input field, but element not present'


@then('Verify the presence of the All help topics header')
def verify_all_help_topics_header(context):
    all_help_topics_header = context.driver.find_element(By.XPATH, "//h2[text()='All help topics']")
    assert all_help_topics_header, f'Expected All help topics header, but element not present'


@then('Verify the presence of the Recommended Topics list')
def verify_recom_topics_list(context):
    recom_topics_list = context.driver.find_element(By.CSS_SELECTOR, 'li.help-topics')
    assert recom_topics_list, f'Expected Recommended Topics List, but element not present'




