from datetime import date

from src.objects.footer import Footer
from src.objects.home_page import HomePage
from src.objects.privacy_policy_page import PrivacyPolicyPage
from src.singleton.driver import Driver
from src.utils.utils import (DataUtils,
                             JSUtils)


class TestPrivacyPolicy(PrivacyPolicyPage):
    @staticmethod
    def get_expected_languages():
        test_data_path = 'resources/test_data.json'
        test_data = DataUtils.get_data(test_data_path)
        return test_data["test_privacy_policy"]["expected_languages"]

    def is_language_switch_displayed(self):
        assert self.get_language_switch().is_displayed(), "Language switch is not displayed"

    def are_all_languages_supported(self, expected_languages):
        supported_languages = self.get_supported_languages()
        for language in expected_languages:
            assert language in supported_languages, f"{language} is not supported"

    def is_revised_this_year(self):
        assert self.get_revision_year() == date.today().year, f"Revision year is {self.get_revision_year()}, not {date.today().year}"

    @staticmethod
    def is_new_tab_opened(num_of_tabs, new_num_of_tabs):
        assert num_of_tabs != new_num_of_tabs, f"New {num_of_tabs} tab isn't {new_num_of_tabs} opened"

    def test_privacy_policy(self):
        driver = Driver().connect()
        expected_languages = self.get_expected_languages()

        home_page = HomePage()
        home_page.load()
        num_of_tabs = len(driver.window_handles)
        JSUtils.scroll_to_the_bottom(driver)

        footer = Footer()
        footer.click_privacy_policy_anchor()

        privacy_policy_page = PrivacyPolicyPage()
        privacy_policy_page.load()
        new_num_of_tabs = len(driver.window_handles)
        self.is_new_tab_opened(num_of_tabs, new_num_of_tabs)
        self.is_language_switch_displayed()
        self.are_all_languages_supported(expected_languages)
        self.is_revised_this_year()
