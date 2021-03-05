#!/usr/bin/env python

import yaml, os

#Resources used for this file included:
#https://stackoverflow.com/questions/1724693/find-a-file-in-python
#https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
#https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/

def main():
	grabbedFile = getYAML('mock1.yaml','.')
	#openYAML(grabbedFile)
	

	test_dictionary = [{'sports' : ['soccer', 'football', 'basketball', 'cricket', 'hockey', 'table tennis']}, 
	{'countries' : ['Pakistan', 'USA', 'India', 'China', 'Germany', 'France', 'Spain']}]

	writeToYAML(grabbedFile, test_dictionary)
	openYAML()

def reminder(text):
	#Using the colon in a print statement: a number before it means the colon ressembles the end of a word; when after it signifies front
	print(text[2:]) #prints am
	print(text[:2]) #prints li


def getYAML(name, path):
	for root, dirs, files in os.walk(path):
		if name in files:
			return os.path.join(root, name)

def openYAML():
	with open("mock1.yaml",'r') as stream:
		try:
			print(yaml.safe_load(stream))
		except yaml.YAMLError as exc:
			print(exc)
	return stream



def writeToYAML(file, dictionary):
	with open(file,'w') as currentFile:
		document = yaml.dump(dictionary, currentFile)


if __name__ == '__main__':
	main()
