from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class MainPage(Page):
    ALL_HIGH_LABEL = (By.CSS_SELECTOR, 'div[wized="projectStatus"]')

    def open_main(self):
        self.driver.get('https://soft.reelly.io/')
        sleep(2)

    def verify_high_demand_tags_present(self):
        expected_label = 24
        actual_label = self.driver.find_elements(*self.ALL_HIGH_LABEL)
        assert expected_label == len(
            actual_label), f'Error, expected {expected_label} did not match actual {len(actual_label)}'
