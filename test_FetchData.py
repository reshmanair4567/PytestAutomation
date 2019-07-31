import ec as ec
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import time
import pytest

@pytest.fixture(scope="module")
def environment_setup():
    global driver
    path = "C:\\Users\\User\\Desktop\\Chrome WebDriver\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://thetestingworld.com/testings/")
    # Maximize browser
    driver.maximize_window()
    driver.refresh()
    yield
    driver.close()

def test_verify_registration(environment_setup):
    time.sleep(20)
    driver.implicitly_wait(60)

    #work on dropdown
    wait=WebDriverWait(driver,100)
    wait.until(ec.text_to_be_present_in_element(By.ID,'countryId'),"India")
    obj=Select(driver.find_element_by_id("countryId"))

