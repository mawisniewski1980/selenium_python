#####   -s print statements, -v verobose
#####   pytest -v -s

### @pytest.fixture()
#### Executes specific method before every test method

### @pytest.yield_fixture() deprecated 
#### Executes specific method before & after every test method


#############################################

## runner commands

#### pytest -v -s .\tests\test_home.py
#### python -m pytest -v -s .\tests
#### python -m pytest -v -s .\tests\test_home.py
#### python -m pytest -v -s .\tests\test_home.py --browser edge
#### python -m pytest -v -s .\tests\test_home.py --browser chrome

### report with two threads
#### python -m pytest -v -s -n=2 .\tests\test_home.py --browser chrome

### report with html report
#### python -m pytest -v -s --html=Reports\report.html .\tests\test_home.py --browser chrome

### report with logs: --capture=tee-sys
#### python -m pytest -v -s --capture=tee-sys --html=Reports\report.html .\tests\test_home.py --browser chrome
#### python -m pytest -v -s -n=2 --capture=tee-sys --html=Reports\report.html .\tests\test_home.py --browser chrome

## packages

### Selenium libraries
### Pytest
### pytest-html
### pytest-xdist - parallel
### openpyxl  -  excel support
### allure-pytest - allure reports


