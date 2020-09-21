from selenium import webdriver
import time


PATH = "/Users/liamcahill/Developer/chromedriver"

driver = webdriver.Chrome(PATH)	
driver.get("https://orteil.dashnet.org/cookieclicker/")



def getBigCookie():
	time.sleep(4)
	element = driver.find_element_by_id("bigCookie")
	#clickBigCookie(element, 10000)

def clickBigCookie(element, x):
	counter = 0

	while(counter < x):
		element.click()
		counter = counter + 1

	time.sleep(2)
	clickBigCookie(element, x)







	'''
	element = driver.find_element_by_id("product1")
	element.click()

	element = driver.find_element_by_id("product0")
	element.click()


	'''		
	

	#element = driver.find_element_by_id("product1")
	#element.click()


if __name__ == '__main__':
	getBigCookie()
