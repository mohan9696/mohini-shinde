import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=god+songs")
driver.maximize_window()
time.sleep(2)