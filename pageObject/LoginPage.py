from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Loginpage:
    textbox_user_xpath="//input[@id='Email']"
    textbox_password_xpath="//input[@id='Password']"
    button_login_xpath="//button[normalize-space()='Log in']"
    button_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver = driver
        self.wait=WebDriverWait(self.driver,20)

    def setUserName(self, username):
        email_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.textbox_user_xpath))
        )
        email_field.clear()
        email_field.send_keys(username)
        # self.driver.find_element(By.XPATH, self.textbox_user_xpath).clear()
        # self.driver.find_element(By.XPATH,self.textbox_user_xpath ).send_keys(username)

    def setPassword(self, password):
        pwd=self.wait.until(
            EC.visibility_of_element_located((By.XPATH,self.textbox_password_xpath))
        )
        pwd.clear()
        pwd.send_keys(password)
        # self.driver.find_element(By.ID,self.textbox_password_xpath).clear()
        # self.driver.find_element(By.ID, self.textbox_password_xpath).send_keys(password)

    def loginClick(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def logoutClick(self):
        self.driver.find_element(By.LINK_TEXT,self.button_logout_linktext).click()
