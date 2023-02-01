import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utilities.read_properties import ReadConfig


@pytest.fixture()
def setup():
    print(" ### once BEFORE every test method ### ")
    chrome_service = Service(ReadConfig.get_chrome_driver_path())
    driver = webdriver.Chrome(service=chrome_service)
    driver.get(ReadConfig.get_url())
    driver.implicitly_wait(15)  # seconds
    driver.maximize_window()
    return driver
    #yield
    #print(" ### once AFTER every test method ### ")
    #driver.close()