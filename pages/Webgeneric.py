# Explicit wait--->WebGeneric

from selenium.webdriver.support.wait import WebDriverWait         # Explicit wait_2
from selenium.webdriver.support import expected_conditions as EC  # Explicit wait_4 expected_conditions = EC

from pages.Locatorgeneric import Locatorgeneric

class Webgeneric(Locatorgeneric):

    def __init__(self,driver):
        self.driver=driver
        Locatorgeneric. __init__(self,driver)

    # def enter(self,locator,input_val):
    def enter(self,loc_type,loc_val,input_val):
        # self.driver.find_element_by_id(locator).send_keys(input_val)
        self.locator(loc_type,loc_val).send_keys(input_val)

    def submit(self,loc_type,loc_val):


# Inroduced Explicit level wait

        wait = WebDriverWait(self.driver,2)           # Explicit wait_1
        v = self.locator(loc_type,loc_val)
        wait.until(EC.visibility_of(v))      # Explicit wait_3
        v.click()

         # self.driver.find_element_by_xpath(locator).click()
        # self.locator(loc_type,loc_val).click() #----------------------- self.locator(loc_type,loc_val) + click()

