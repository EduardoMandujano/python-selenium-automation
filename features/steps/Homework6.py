from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR, "a[href*='www.amazon.com/privacy']")

@given('Open Amazon Terms and Conditions page')
def open_terms_and_conditions(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')


@when('Store original windows')
def current_window(context):
    context.current_window = context.driver.current_window_handle
    print(context.current_window)


@when('Click on Amazon Privacy Notice link')
def click_on_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE_LINK).click()


@when('Switch to the newly opened window')
def switch_to_the_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    print('\nAll Windows: ', windows)
    context.driver.switch_to.window(windows[1])

    context.current_window = context.driver.current_window_handle
    print('\nAfter window switch:')
    print(context.current_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html'))


@then('User can close new window')
def close_new_window(context):
    context.driver.close()


@then('Switch back to original window')
def switch_back_to_original_window(context):
    windows = context.driver.window_handles
    print('\nAll Windows: ', windows)
    context.driver.switch_to.window(windows[0])

