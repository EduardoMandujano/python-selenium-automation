from pages.main_page import MainPage
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)



