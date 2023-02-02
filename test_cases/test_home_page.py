from page_objects.home_page import HomePage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class TestHomePage_01:
    logger = LogGen.loggen("TestHomePage_01")

    def test_home_page_title(self, setup):
        self.logger.info("******* TestHomePage_01 ******")
        self.logger.info("******* test_home_page_title ******")

        self.driver = setup
        self.home_page = HomePage(self.driver)
        assert ReadConfig.get_title() in self.home_page.get_title()
        self.driver.close()
