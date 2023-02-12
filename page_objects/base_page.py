class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def save_scr(self, filename):
        self.driver.save_screenshot('.//screenshots/' + filename + '.png')