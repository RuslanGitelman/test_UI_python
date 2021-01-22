import logging

from webium import BasePage
from pages.base_page_object import BasePageObject
from pages.shop_page import ShopPage
import allure
from selenium.webdriver.common.action_chains import ActionChains

LOGGER = logging.getLogger(__name__)


class ShopActions(BasePage, BasePageObject):

    # Get an instance driver, app, page locators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.shop_actions = ShopPage(driver=self.driver)

    @allure.step("Verify default sort option")
    def verify_sort_option(self, option_name):
        LOGGER.info("Verify default sort option")
        default_option_name = self.shop_actions.get_dropdown_option()
        assert default_option_name == option_name, f"Test verify default sort option failed. " \
                                                   f"Expected default option: {option_name}, " \
                                                   f"Actual default option: {default_option_name}"

    @allure.step("Verify search results info")
    def verify_search_results_info(self):
        LOGGER.info("Verify search results info")
        product_num = self.shop_actions.get_search_results_product_num()
        # while True:
        #     while not self.shop_actions.view_more_button.is_displayed():
        #         ActionChains(driver=self.driver).send_keys('ue015').perform()
        # while self.shop_actions.view_more_button.is_displayed():
        #     self.shop_actions.click_view_more()
        actual_product_num = self.shop_actions.get_product_num()
        assert product_num == actual_product_num, f"Test search failed. " \
                                                  f"Expected result product's num: {product_num}, " \
                                                  f"Actual result product's' num: {actual_product_num}"

    @allure.step("Add specified product to cart")
    def add_product_to_cart(self, index):
        LOGGER.info("Add specified product to cart")
        self.shop_actions.click_buy_product_link(index)

    @allure.step("Open order menu")
    def open_order_menu(self):
        LOGGER.info("Open order menu")
        self.shop_actions.click_cart_icon()
        self.shop_actions.click_checkout_button()