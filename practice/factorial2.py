import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
time.sleep(2)
#driver.find_element(By.ID,'smallsearchterms').send_keys('Lenovo')
#driver.find_element(By.NAME,'q').send_keys('Lenovo')
#driver.find_element(By.XPATH,"//button[@class='button-1 searchbox-button']").click()
#driver.find_element(By.LINK_TEXT,'Register').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Reg').click()
time.sleep(3)
driver.close()
