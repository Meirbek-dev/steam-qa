from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from singleton.meta_class_singleton import MetaClassSingleton
from webdriver_manager.chrome import ChromeDriverManager


class Driver(metaclass=MetaClassSingleton):
    connection = None

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument("--incognito")

    def connect(self):
        if self.connection is None:
            self.connection = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=self.chrome_options,
            )
        return self.connection
