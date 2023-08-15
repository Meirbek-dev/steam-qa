from selenium.webdriver.common.by import By

from src.singleton.driver import Driver


class Header(object):
    def __init__(self):
        self.driver = Driver().connect()
        self.search_field_id = "store_nav_search_term"

    def search_for_item(self, expected_item):
        search_field = self.driver.find_element(by=By.ID, value=self.search_field_id)
        search_field.send_keys(expected_item)
        search_field.submit()
