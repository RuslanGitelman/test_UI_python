import pytest
from time import sleep


@pytest.mark.search
class TestSearchSuite:

    @pytest.mark.tcid50
    def test_search_one_item(self, app):
        app.navigate_to_home_page()
        app.authorize()
        app.home_page_actions.search_item(
            option=app.config["search_one_item"]["option"]
        )
        sleep(7)
        app.shop_actions.verify_search_one_item(
            url=app.config["search_one_item"]["url"]
        )