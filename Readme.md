#####   -s print statements, -v verobose
#####   pytest -v -s

### @pytest.fixture()
#### Executes specific method before every test method

### @pytest.yield_fixture() deprecated 
#### Executes specific method before & after every test method


#############################################

## runner commands

#### pytest -v -s .\testCases\TestHome.py
#### python -m pytest -v -s TestCases
#### python -m pytest -v -s .\TestCases\TestHome.py
#### python -m pytest -v -s .\TestCases\TestHome.py --browser edge
#### python -m pytest -v -s .\TestCases\TestHome.py --browser chrome

### report with two threads
#### python -m pytest -v -s -n=2 .\TestCases\TestHome.py --browser chrome

### report with html report
#### python -m pytest -v -s --html=Reports\report.html .\TestCases\TestHome.py --browser chrome

### report with logs: --capture=tee-sys
#### python -m pytest -v -s --capture=tee-sys --html=Reports\report.html .\TestCases\TestHome.py --browser chrome

## packages

### Selenium libraries
### Pytest
### pytest-html
### pytest-xdist - parallel
### openpyxl  -  excel support
### allure-pytest - allure reports