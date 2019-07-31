from selenium.webdriver import Chrome
import pytest
a=100

#setting up Fixtures
@pytest.fixture()
def setPath():
    global driver
    path = "C:\\Users\\User\\Desktop\\Chrome WebDriver\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path) # this will be local at first, have to make it global
    yield
    driver.close()

#@pytest.mark.skip("don't want to execute")
#@pytest.mark.Smoke
#@pytest.mark.skipif(a>100,reason ="Don't do")
def test_registration_valid_data(setPath):
    driver.get("http://thetestingworld.com/testings/")
    driver.get_screenshot_as_file("C:/Users/User/PycharmProjects/LearnPytest/BeforeRegistration.png")
    assert driver.current_url =="http://thetestingworld.com/testings/"


#@pytest.mark.Sanity
def test_iregistration_valid_data(setPath):
    driver.get("http://thetestingworld.com/testings/")
    driver.maximize_window()
    assert driver.title=="Login & Sign Up Forms"

