from selenium.webdriver import Chrome
import pytest

@pytest.mark.skip
def test():
    path = "C:\\Users\\User\\Desktop\\Chrome WebDriver\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://toolsqa.com/iframe-practice-page/")
    driver.maximize_window()
    driver.switch_to.frame("iframe1") #frame name
    #driver.switch_to.frame("IF1") #frame id
    driver.find_element_by_xpath("//a[contains(text(),'Read More')]").click()

    #to switch out of the frame back to main screen
    driver.switch_to.default_content()
    driver.find_element_by_xpath("//span[text()='VIDEOS']").click()