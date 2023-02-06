from pageObjects.HomePage import HomePage
from utilities.read_props import ReadCfg
from utilities.cust_logger import LogGen
import logging

class Test_001_Home:
    base_url = ReadCfg.get_app_url()
    title = ReadCfg.get_app_title()
    title_fail = ReadCfg.get_app_title_fail()

    def test_home_page_title(self, setup, caplog):
        caplog.set_level(logging.INFO, logger=__name__)
        logging.getLogger().info("**** Test_001_Home ****")
        logging.getLogger().info("**** test_home_page_title ****")

        self.driver = setup
        self.driver.get(self.base_url)
        self.homePage = HomePage(self.driver)
        self.page_title = self.homePage.get_title()
        if self.page_title == self.title:
            assert True
            self.driver.close()
            logging.getLogger().info("**** test_home_page_title PASSED ****")
        else:
            self.homePage.save_scr('test_home_page_title')
            self.driver.close()
            caplog.error("**** test_home_page_title FAIL ****")
            assert False

    def test_home_page_title_fail(self, setup, caplog):
        caplog.set_level(logging.INFO, logger=__name__)
        logging.getLogger().info("**** Test_001_Home ****")
        logging.getLogger().info("**** test_home_page_title_fail ****")

        self.driver = setup
        self.driver.get(self.base_url)
        self.homePage = HomePage(self.driver)
        self.page_title = self.homePage.get_title()
        if self.page_title == self.title_fail:
            assert True
            self.driver.close()
            logging.getLogger().info("**** test_home_page_title_fail PASSED ****")
        else:
            self.homePage.save_scr('test_home_page_title_fail')
            self.driver.close()
            logging.getLogger().error("**** test_home_page_title_fail FAIL ****")
            assert False
