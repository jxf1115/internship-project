# # # # #         Lesson 2  -  Locators         # # # # #

# from 'amazon_search_script.py'

#  "driver" = browser

# input search text
#driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')   * * * "By.ID" = Locator, to find particular element

# # #       *** Search Slack for "Locator" Python file from 7/22 by Lana        # # #
#
# # # #   * * *  @ 51:35
# > $x("//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_amazonbasics']")  --> Output is [a.nav-a] which is the element we are looking for ###

# to find text as an element  ####
#     $x("//a[text()='Best Sellers' and @class='nav-a  ']")     ---->  Output is [a.nav-a]


####        Lana's  Lesson 2 code       #######

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
# # create a new Chrome browser instance
# service = Service(executable_path='<provide your absolute path>')
# driver = webdriver.Chrome(service=service)
#
#
# # By ID
# driver.find_element(By.ID, 'nav-search-submit-button')
# driver.find_element(By.ID, 'nav-cart-count')
#
# # By XPATH
#
# # Tag and attribute
# driver.find_element(By.XPATH, "//a[@data-csa-c-content-id='nav_cs_bestsellers']")
# driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
#
# # Multiple attributes
# driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_bestsellers']")
#
# # By Xpath, text
# driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
# driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
#
# # Any tag = *
# driver.find_element(By.XPATH, "//*[text()='Best Sellers' and @class='nav-a  ']")
#
# # Contains
# driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")
# driver.find_element(By.XPATH, "//a[contains(text(), 't Seller') and @class='nav-a  ']")
#
# # //parent[...]//child[...]
# driver.find_element(By.XPATH, "//div[@id='nav-belt']//input[@placeholder='Search Amazon']")



# # # # # #   * * *     Lana's review of the code with explanation per step  @ 1:22:27    * * *    # # # # # #

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # create a new Chrome browser instance -->     # #  * * * Explanation of steps @ 1:24:00
# service = Service(executable_path='https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/mac-x64/chromedriver-mac-x64.zip')   # # *** opens and creates open instance of Chrome
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()       # # ** maximizes window so Selenium will be able to work entire screen and make automation more stable
#
# driver.get('https://www.amazon.com/')         # # ***  'get' command opens webpage
# sleep(4)
#
# # Input search text                                                   # # # ***  @ 1:26:30
# driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')  # # ***  format = 'Find' element + Where (ID, XPath) & some action (click, etc.)
#                                                                           # # ***  "send_keys" = populate, so 'popluate' search with 'table'  @ 1:27:31
# # Click on search btn
# driver.find_element(By.ID, 'nav-search-submit-button').click()
#
# expected_result = '"table"'        # # *** because on the screen the text you need includes the "", you treat them as part of 'table'
# actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text   # # *** '.text' instructs to only use the text aspect of that element code  #
#
# assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'  # # *** Assertion explained @ 1:33:35, 2nd part ...@ 1:38:30
#print('Test case passed')

#driver.quit()   # # *** although Selenium should auto close browser, good code will include definitive 'quit' command to ensure closure of browser  #


# # # #     * * *     Homework Review  @ 1:41:23      * * *    # # # #


