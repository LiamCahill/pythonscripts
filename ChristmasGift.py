import yaml
import os


class gift:
    def __init__(self, gift_idea, gift_for, gift_from, gift_price, purchase_date):
        self.item = gift_idea
        self.receiver = gift_for
        self.giver = gift_from
        self.price = gift_price
        self.purchase_date = purchase_date

    def getIdea(self, gift):
        return gift.item

    def getPrice(self, gift):
        return gift.price

    def getReceiver(self, gift):
        return gift.receiver

    def getGiver(self, gift):
        return gift.giver

    def getPurchaseDate(self, gift):
        return gift.purchase_date

# This function will take in a gift object, and return a dictionary where [key, value] == [gift_receiver, gift_item]


def parseGift(gift):
    dictionary = []

    return dictionary


def writeToYAML(file, dictionary):
    with open(file, 'w') as currentFile:
        document = yaml.dump(dictionary, currentFile)


Regis_gift = gift('HDMI cord', "Regis", "Liam", "25", "12/7/2020")

parseGift(Regis_gift)
