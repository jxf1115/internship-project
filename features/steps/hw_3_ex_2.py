# HW Lesson 3 Ex 2

from behave import given, when, then
from selenium.webdriver.common.by import By


# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify sign in page opened')
def sign_in(context):
    assert context.driver.find_element(By.ID, 'ap_email'), 'Input field is not shown'  # Verify if signin field is present


@when('Click Cart Icon')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()


@then('Cart is open')
def open_cart(context):
    assert context.driver.find_element(By.ID, 'sc-active-cart'), 'Cart open failed'