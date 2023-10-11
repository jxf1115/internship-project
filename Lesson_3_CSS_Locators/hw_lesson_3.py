#   Homework Lesson 3 - CSS Locators
#

#  0) Repeat Class Code

#from behave import given, when, then
#from selenium.webdriver.common.by import By


#@given('Open Amazon page')
#def open_amazon(context):
#    context.driver.get('https://www.amazon.com/')


#@when('Search for table')
#def search_on_amazon(context):
#    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
#    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


#@then('Verify search result is correct')
#def verify_search_result(context):
#    expected_result = '"table"'
#    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold').text
#    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

#   1) Find CSS Selectors

#   Amazon logo                         => By CSS Selector, $$('.a-icon a-icon-logo')
#   Create account header               => By XPATH,  $x("//h1[text()='Create account' and @class='a-spacing-small']")
#   Your Name field                     => By CSS Selector,  $$('#ap_customer_name.a-input-text a-span12 auth-autofocus auth-required-field')
#   Email field                         => By CSS Selector,  $$('.ap_email [type="email"]')
#   Password field                      => By CSS Selector,  $$('#ap_password [type="password"]')
#   Password must be 6 char             => By CSS Selector,  $x("//div[text()='Passwords must be at least 6 characters.' and @class='a-alert-content']")
#   Re-enter Password field             => By CSS Selector,  $$('#ap_password_check [type="password"]')
#   Create your Amazon account (Continue) button   => By CSS Selector,  $$('#continue [type="submit"]')
#   Conditions of Use link              => By CSS Selector,  $$('[href*="ap_register_notification_condition_of_use?"]')
#   Privacy Notice link                 => By CSS Selector,  $$('[href*="ap_register_notification_privacy_notice?"]')
#   Sign-in link                        => By CSS Selector,  $$('.a-link-emphasis.a-row')

#   2) Test Case in BDD for EX 2 of HW 2
# Separate files to be sent: hw_3_ex_2.py and hw_3_ex_2.feature

#   3) Test Case in BDD for Amazon Cart
# Separate files to be sent: