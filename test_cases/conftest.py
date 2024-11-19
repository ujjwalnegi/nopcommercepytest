import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_metadata.plugin import metadata_key

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",
                     help="Specify the browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    return driver

######### for pytest html reports #######
#hook for adding environment info in html report ########
def pytest_configure(config):  # TO ADD BELOW VALUES IN OUR PREVIOUS HTML REPORT
    config.stash[metadata_key]['Project Name']= 'Ecommerce Project,nopcommerce'
    config.stash[metadata_key]['Test Module Name']= 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name']= 'Ujjwal'
#hook for delete/modify  environment info in html report
@pytest.mark.optionalhook  #TO REMOVE BELOW VALUES FROM OUR PREVIOUS HTML REPORT
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)
