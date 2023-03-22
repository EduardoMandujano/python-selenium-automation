from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):
    ORDERS_CLICK = (By.XPATH, "//a[@id='nav-orders']")
    VISIBLE_SIGNIN = (By.XPATH, "//h1[@class='a-spacing-small']")
    PRESENT_INPUT_FIELD = (By.ID, 'ap_email')
    CART_ICON_CLICK = (By.ID, 'nav-cart-count')
    EMPTY_CART = (By.CSS_SELECTOR, "span.nav-cart-0")
    NUMBER_ZERO = (By.CSS_SELECTOR, "span.nav-cart-0")
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    SEARCH_INPUT_FIELD = (By.ID, 'twotabsearchtextbox')

    def click_orders_menu(self):
        self.click(*self.ORDERS_CLICK)

    def click_cart_icon(self):
        self.click(*self.CART_ICON_CLICK)

    def select_department(self, alias):
        department_dropdown_menu = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_dropdown_menu)
        select.select_by_value(f'search-alias={alias}')

    def search_terms_input(self, text, *SEARCH_INPUT_FIELD):
        e = self.driver.find_element(*SEARCH_INPUT_FIELD)
        e.clear()
        e.send_keys(text)
        print(f'Inputting text: {text}')

