import logging

from pageObjects.HomePage import HomePage
from testCases.BaseTest import BaseTest
from utilities.cust_logger import LogGen
from utilities.read_props import ReadCfg

logger = LogGen.loggen(__name__)


class Test_001_Home(BaseTest):

    def test_home_page_title(self, setup, caplog):
        caplog.set_level(logging.INFO, logger=__name__)
        logger.info("**** Test_001_Home ****")
        logger.info("**** test_home_page_title ****")

        self.driver = setup
        self.homePage = HomePage(self.driver)
        self.page_title = self.homePage.get_title()
        if self.page_title == self.get_title:
            assert True
            self.driver.close()
            logger.info("**** test_home_page_title PASSED ****")
        else:
            self.homePage.save_scr('test_home_page_title')
            self.driver.close()
            logger.error("**** test_home_page_title FAIL ****")
            assert False

    def test_home_page_title_fail(self, setup, caplog):
        caplog.set_level(logging.INFO, logger=__name__)
        logger.info("**** Test_001_Home ****")
        logger.info("**** test_home_page_title_fail ****")

        self.driver = setup
        self.homePage = HomePage(self.driver)
        self.page_title = self.homePage.get_title()
        if self.page_title == self.get_title_fail:
            assert True
            self.driver.close()
            logger.info("**** test_home_page_title_fail PASSED ****")
        else:
            self.homePage.save_scr('test_home_page_title_fail')
            self.driver.close()
            logger.error("**** test_home_page_title_fail FAIL ****")
            assert False
