import time
import pytest
from pageObject.LoginPage import Loginpage
from pageObject.AddCustomerPage import AddCustomer
from pageObject.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    
    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("************* SearchCustomerByName_004 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginClick()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******** Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")

        self.driver.close()