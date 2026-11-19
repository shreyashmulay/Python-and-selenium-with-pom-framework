import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer():
    # locators
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_xpath = "//label[normalize-space()='Male']"
    rdFemaleGender_xpath = "//label[normalize-space()='Female']"
    # txtDob_xpath = ""
    cbox_taxExpmpt_xpath = "//input[@id='IsTaxExempt']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtcustomerRoles_xpath = "//ul[@class='select2-selection__rendered']"
    lstitemAdministrators_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-tjy3-1']"
    lstitemRegistered_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-uz0q-3']"
    lstitemGuests_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-ffuw-4']"
    lstitemVendors_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-yalp-5']"
    drpmgrOfVendor_xpath = "//span[@class='select2-selection select2-selection--single']"
    txtAdminCommtent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH,self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//span[@role='presentation'][normalize-space()='×']").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click() is not working on list items hence using javaScript function
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
            drp = Select(self.driver.find_element(By.XPATH,self.drpmgrOfVendor_xpath))
            drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH,self.rdMaleGender_xpath).click()

        elif gender == 'Female':
            self.driver.find_element(By.XPATH,self.rdFemaleGender_xpath).click()

        else:
            self.driver.find_element(By.XPATH,self.rdMaleGender_xpath).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)


    def setLastName(self, lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)


    # def setDob(self, dob):
    #     self.driver.find_element(By.XPATH,self.txtDob_xpath).send_keys(dob)
    def setTaxExempt(self):
        self.driver.find_element(By.XPATH,self.cbox_taxExpmpt_xpath).click()

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()

