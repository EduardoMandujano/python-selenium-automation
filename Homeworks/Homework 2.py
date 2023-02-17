# 1. I watched the whole class and coded along,
# I also registered for Codewars (username Eduardo_Mandujano)
# I read the XPATH article

# 2. The locators practice code is here:

# Amazon logo
# $x("//i[@aria-label='Amazon']")
# driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# Continue button
# driver.find_element(By.ID, 'continue')

# Need help link
# $x("//span[@class='a-expander-prompt']")
# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot password link
# driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-In link
# driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon button account
# driver.find_element(By.ID, 'createAccountSubmit')

# Conditions of use link
# $x("//a[@href='"/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&amp;nodeId=508088"']")
# driver.find_element(By.XPATH, "//a[@href='"/gp/help/customer/display.html/ref=ap_desktop_footer_cou?ie=UTF8&amp;nodeId=508088"']")

# Privacy Notice link
# $x("//a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_privacy_notice?ie=UTF8&amp;nodeId=468496']")
# driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_desktop_footer_privacy_notice?ie=UTF8&amp;nodeId=468496']")


# 3. The test case for  Sign In page will go here:
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='/Users/eduar/Automation/python-selenium-automation/chromedriver')
service = Service('/Users/eduar/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

# Open Amazon Home Page
driver.get('https://www.amazon.com/')

# Find Returns and Orders > Click
driver.find_element(By.XPATH, "//span[@class='nav-line-2']").click()

# Verification: Sign-In page Opened (Sign In Page Header is visible / Email Input Field is present)
expected_result = '"Sign-In Header"'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
print(actual_result)

expected_result_2 = '"Email Input Field Present"'
actual_result_2 = driver.find_element(By.XPATH, "//input[@type='email']").text
print(actual_result_2)

assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
print('Sign-In Header Verified')

assert expected_result_2 == actual_result_2, f'Expected {expected_result_2} but got actual {actual_result_2}'
print('Email Input Field Verified')

if (expected_result == actual_result_2) and (expected_result_2 == actual_result_2):
    print('Test Case Passed')
else:
    print('Test Case Failed')

driver.quit()

# 4. Committed and pushed to Repo: