from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/liamcahill/Developer/chromedriver"

driver = webdriver.Chrome(PATH)	
driver.get("https://www.google.com")
print(driver.title)


#element = driver.find_element_by_id("q")

time.sleep(5)
driver.quit 