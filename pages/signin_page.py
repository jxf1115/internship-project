from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    EMAIL_INPUT = (By.CSS_SELECTOR, '#email-2')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input#field')
    LOGIN_BTN = (By.CSS_SELECTOR, 'a.login-button')

    def login(self):
        # self.driver.find_element(*self.EMAIL_INPUT).send_keys('juliofernandez.re@gmail.com')
        # self.driver.find_element(*self.PASSWORD_INPUT).send_keys('Tomas2828')
        # self.click(*self.LOGIN_BTN)
        sleep(2)
        self.wait_for_element_clickable(self.EMAIL_INPUT)
        self.input_text('juliofernandez.re@gmail.com', *self.EMAIL_INPUT)

        self.wait_for_element_clickable(self.PASSWORD_INPUT)
        self.input_text('Tomas2828', *self.PASSWORD_INPUT)

        self.wait_for_element_clickable_click(self.LOGIN_BTN)
        sleep(2)
