from selenium.webdriver.common.by import By

from src.singleton.driver import Driver


class SteamSearchPage(object):
    def __init__(self):
        self.driver = Driver().connect()
        self.__steam_search_link = "https://store.steampowered.com/search/?term=Dota+2"
        self.__search_box_id = "realterm"
        self.__first_item_xpath = '//span[@class="title"][1]'

    def load(self):
        self.driver.get(self.__steam_search_link)

    def get_search_box_value(self):
        return self.driver.find_element(
            by=By.ID, value=self.__search_box_id
        ).get_attribute("value")

    def get_first_item_name(self):
        return self.driver.find_element(by=By.XPATH, value=self.__first_item_xpath).text

    @staticmethod
    def get_item_row_xpath(item_num):
        return f"(//div[@class='responsive_search_name_combined'])[{item_num}]"

    def get_item_name(self, item_row):
        return self.driver.find_element(
            by=By.XPATH, value=f'{item_row}//span[@class="title"]'
        ).text

    def get_item_release_date(self, item_row):
        return self.driver.find_element(
            by=By.XPATH, value=f'{item_row}//div[contains(@class,"search_released")]'
        ).text

    def get_item_price(self, item_row):
        return self.driver.find_element(
            by=By.XPATH,
            value=f'{item_row}//div[@class="discount_final_price"]',
        ).text

    def get_item_platforms(self, item_row):
        platform_elements = self.driver.find_elements(
            by=By.XPATH,
            value=f'{item_row}//child::span[starts-with(@class,"platform_img")]',
        )
        return [
            element.get_attribute("class").split()[-1] for element in platform_elements
        ]

    def get_item_review(self, item_row):
        return (
            self.driver.find_element(
                by=By.XPATH,
                value=f'{item_row}//span[contains(@class,"search_review_summary")]',
            )
            .get_attribute("data-tooltip-html")
            .split("<")[0]
        )

    def get_item_info(self, item_num):
        item_row_xpath = self.get_item_row_xpath(item_num)
        name = self.get_item_name(item_row_xpath)
        release_date = self.get_item_release_date(item_row_xpath)
        price = self.get_item_price(item_row_xpath)
        platforms = self.get_item_platforms(item_row_xpath)
        review = self.get_item_review(item_row_xpath)
        return [name, release_date, platforms, price, review]
