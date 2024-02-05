from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=Service(executable_path="chromedriver.exe"))

driver.get("https://www.google.com/")

input_element=driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.send_keys("EPI"+Keys.ENTER)

time.sleep(15)
driver.quit()