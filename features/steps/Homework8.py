from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_INPUT_FIELD = (By.ID, 'twotabsearchtextbox')


@given('Open Sample Closing Category Product Page')
def closing_sale_sample_product(context):
    context.app.search_results_page.open_closing_cat_prod()


@when('Hover over New Arrivals option')
def hover_new_arrivals(context):
    context.app.search_results_page.hover_new_arrivals()


@then('Verify that user can see the New Arrivals deals')
def verify_the_deals(context):
    context.app.search_results_page.verify_the_deals()


@when('Select department by alias {alias}')
# def cds_and_vinyl_dept(context, alias):
def select_department(context, alias):
    context.app.header.select_department(alias)


@when('Input text {text}')
def search_terms_input(context, text):
    # context.app.header.search_terms_input(text)
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(text)


@then('Verify that {category} Department is selected')
def selected_cd_vinyl(context, category):
    context.app.search_results_page.verify_selected_dept(category)


