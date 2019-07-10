from pages.Webgeneric import Webgeneric

class Login(Webgeneric):

    def __init__(self,driver):
        self.driver=driver
        Webgeneric.__init__(self,driver)
        self.un_id="usernameField"
        self.pwd_id="passwordField"
        self.sb_xpath="//button[text()='Login']"

    def naukri_Login(self,UN,PWD):

        # self.driver=webdriver.Chrome(executable_path="C:/Users/Guest User/PycharmProjects/POM_Practice1/drivers/chromedriver.exe")
        # self.driver.get("https://www.naukri.com/nlogin/login")..................Moved to conftest

        # Login
        # self.driver.find_element_by_id("usernameField").send_keys(UN)
        # self.driver.find_element_by_id("passwordField").send_keys(PWD)
        # self.driver.find_element_by_xpath("//button[text()='Login']").click()

        # self.enter(self.un_id,UN)
        self.enter("id",self.un_id,UN)

        # self.enter(self.pwd_id,PWD)
        self.enter("id",self.pwd_id,PWD)

        # self.submit(self.sb_xpath)
        self.submit("xpath",self.sb_xpath)


        #----------- If password refernce provided in LoginPage itself-----------------

        # def naukri_Login(self):

        # self.enter("id", self.un_id, self.get_val("Sheet1", "USERNAME"))
        # self.enter("id", self.pwd_id, self.get_val("Sheet1", "PASSWORD"))
        # self.submit("xpath",self.sb_xpath)