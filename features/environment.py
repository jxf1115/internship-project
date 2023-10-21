from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    # Normal non-headless
    # service = Service(executable_path='./chromedriver')
    # context.driver = webdriver.Chrome(service=service)

    options = Options()
    options.add_argument('--headless')
    service = Service(executable_path='./chromedriver')
    context.driver = webdriver.Chrome(
        options=options,
        service=service
    )
    context.driver.set_window_size(1920, 1080)

    ### FIREFOX ###
    #service = Service(executable_path='./geckodriver')
    #context.driver = webdriver.Firefox(service=service)

    ### BROWSERSTACK ###

    # bs_user = 'juliofernandez_Lq6Xy8'
    # bs_key = 'arKeUGsZnvyyWSiWSrVQ'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'OS X',
    #     'osVersion': '10',
    #     'browserName': 'Chrome',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.maximize_window()
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
