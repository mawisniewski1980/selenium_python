import logging
from logging.handlers import RotatingFileHandler


class LogGen:
    @staticmethod
    def loggen(name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s')

        #file_handler = logging.FileHandler('./Logs/automation.log')
        # Limit the size to 1000000Bytes ~ 1MB .
        file_handler = RotatingFileHandler('./Logs/automation.log', maxBytes=1000000, backupCount=5)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger
