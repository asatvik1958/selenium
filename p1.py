from selenium import webdriver
from selenium.webdriver.chrome.options import Options
'''
options = Options()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(executable_path="C:\AAS\PROGRAMMING\Selenium\chromedriver_win32\chromedriver.exe",options=options)
'''
options = Options()

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Edge(executable_path="C:\AAS\PROGRAMMING\Selenium\edgedriver_win64\msedgedriver.exe",options=options)
driver.get("https://github.com/mozilla/geckodriver/releases")