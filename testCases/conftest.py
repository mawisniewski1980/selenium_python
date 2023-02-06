import pytest
import datetime
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utilities.read_props import ReadCfg


@pytest.fixture
#def setup():
def setup(browser):
    ct = datetime.datetime.now()
    if browser == 'chrome':
        service = Service(ReadCfg.get_chrome_driver_path())
        driver = webdriver.Chrome(service=service)
        print("################################### CHROME ########################################")
    elif browser == 'ff':
        service = Service(ReadCfg.get_firefox_driver_path())
        driver = webdriver.Firefox(service=service)
        print("##################################### FF ###################################################")
    elif browser == 'edge':
        service = Service(ReadCfg.get_edge_driver_path())
        driver = webdriver.Edge(service=service)
        print("##################################### EDGE ###################################################")
    else:
        service = Service(ReadCfg.get_chrome_driver_path())
        driver = webdriver.Chrome(service=service)
        print("################################### CHROME ########################################")

    driver.get(ReadCfg.get_app_url())
    driver.implicitly_wait(15)  # seconds
    #driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name'] = 'pepper'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)