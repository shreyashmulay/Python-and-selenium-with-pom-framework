import pytest
from selenium import webdriver
from pageObject.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("**** Test Case 001 ****")
        self.logger.info("**** Verify HomePage Title ****")
        self.driver=setup
        self.driver.get(self.baseurl)
        actual_title=self.driver.title
        if actual_title== "nopCommerce demo store. Login":
            assert True
            self.logger.info("**** Verified HomePage Title ****")
            self.driver.close()
        else:
            self.driver.save_screenshot("E:/Python/Testing/Python+Selenium/Framework-Pytest-POM-HTML_Reports/Screenshots/" + "Test_homePageTitle.png")
            self.logger.error("**** Failed to Verify HomePage Title ****")
            self.driver.close()
            assert False


    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("**** Test Case 002 ****")
        self.logger.info("**** Verify Login Test ****")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserName(self.password)
        self.lp.loginClick()
        act_title=self.driver.title
        self.driver.close()
        if act_title== "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**** Verified Login Test ****")

        else:
            self.driver.save_screenshot("E:/Python/Testing/Python+Selenium/Framework-Pytest-POM-HTML_Reports/Screenshots/" + "Test_Login.png")
            self.logger.error("**** Failed to Verified Login Test ****")
            self.driver.close()
            assert False

