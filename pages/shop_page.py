from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from webium.wait import wait


class ShopPage(BasePage):
    dropdown_option = Find(
        by=By.CSS_SELECTOR,
        value="span[data-bind='text: title']"
    )
    search_results_info = Find(
        by=By.XPATH,
        value="//div[@class='searchAndSort-container']/div/h1[@class='head_section']"
    )
    view_more_button = Find(
        by=By.XPATH,
        value="//button[.='View More']")
    result_products = Finds(
        by=By.CSS_SELECTOR,
        value="div[class='thumbnail_container_outer']"
    )
    add_product_links = Finds(
        by=By.XPATH,
        value="//button/span[.='Add to bag']/.."
    )
    cart_icon = Find(
        by=By.CSS_SELECTOR,
        value="span[class='tigi-header__bag-icon__label']"
    )
    checkout_button = Find(by=By.XPATH, value="//a[.='Checkout']")

    def get_dropdown_option(self):
        wait(self.dropdown_option.is_displayed)
        return self.dropdown_option.text

    def get_search_results_product_num(self):
        wait(self.search_results_info.is_displayed)
        return self.search_results_info.text.split(sep=" ")[0]

    def click_view_more(self):
        wait(self.view_more_button)
        self.view_more_button.click()

    def get_expected_product_num(self):
        return len(self.result_products)

    def click_buy_product_link(self, index):
        wait(self.add_product_links[index].is_displayed)
        self.add_product_links[index].click()

    def click_cart_icon(self):
        wait(self.cart_icon.is_displayed)
        self.cart_icon.click()

    def click_checkout_button(self):
        wait(self.checkout_button.is_displayed)
        self.checkout_button.click()