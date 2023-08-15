from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.singleton.driver import Driver


class Footer(object):
    def __init__(self):
        self.driver = Driver().connect()
        self.__privacy_policy_anchor_xpath = '//a[@href="https://store.steampowered.com/privacy_agreement/?snr=1_44_44_"]'

    def click_privacy_policy_anchor(self):
        privacy_policy_anchor = WebDriverWait(self.driver, timeout=3).until(
            lambda w: w.find_element(
                by=By.XPATH, value=self.__privacy_policy_anchor_xpath
            )
        )
        privacy_policy_anchor.click()
