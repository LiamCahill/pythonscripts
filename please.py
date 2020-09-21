#print("Hello")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/liamcahill/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

username = "liamcahill"
password = "ciamlahill"

driver.get("https://play.pocketcasts.com/user/login")
print(driver.find_element_by_name("Email"))

#email = driver.find_element_by_name("Email")
#email.send_keys("test")
#email.send_keys(Keys.RETURN) 



#driver.quit()