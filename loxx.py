import logging

logging.basicConfig(filename="./Logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %I:%M:%S %p',
                            level=logging.INFO,
                            encoding='utf-8'
                            )

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")