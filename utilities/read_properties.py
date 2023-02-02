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

    @staticmethod
    def get_edge_driver_path():
        edge_location = config.get('webdrivers locations', 'edge_location')
        return edge_location

    @staticmethod
    def get_firefox_driver_path():
        firefox_location = config.get('webdrivers locations', 'firefox_location')
        return firefox_location