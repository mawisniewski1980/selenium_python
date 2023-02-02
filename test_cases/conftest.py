import time

import pytest
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen

logger = LogGen.loggen("setup")


@pytest.fixture()
def setup(browser):
    ct = datetime.datetime.now()
    logger.info("### Test started at: %s ###", ct)

    if browser == 'ff':
        options = FirefoxOptions()
        #options.add_argument("--headless")
        options.add_argument()
        service = Service(ReadConfig.get_firefox_driver_path())
        driver = webdriver.Firefox(service=service, options=options)
        logger.info("### Browser Firefox ###")
    elif browser == 'edge':
        service = Service(ReadConfig.get_edge_driver_path())
        driver = webdriver.Edge(service=service)
        logger.info("### Browser Edge ###")
    else:
        service = Service(ReadConfig.get_chrome_driver_path())
        driver = webdriver.Chrome(service=service)
        logger.info("### Browser Chrome ###")

    driver.get(ReadConfig.get_url())
    driver.implicitly_wait(15)  # seconds
    driver.maximize_window()
    return driver
    # yield
    # print(" ### once AFTER every test method ### ")
    # driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
