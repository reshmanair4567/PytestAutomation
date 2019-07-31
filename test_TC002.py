from selenium.webdriver import Chrome
import pytest


@pytest.mark.Sanity
def test():
    path = "C:\\Users\\User\\Desktop\\Chrome WebDriver\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://naukri.com")
    driver.maximize_window()
    Allwindow=driver.window_handles
    print(Allwindow)
    mainWin=""


    ### Multi Window Handling - Windows
    for win in Allwindow:
        driver.switch_to.window(win)
        print(driver.current_url)
        if(driver.current_url)=="https://www.naukri.com/":
            print("This is my main window")
            mainWin=win
        else:
            driver.close()
    driver.switch_to.window(mainWin) # we need to take the control back from the last window that was closed
    print(driver.current_url)


    driver.close()