#  Homework Lesson_2

# 1) Repeat class code

# open the url ... ('get' command = open, 'open browser')
#driver.get('https://www.amazon.com/')

# input search text
#driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

# click search button
#driver.find_element(By.ID, 'nav-search-submit-button').click()


#expected_result = '"table"'
#actual_result = driver.find_element(By.XPATH, '//span[@class="a-color-state a-text-bold"]').text
#assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'

#sleep(5)

#print('Test case passed')

#driver.quit()

# 2) Practice with Locators

# Amazon logo                           => By XPATH
# Sign In header                        => By XPATH
# Email field                           => By ID, "ap_email"
# Continue button                       => By ID, "continue"
# Conditions of use link                => By XPATH
# Privacy Notice link                   => By XPATH
# Need help link                        => By XPATH
# Forgot your password link             => By ID, "auth-fpp-link-bottom"
# Other issues with Sign-In link        => By ID, "ap-other-signin-issues-link"
# Create your Amazon account button     => By ID, "createAccountSubmit"
# Orders                                => By ID, "nav-orders"

# 3) Test Case - Sign In page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path="/Users/jfernandez/QA/python-selenium-automation/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url ... ('get' command = open, 'open browser')
driver.get('https://www.amazon.com/')

# Click Orders
driver.find_element(By.ID, 'nav-orders').click()


expected_result = 'a-page'        # Sign In Page
actual_result = driver.find_element(By.ID, 'a-page')
expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]').text   # Sign In Header

assert driver.find_element(By.ID, 'ap_email'), 'Input field is not shown' #Verify if signin field is present

# assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'

sleep(5)

print('Test case passed')

driver.quit()


