from selenium.webdriver import ActionChains
from pages.Webgeneric import Webgeneric

class Logout(Webgeneric):

    def __init__(self, driver):
        self.driver = driver
        Webgeneric.__init__(self,driver)
        self.logout_xpath="//a[text()='Logout']"


    def naukri_Logout(self):

        # Logout
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element_by_xpath("//div[text()='My Naukri']"))
        act.perform()
        # self.driver.find_element_by_xpath("//a[text()='Logout']").click()
        self.submit("xpath",self.logout_xpath)



