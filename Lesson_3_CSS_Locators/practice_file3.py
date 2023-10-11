####   Lesson 3 - CSS Selectors   #####

###  Lesson 2 HW review

####  Conditions of Use

###  Privacy Notice



####  Build CSS locators  @ 22:28    #####

#  Search for ID
#   $$('#twotabsearchtextbox')        --->  In CSS you use the '#' for ID,... ID + value
#   Output =  [input#twotabsearchtextbox.nav-input.nav-progressive-attribute]

#   Search for Class  @ 28:15
#    $$('.nav-input.nav-progressive-attribute')   --->  in CSS you use '.' for Class, if there is a space between mult values, you use a '.' for each space,...
#            ... for spaces AFTER single values, you do NOT need to keep the space like you do in XPATH
#    Output =  (2) [input#twotabsearchtextbox.nav-input.nav-progressive-attribute, input#nav-search-submit-button.nav-input.nav-progressive-attribute]

#      **** Build locators with 'Class' first!  @ 33:20
#   Search for Others  @38:20
#     $$("[name='field-keywords'][type='text']")  ---> name, type, etc...use [] for each as shown here
#   Output =  [input#twotabsearchtextbox.nav-input.nav-progressive-attribute]
#
# # # #         Using 'contains' in your search when using 'href'   @ 1:08:30
#       $$('[href*="ap_signin_notification_condition_of_use"]')  ---> use '*' before '=" and use a portion of the entire href value
#

# # # #       Searching for links within parent tag element   @ 1:12:00
#       $$("#legalTextRow a")                      --> add space between 'Row' and 'a' which is the parent element you seek
#        Output = 2 links  --> (2) [a,a]               --> next step below is to find one specific link of the two
#       $$("#legalTextRow a[href*='condition_of_use']")  ---> this is adding 'contains' to find specific link within parent element (a)


####            Behavior Driven Development (BDD)  @ 1:17:23
#
#   Under python-selenium-automation>Features>tests>product_search.feature  you will find a test case in Behave language
#    -->        Feature: Test Scenarios for Search functionality      @ 1:23:24
#
#                   Scenario: User can search for a product
#                       Given Open Google page                  ---> using "command" + 'B' while moving cursor to each line will take you to corresponding code for each line
#                       When Input Car into search field
#                       And Click on search icon
#                       Then Product results for Car are shown
#
#
#


