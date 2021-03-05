#! /usr/bin/
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class Workout:
    def __init__(self, ):
        self.pushups = pushups
        self.situps = situps
        self.running = running


def grabber():
	score = []
	try:
		situps = int(input("How many situps did you do? "))
	try:
        pushups = int(input("How many pushups did you do? "))
    try:
        run = float(input("What was your run time? "))

	return scores

    

def getPushups(Workout):
    return Workout.pushups


def getSitups(Workout):
    return Workout.situps


def getRunning(Workout):
    return Workout.running


def enterAge():
    age = input("How older are you? ")
    try:
        age = int(age)
        return age
    except:
        print("Please enter a valid number.")
        enterAge()


def calculatePU_score(Workout):
    pu_percentage = Workout.pushups
    print(pu_percentage)


def score_search():

    PATH = "/Users/liamcahill/Developer/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get(
        "https://usarmybasic.com/army-physical-fitness/male-pushup-standards")


if __name__ == "__main__":

    initial_results = grabber()

    workout1 = Workout(initial_results)


# things to add:
# use VS code to get inputs for the three tests as raw scores
# hardcode standards, but brainstorm workarounds, long-term solution
