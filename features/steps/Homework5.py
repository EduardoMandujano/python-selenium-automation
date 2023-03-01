from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep - Commented out in favor of implicit wait from environment.py
from selenium.webdriver.support import expected_conditions as EC


MENS_JEANS_COLORS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_MENS_JEANS_COLORS = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Navigate to Amazon {mens_jeans_id} Mens Jeans Page')
def open_mens_jeans_page(context, mens_jeans_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{mens_jeans_id}/')


@then('Verify that user can click and select any color')
def click_through_all_colors(context):
    context.driver.find_element(*MENS_JEANS_COLORS) # .click()
    # sleep(4) - Commented out in favor of implicit wait from environment.py

    all_mens_jeans_colors = context.driver.find_elements(*MENS_JEANS_COLORS)
    print('Mens Jeans Colors List', all_mens_jeans_colors)
    expected_mens_jeans_colors = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage', 'Dark Indigo/Rinsed']

    actual_mens_jeans_colors = []
    for color in all_mens_jeans_colors[:5]:
        color.click()
        current_mens_jeans_colors = context.driver.find_element(*CURRENT_MENS_JEANS_COLORS).text
        print('Current Mens Jeans:', current_mens_jeans_colors)
        actual_mens_jeans_colors += [current_mens_jeans_colors]

    assert expected_mens_jeans_colors == actual_mens_jeans_colors, f'Expected {expected_mens_jeans_colors}, got {actual_mens_jeans_colors}'
