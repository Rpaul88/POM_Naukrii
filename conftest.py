import pytest

@pytest.fixture(scope="class")

def test_setup(request):

    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:/Users/Guest User/PycharmProjects/POM_Practice1/drivers/chromedriver.exe")
    driver.get("https://www.naukri.com/nlogin/login")
    driver.implicitly_wait(15)
    request.cls.driver=driver
    yield
    driver.quit()



