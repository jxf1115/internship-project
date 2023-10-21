from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    FILTERS_BTN = (By.CSS_SELECTOR, 'a.filter-button.w-inline-block div.filter-text')
    HIGH_DEMAND_BTN = (By.CSS_SELECTOR, 'div[wized="priorityStatusHighDemand"].tag-properties.margin-bottom-8 .tag-text-proparties')

    def click_filters(self):
        sleep(2)
        self.wait_for_element_clickable_click(self.FILTERS_BTN)

    def click_high_demand_from_popup(self):
        self.wait_for_element_clickable_click(self.HIGH_DEMAND_BTN)
