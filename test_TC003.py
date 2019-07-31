from selenium.webdriver import Chrome

path = "C:\\Users\\User\\Desktop\\Chrome WebDriver\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("http://thetestingworld.com/testings/")
driver.maximize_window()
mainWin=""
driver.find_element_by_xpath("//label[text()='Login']").click()
driver.find_element_by_name("_txtUserName").send_keys("test")
driver.find_element_by_name("_txtPassword").send_keys("test")
driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Delete')]").click()

### Multi Window Handling - Tabs
allTabs=driver.window_handles
print(allTabs)
for tab in allTabs:
    driver.switch_to.window(tab)
    print(driver.current_url)
    if (driver.current_url=="http://thetestingworld.com/testings/manage_customer.php"):
        driver.find_element_by_xpath("//button[text()='Start Download']").click()



driver.close()