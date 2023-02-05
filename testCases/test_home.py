import pytest
from selenium import webdriver

from pageObjects.HomePage import HomePage
from utilities.read_props import ReadCfg
from utilities.cust_logger import LogGen

class Test_001_Home:
    base_url = ReadCfg.get_app_url()
    title = ReadCfg.get_app_title()
    title_fail = ReadCfg.get_app_title_fail()
    logger = LogGen.loggen()

    def test_home_page_title(self, setup):
        self.logger.info("**** Test_001_Home ****")
        self.logger.info("**** test_home_page_title ****")

        self.driver = setup
        self.driver.get(self.base_url)
        self.homePage = HomePage(self.driver)
        self.page_title = self.homePage.get_title()
        if self.page_title == self.title:
            assert True
            self.driver.close()
            self.logger.info("**** test_home_page_title PASSED ****")
        else:
            self.homePage.save_scr('test_home_page_title')
            self.driver.close()
            assert False
            self.logger.error("**** test_home_page_title FAIL ****")

    def test_home_page_title_fail(self, setup):
        self.logger.info("**** Test_001_Home ****")
        self.logger.info("**** test_home_page_title_fail ****")

        self.driver = setup
        self.driver.get(self.base_url)
        self.homePage = HomePage(self.driver)
        self.page_title = self.homePage.get_title()
        if self.page_title == self.title_fail:
            assert True
            self.driver.close()
            self.logger.info("**** test_home_page_title_fail PASSED ****")
        else:
            self.homePage.save_scr('test_home_page_title_fail')
            self.driver.close()
            assert False
            self.logger.error("**** test_home_page_title_fail FAIL ****")

