import logging


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='SSSS %(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %I:%M:%S %p',
                            level=logging.INFO,
                            encoding='utf-8'
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
