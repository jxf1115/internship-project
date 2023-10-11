#Lesson 4 HW - Julio Fernandez

from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
bestsellers = (By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id='nav_cs_bestsellers']")
@when('Click Best Sellers')
def click_bestsellers(context):
    sleep(2)
    element = context.driver.find_elements(*bestsellers)
    element[0].click()
@then('Verify 5 bestseller links on page')
def verify_5bestsellerlinks(context):
    assert context.driver.find_elements(By.CSS_SELECTOR, "#zg_header [class*='zg-nav-tab'] a"), 'Header not present'