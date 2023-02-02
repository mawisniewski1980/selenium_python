import logging
import logging.config

logging.config.fileConfig('../configurations/logging.conf')

class LogGen:
    @staticmethod
    def loggen(name):
        logger = logging.getLogger(name)
        return logger
