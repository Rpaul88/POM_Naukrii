# from selenium import webdriver................Moved to conftest
# from selenium.webdriver import ActionChains
from pages.LoginPage import Login
from pages.HomePage import Logout
from data.TestData import *

import pytest #.................................After creating conftest for driver reference

@pytest.mark.usefixtures("test_setup") #........ "test_setup"--Method declared in conftest

# driver=webdriver.Chrome(executable_path="C:/Users/Guest User/PycharmProjects/POM_Practice1/drivers/chromedriver.exe")
# driver.get("https://www.naukri.com/nlogin/login")..............Moved to Loginpage


class Test_Naukri:

    def test_login(self):
        driver=self.driver #.........Reverse should be provided in pages for driver reference
        lp = Login(driver) #........Object creation for Login page with driver instance
        # lp.naukri_Login(USERNAME,PASSWORD)  #.........We will get all functions from Login page
        lp.naukri_Login(lp.get_val("Sheet1","USERNAME"),lp.get_val("Sheet1","PASSWORD"))




    def test_logout(self):
        driver = self.driver
        lp = Logout(driver)
        lp.naukri_Logout()


# If password refernce provided in Loginpage, In naukri_Login(), no arguments(USERNAME,PASSWORD) required.
# AND hence TestData.py reference (from data.TestData import *) also not required.




# # Login.......................................................Moved to Login page
# driver.find_element_by_id("usernameField").send_keys("rpaulpj88@gmail.com")
# driver.find_element_by_id("passwordField").send_keys("R6j35h@123")
# driver.find_element_by_xpath("//button[text()='Login']").click()
#
# # Logout........................................................Moved to Home page
# act = ActionChains(driver)
# act.move_to_element(driver.find_element_by_xpath("//div[text()='My Naukri']"))
# act.perform()
# driver.find_element_by_xpath("//a[text()='Logout']").click()
