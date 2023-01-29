import logging
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.home_page import HomePage

chrome_service = Service("../drivers/chromedriver.exe")
driver = webdriver.Chrome(service = chrome_service)
driver.get("http://www.pepper.pl")
driver.implicitly_wait(10) # seconds

file_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

#logging.basicConfig(level = logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y %m %d %I:%M:%S %p: ')

logging.basicConfig(
    filename = '../log/' + file_name + ".log",
    encoding = 'utf-8',
    level = logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%Y%m%d %I:%M:%S %p: ')

logger = logging.getLogger()

title = "Pepper.pl - Najlepsze Okazje, Rabaty, Promocje i Błędy Cenowe"
logger.info("title %s", driver.title)
assert title in driver.title

wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains(title))

cookies = driver.get_cookies()
logging.info("cookies %s", len(cookies))

# for cookie in cookies:
#     print(f'Cookie: {cookie}')

all_links = driver.find_elements(By.TAG_NAME, 'a')
logger.info("links %s", len(all_links))

# for link in all_links:
#     url = link.get_attribute('href')
#     print(f'Url: {url}')

# home_page = HomePage(driver)
# home_page.get_page_title()

driver.save_screenshot("../screenshots/" + file_name + ".png")
#driver.get_screenshot_as_file()

driver.close()




