# 1. Find the most optimal locators for Create Account (Registration) page elements

# Amazon logo
# $$('i.a-icon-logo')
# driver.find_element(By.CSS_SELECTOR, "i.a-icon-logo")

# Create account
# driver.find_element(By.ID, 'continue')

# Your name
# $$('#ap_customer_name')
# driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# Email
# $$('#ap_email')
# driver.find_element(By.CSS_SELECTOR, '#ap_email')

# Password
# $$('#ap_password')
# driver.find_element(By.CSS_SELECTOR, '#ap_password')

# Re-enter password
# $$('#ap_password_check')
# driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# Create your Amazon account button
# $$('#continue')
# driver.find_element(By.CSS_SELECTOR, '#continue')

# Conditions of Use
# driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")

# Privacy Notice
# driver.find_element(By.CSS_SELECTOR, "a[href*='register_notification_privacy_notice']")

# Sign In
# $$('a.a-link-emphasis')
# driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")

# 2. Update a test case to verify that logged-out user sees Sign In when clicking Returns and Orders
# to use Behave (BDD)

from selenium.webdriver.common.by import By
from behave import given, when, then

# Open Amazon Home Page


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

# Find Returns and Orders > Click


@when('Click on Orders')
def orders_click(context):
    context.driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()

# Verification: Sign-In page Opened (Sign In Page Header is visible / Email Input Field is present)


@then('Sign-in header is visible')
def verify_signin_header(context):
    expected_text = 'Sign in'
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert actual_text == expected_text, f'Expected {expected_text} but got actual {actual_text}'


@then('Input Field is Present')
def verify_input_field(context):
    email = context.driver.find_element(By.ID, 'ap_email')
    assert email, f"Expecting Email Field but could not find the field"

# 3.  Create a test case using BDD that opens amazon.com
# clicks on the cart icon and verifies that Your Amazon Cart is empty.


# @given('Open Amazon page')
# def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')


# Find Cart Icon > Click
@when('Click on Cart icon')
def orders_click(context):
    context.driver.find_element(By.ID, 'nav-cart-count').click()


# Verification - Cart is empty
@then('Cart is Empty')
def empty_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-0")
    expected_result_3 = '0'
    actual_result_3 = context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-0").text
    assert expected_result_3 == actual_result_3, f'Expected {expected_result_3} but got actual {actual_result_3}'
