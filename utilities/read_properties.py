import configparser

config = configparser.RawConfigParser()
config.read("../configurations/config.ini")


class ReadConfig:

    @staticmethod
    def get_url():
        base_url = config.get('base info', 'base_url')
        return base_url

    @staticmethod
    def get_title():
        base_title = config.get('base info', 'base_title')
        return base_title

    @staticmethod
    def get_chrome_driver_path():
        chrome_location = config.get('webdrivers locations', 'chrome_location')
        return chrome_location

