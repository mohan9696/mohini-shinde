import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver =webdriver.Chrome()
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2017/01/frames-in-selenium-webdriver.html")
at = driver.find_element(By.XPATH, "//button[normalize_space()='AutomationTool']")
act=ActionChains(driver)
act.move_to_element(act).perform()
time.sleep(10)
driver.find_element(By.XPATH,"//a[Test()='testNG']").click()
time.sleep(5)
driver.close()