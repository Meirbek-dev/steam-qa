from selenium.webdriver.common.by import By

from src.singleton.driver import Driver


class PrivacyPolicyPage(object):
    def __init__(self):
        self.driver = Driver().connect()
        self.__privacy_policy_link: str = (
            "https://store.steampowered.com/privacy_agreement/?snr=1_44_44_"
        )
        self.__language_switch_id = "languages"
        self.__language_tags_xpath = '//div[@id="languages"]//child::a'
        self.__revision_date_xpath = '//i[contains(text(),"Revision Date")]'

    def load(self):
        self.driver.get(self.__privacy_policy_link)

    def get_language_switch(self):
        return self.driver.find_element(by=By.ID, value=self.__language_switch_id)

    def get_language_tags(self):
        return self.driver.find_elements(by=By.XPATH, value=self.__language_tags_xpath)

    def get_supported_languages(self):
        return [
            language.get_attribute("href").split("/")[-2]
            for language in self.get_language_tags()
        ]

    def get_revision_date(self):
        return self.driver.find_element(by=By.XPATH, value=self.__revision_date_xpath).text

    def get_revision_year(self):
        return int(self.get_revision_date().split()[-1])
