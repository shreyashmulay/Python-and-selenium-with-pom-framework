import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import argparse

@pytest.fixture
def setup(browser):
    if browser== "chrome":
        options = ChromeOptions()
        # Essential flags to hide automation indicators
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        print("launched on chrome browser")
    elif browser== "firefox":
        options = FirefoxOptions()
        # Firefox specific preference to mask automation
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        driver = webdriver.Firefox(options=options)
        print("launched on Firefox browser")
    elif browser== "edge":
        options = EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Edge(options=options)
        print("launched on Edge browser")
    else:
        driver= webdriver.Ie()
    return driver

def pytest_addoption(parser):
    try:
        parser.addoption("--browser", action="store")
    except (ValueError,argparse.ArgumentError):
        pass

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


# Pytest HTML Reports
def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata['Project Name'] = 'E-commerce Test'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Shreyash'

# Hook for delete/Modify environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins",None)
