import configparser

cfg = configparser.RawConfigParser()
cfg.read('./Configurations/config.ini')


class ReadCfg():

    @staticmethod
    def get_app_url():
        return cfg.get('common data', 'base_url')

    @staticmethod
    def get_app_title():
        return cfg.get('common data', 'title')

    @staticmethod
    def get_app_title_fail():
        return cfg.get('common data', 'title_fail')

    @staticmethod
    def get_chrome_driver_path():
        return cfg.get('drivers path', 'chrome')

    @staticmethod
    def get_firefox_driver_path():
        return cfg.get('drivers path', 'ff')

    @staticmethod
    def get_edge_driver_path():
        return cfg.get('drivers path', 'edge')

    @staticmethod
    def get_opera_driver_path():
        return cfg.get('drivers path', 'opera')
