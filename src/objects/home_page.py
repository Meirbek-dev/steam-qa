from src.singleton.driver import Driver


class HomePage(object):
    def __init__(self):
        self.driver = Driver().connect()
        self.__home_page_link: str = "https://store.steampowered.com/"

    def load(self):
        self.driver.get(self.__home_page_link)
