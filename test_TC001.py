from selenium.webdriver import Chrome
import TakeScreenshot
import pytest

@pytest.fixture(scope="module")
def setPath():
    global driver
    path = "C:\\Users\\User\\Desktop\\Chrome WebDriver\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path) # this will be local at first, have to make it global
    yield
    driver.close()

def test_registration_valid_data(setPath):
    driver.get("http://thetestingworld.com/testings/")
    driver.get_screenshot_as_file("C:/Users/User/PycharmProjects/LearnPytest/BeforeRegistration.png")
    assert driver.current_url =="http://thetestingworld.com/testings/"
    #driver.get_screenshot_as_file("C:/Users/User/PycharmProjects/LearnPytest/BeforeRegistration.png") -- Style 1
    TakeScreenshot.take_page_screenshot(driver,"FirstScreenshot") # Style 2
    driver.execute_script("window.scrollTo(0,400)")  # Scroll the window for 400pixels.