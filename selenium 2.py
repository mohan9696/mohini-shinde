from selenium import webdriver

driver = webdriver.Chrome(executable_path="file:///C:/Users/Admin/Downloads/Mohan%20shinde%20resume%2001.pdf//mohanshinderesume.txe")
driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element_by_name("_token")
driver.find_