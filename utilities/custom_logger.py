import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='../logs/example.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        return logger
