from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class HomePage(BasePage):
    img_logo_class = "nav-logo"
    div_footer_data = "div[data-t='bottom']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_if_page_is_loaded(self):
        self.wait_until_visibility_of_element_located((By.CLASS_NAME, self.img_logo_class))
        self.wait_until_visibility_of_element_located((By.CSS_SELECTOR, self.div_footer_data))

    def get_title(self):
        self.check_if_page_is_loaded()
        return self.driver.title
