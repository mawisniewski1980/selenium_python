from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtil():

    def __init__(self, driver):
        self.driver = driver

