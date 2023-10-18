from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep



@given('Open Reelly page')
def open_reelly(context):
    context.app.main_page.open_main()


@when('Login')
def login(context):
    context.app.signin_page.login()


@when('Click on Filters')
def click_filters(context):
    context.app.header.click_filters()


@when('Click on High Demand')
def click_high_demand_from_popup(context):
    context.app.header.click_high_demand_from_popup()


@when('Wait for 4 sec')
def wait_sec(context):
    sleep(4)


@then('Verify each product contains High Demand tag')
def verify_high_demand_tags_present(context):
    context.app.main_page.verify_high_demand_tags_present()





