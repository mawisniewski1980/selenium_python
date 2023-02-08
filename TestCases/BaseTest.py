from Utilities.read_props import ReadCfg


class BaseTest:
    __title = ReadCfg.get_app_title()
    __title_fail = ReadCfg.get_app_title_fail()

    @property
    def get_title(self):
        return self.__title

    @property
    def get_title_fail(self):
        return self.__title_fail
