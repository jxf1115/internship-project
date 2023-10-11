# Lesson 4 HW - Julio Fernandez

from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
CART_COUNT = (By.CSS_SELECTOR, '.nav-cart-count.nav-cart-1.nav-progressive-attribute.nav-progressive-content')
PRODUCT_TOCLICK = (By.CSS_SELECTOR, 'div[cel_widget_id="MAIN-SEARCH_RESULTS-3"]')

@when('Search for table')
def search_on_amazon(context):
    context.driver.find_element(*SEARCH_FIELD).send_keys('table')
    context.driver.find_element(*SEARCH_BTN).click()


@when('Click on product')
def click_product(context):
    context.driver.find_element(*PRODUCT_TOCLICK).click()
    sleep(5)



@when('Click Add to Cart')
def click_add_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(2)


@then('Verify Cart has product')
def verify_product_in_cart(context):
    expected_result = '1'
    actual_result = context.driver.find_element(*CART_COUNT).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'