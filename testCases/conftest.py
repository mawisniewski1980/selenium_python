import pytest
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utilities.read_props import ReadCfg


@pytest.fixture
def setup():
    # def setup(browser):
    ct = datetime.datetime.now()

    service = Service(ReadCfg.get_chrome_driver_path())
    driver = webdriver.Chrome(service=service)
    driver.get(ReadCfg.get_app_url())
    driver.implicitly_wait(15)  # seconds
    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
