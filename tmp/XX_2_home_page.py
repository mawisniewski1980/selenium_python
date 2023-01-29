import unittest
import logging
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

file_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
title = "Pepper.pl - Najlepsze Okazje, Rabaty, Promocje i Błędy Cenowe"


class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('tests in class started')

    @classmethod
    def tearDownClass(cls):
        print('tests in class finished')

    @classmethod
    def setUp(self):
        chrome_service = Service("../drivers/chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get("http://www.pepper.pl")
        self.driver.implicitly_wait(10)  # seconds
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_contains(title))

    @classmethod
    def tearDown(self) -> None:
        self.driver.close()

    def test_if_title_is_correct(self):

        print('title ', self.driver.title)
        assert title in self.driver.title

        cookies = self.driver.get_cookies()
        print('size cookies ', len(cookies))

        links = self.driver.find_elements(By.TAG_NAME, 'a')
        print('size links ', len(links))

        #self.driver.save_screenshot("../screenshots/" + file_name + ".png")


if __name__=="__main__":
    unittest.main()
