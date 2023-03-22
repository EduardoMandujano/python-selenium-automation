from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class SearchResultsPage(Page):
    EMPTY_CART = (By.CSS_SELECTOR, "span.nav-cart-0")
    NUMBER_ZERO = (By.CSS_SELECTOR, "span.nav-cart-0")
    NEW_ARRIVALS_ELEMENT = (By.CSS_SELECTOR, "span.nav-a-content")
    NEW_ARRIVALS_DEALS = (By.XPATH, "//a[@class='mm-merch-panel']")
    MAG_GLASS_ICON = (By.ID, 'nav-search-submit-button')
    SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")
    # SUBNAV_CD_VINYL = (By.XPATH, "//div[@data-category='music']")

    def verify_empty_cart(self, expected_result_3):
        # self.driver.find_element(*EMPTY_CART)
        expected_result_3 = '0'
        actual_result_3 = self.driver.find_element(*self.NUMBER_ZERO).text
        assert expected_result_3 == actual_result_3, f'Expected {expected_result_3} but got actual {actual_result_3}'

    def open_closing_cat_prod(self):
        self.open_url('https://www.amazon.com/gp/product/B074TBCSC8')

    def hover_new_arrivals(self):
        new_arrivals_element = self.find_element(*self.NEW_ARRIVALS_ELEMENT)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals_element)
        actions.perform()

    def verify_the_deals(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS_DEALS)

    def clicking_on_mag_glass(self):
        self.driver.find_element(*self.MAG_GLASS_ICON).click()

    # ignore this, just tracing my own steps.
    # def verify_selected_cd_vinyl(self):
    #     self.wait_for_element_appear(*self.SUBNAV)

    # Dynamic locator creating function
    def get_subnav_locator(self, category):
        return [self.SUBNAV[0], self.SUBNAV[1].replace('{CATEGORY}', category)]

    def verify_selected_dept(self, category):
        locator = self.get_subnav_locator(category)
        self.wait_for_element_appear(*locator)

