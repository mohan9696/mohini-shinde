
import time
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome
driver.get("https://www.selenium.dev/")
time.sleep(5)  