import time

import pytest
from selenium import webdriver
from trio._tests.type_tests import path

from pageObject.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseurl=ReadConfig.getApplicationURL()
    path="E:/Python/Testing/Python+Selenium/Framework-Pytest-POM-HTML_Reports/testData/Logindata.xlsx"
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test__DDT_Login(self,setup):
        self.logger.info("**** Test Case Of DDT 002 ****")
        self.logger.info("**** Verify Login Test ****")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Loginpage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,"Sheet1")
        print("No of rows in excel sheet",self.rows )

        lst_status=[]

        for i in range(2,self.rows +1):
            self.user=XLUtils.readData(self.path,"Sheet1",i,1)
            self.password = XLUtils.readData(self.path, "Sheet1", i, 2)
            self.exp=XLUtils.readData(self.path, "Sheet1", i, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.loginClick()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("**** Verified Login Test ****")
                    self.lp.logoutClick()
                    lst_status.append("pass")
                elif self.exp=="Fail":
                    self.logger.info("**** Failed to Verify Login Test ****")
                    self.lp.logoutClick()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="pass":
                    self.logger.info("**** Failed to Verify Login Test ****")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("**** Verified Login Test ****")
                    lst_status.append("Pass")

            if "Fail" not in lst_status:
                self.logger.info("**** Verified Login DDT Test ****")
                self.driver.close()
                assert True
            else:
                self.logger.info("**** Failed to Verify Login DDT Test ****")
                self.driver.close()
                assert False

        self.logger.info("**** End of DDT login TC ****")
        self.logger.info("**** Completed Test_002_DDT_Login ****")





