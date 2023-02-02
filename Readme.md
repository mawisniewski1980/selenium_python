

#####   -s print statements, -v verobose
#####   pytest -v -s
#####   pytest -v -s .\test_cases\test_home_page.py --browser chrome
#####   pytest -v -s --html=report.html .\tests\test_webdriver.py
#####   pytest -v -s --html=report.html --self-contained-html .\tests\test_webdriver.py
#####   pytest -v -s --html=.\reports\report.html --self-contained-html .\tests\test_webdriver.py

### @pytest.fixture()
#### Executes specific method before every test method

### @pytest.yield_fixture() deprecated 
#### Executes specific method before & after every test method


#############################################

# packages

## Selenium libraries
## Pytest
## pytest-html
## pytest-xdist - parallel
## openpyxl  -  excel support
## allure-pytest - allure reports