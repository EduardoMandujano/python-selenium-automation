from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    EMPTY_CART = (By.CSS_SELECTOR, "span.nav-cart-0")
    NUMBER_ZERO = (By.CSS_SELECTOR, "span.nav-cart-0")

    def verify_empty_cart(self, expected_result_3):
        # self.driver.find_element(*EMPTY_CART)
        expected_result_3 = '0'
        actual_result_3 = self.driver.find_element(*self.NUMBER_ZERO).text
        assert expected_result_3 == actual_result_3, f'Expected {expected_result_3} but got actual {actual_result_3}'