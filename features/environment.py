from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.application import Application
from selenium import webdriver      # Mobile Emulation mode


# Allure logging command below - Lesson 10 for more information
# behave -f allure_behave.formatter:AllureFormatter -o test_results/features/tests/User_can_filter_high_demand.feature


def browser_init(context):
    """
    :param context: Behave context
    """
    #Normal non-headless
    # service = Service(executable_path='./chromedriver')
    # context.driver = webdriver.Chrome(service=service)


    # Headless mode
    #options = Options()
    #options.add_argument('--headless')
    #service = Service(executable_path='./chromedriver')
    #context.driver = webdriver.Chrome(
        #options=options,
        #service=service
    #)
    #context.driver.set_window_size(1920, 1080)

    ### FIREFOX ###
    #service = Service(executable_path='./geckodriver')
    #context.driver = webdriver.Firefox(service=service)

    ### BROWSERSTACK ###

    #bs_user = 'juliofernandez_Lq6Xy8'
    #bs_key = 'arKeUGsZnvyyWSiWSrVQ'
    #url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    # options = Options()
    # bstack_options = {
    #      'os': 'Windows',
    #      'osVersion': '10',
    #      'browserName': 'Chrome',
    #      'sessionName': 'verify_high_demand_feature'
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # Mobile Emulation mode
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    service = Service(executable_path='./chromedriver')
    context.driver = webdriver.Chrome(service=service)
    context.driver = webdriver.Chrome(options=chrome_options)

    # common parts
    context.driver.maximize_window()  # comment out for headless mode
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
