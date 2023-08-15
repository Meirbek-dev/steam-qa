import pytest

from singleton.driver import Driver
from tests.game_search.test_game_search import TestGameSearch
from tests.privacy_policy.test_privacy_policy import TestPrivacyPolicy


@pytest.fixture(scope="session")
def setup(request):
    request.driver = Driver().connect()

    yield request.driver

    request.driver.quit()


def test_1():
    TestGameSearch().test_game_search()


def test_2():
    TestPrivacyPolicy().test_privacy_policy()
