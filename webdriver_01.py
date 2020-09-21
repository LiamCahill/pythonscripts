#! /usr/bin/env

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/liamcahill/Developer/chromedriver"

booklist = ["Maps of Meaning", "Harry Potter", "The War on the Cops"]

driver = webdriver.Chrome(PATH)	
driver.get("https://www.amazon.com")
print(driver.title)
	
for book in booklist:
	element = driver.find_element_by_id("twotabsearchtextbox")
	element.clear()
	element.send_keys(book)
	element.send_keys(Keys.RETURN)
	time.sleep(3)


driver.quit()

#print("John 8:32")
