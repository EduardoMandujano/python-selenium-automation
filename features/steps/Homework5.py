from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep - Commented out in favor of implicit wait from environment.py
from selenium.webdriver.support import expected_conditions as EC


MENS_JEANS_COLORS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_MENS_JEANS_COLORS = (By.CSS_SELECTOR, "#variation_color_name .selection")
# KETTS_PRODUCT_NAMES = (By.CSS_SELECTOR, "span.a-size-base-plus")
# CURRENT_KETTS_PRODUCT_NAMES = (By.CSS_SELECTOR, "span.a-size-base-plus .selection")
# KETTS_PRODUCT_NAMES = (By.CSS_SELECTOR, "span.a-size-base-plus")
# CURRENT_KETTS_PRODUCT_NAMES = (By.CSS_SELECTOR, "span.a-size-base-plus .selection")
# KETTS_PRODUCT_IMAGES = (By.CSS_SELECTOR, "img.s-image")


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


# @then('Verify that search results have a product name and image')
# def click_through_all_ketts(context):
    # context.driver.find_element(*KETTS_PRODUCT_NAMES).click()
    # context.driver.find_element(By.CSS_SELECTOR, "a.a-link-normal").click()

    # all_ketts_prod_names = context.driver.find_elements(*KETTS_PRODUCT_NAMES)
    # print('Kettlebells Product Names List', all_ketts_prod_names)
    # expected_ketts_prod_names = ['Amazon Basics Vinyl Coated Cast Iron Kettlebell Weight',
                               #   'Lifeline Kettlebell Weight for Whole-Body Strength Training',
                                #  'Kettlebell Kings | Powder Coated Kettlebell Weights (5-90LB) For Women & Men | Durable Coating for Grip Strength, Rust Prevention, Longevity | American Style Weight Increments']

   #  actual_ketts_prod_names = []
    # for names in all_ketts_prod_names[:3]:
        # names.click()
        # current_ketts_prod_names = context.driver.find_element(*CURRENT_KETTS_PRODUCT_NAMES).text
       #  print('Current Kettlebells Names:', current_ketts_prod_names)
        # actual_ketts_prod_names += [current_ketts_prod_names]

    # assert expected_ketts_prod_names == actual_ketts_prod_names, f'Expected {expected_ketts_prod_names}, got {actual_ketts_prod_names}'

