from src.models.item import Item
from src.objects.header import Header
from src.objects.home_page import HomePage
from src.objects.steam_search_page import SteamSearchPage
from src.singleton.driver import Driver
from src.utils.utils import DataUtils


class TestGameSearch(SteamSearchPage):
    @staticmethod
    def get_expected_item():
        test_data_path = "resources/test_data.json"
        test_data = DataUtils.get_data(test_data_path)
        return test_data["test_game_search"]["expected_item"]

    def is_correct_item_requested(self, expected_item):
        search_box_value = self.get_search_box_value()
        assert (
            search_box_value == expected_item
        ), f"{expected_item} was not requested, instead '{search_box_value}' was requested"

    def is_correct_result_shown(self, expected_item):
        first_item_name = self.get_first_item_name()
        assert (
            first_item_name == expected_item
        ), f"First item is not {expected_item}, it is {first_item_name}"

    @staticmethod
    def are_items_equal(old_item, new_item):
        assert (
            old_item == new_item
        ), f"The old item: {old_item}, different from the new item: {new_item}"

    def test_game_search(self):
        items_info_path = "tests/game_search/items_info.json"
        expected_item = self.get_expected_item()

        home_page = HomePage()
        home_page.load()

        header = Header()
        header.search_for_item(expected_item)

        steam_search_page = SteamSearchPage()

        self.is_correct_item_requested(expected_item)
        self.is_correct_result_shown(expected_item)

        first_item = Item(*steam_search_page.get_item_info(1))
        second_item = Item(*steam_search_page.get_item_info(2))
        DataUtils.save_info_to_json(items_info_path, first_item.info, second_item.info)
        header.search_for_item(second_item.name)
        self.is_correct_result_shown(second_item.name)
        new_first_item = Item(*steam_search_page.get_item_info(1))
        new_second_item = Item(*steam_search_page.get_item_info(2))
        self.are_items_equal(first_item.info, new_second_item.info)
        self.are_items_equal(second_item.info, new_first_item.info)
        Driver().connect().quit()
