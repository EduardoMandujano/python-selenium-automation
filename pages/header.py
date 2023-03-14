from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    ORDERS_CLICK = (By.XPATH, "//a[@id='nav-orders']")
    VISIBLE_SIGNIN = (By.XPATH, "//h1[@class='a-spacing-small']")
    PRESENT_INPUT_FIELD = (By.ID, 'ap_email')
    CART_ICON_CLICK = (By.ID, 'nav-cart-count')
    EMPTY_CART = (By.CSS_SELECTOR, "span.nav-cart-0")
    NUMBER_ZERO = (By.CSS_SELECTOR, "span.nav-cart-0")

    def click_orders_menu(self):
        self.click(*self.ORDERS_CLICK)

    def click_cart_icon(self):
        self.click(*self.CART_ICON_CLICK)

