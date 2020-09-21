#! /usr/bin/
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

booklist = []
PATH = "/Users/liamcahill/Developer/chromedriver"

def nextBook():
	file1 = open('bookList.txt','r')
	
	for line in file1:
		print(line)
		booklist.append(line.strip())
	

def bookSeach():

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

if __name__ == '__main__':
	nextBook()
	bookSeach()
