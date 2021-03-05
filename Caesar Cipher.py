#Adapted by Liam Cahill from 
#Cracking Codes with Python(No Starch Press) to use functions.

message = "This is a test message."

key = 20

mode = 'encrypt'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'

translated = ''

def getSymbolIndex(symbol):
	symbolIndex = SYMBOLS.find(symbol)
	return symbolIndex

def encryptMessage(symbolIndex):
	translatedIndex = symbolIndex + key
	return translatedIndex

def decryptMessage(symbolIndex):
	translatedIndex = symbolIndex - key
	return translatedIndex

def wrapAroundGreaterE(translatedIndex):
	translatedIndex = translatedIndex - len(SYMBOLS)
	return translatedIndex

def wrapAroundLess(translatedIndex):
	translatedIndex = translatedIndex + len(SYMBOLS)
	return translatedIndex




for symbol in message:

	if symbol in SYMBOLS:
		symbolIndex = getSymbolIndex(symbol)

		if mode == 'encrypt':			
			translatedIndex = encryptMessage(symbolIndex)
		elif mode == "decrypt":
			translatedIndex = decryptMessage(symbolIndex)

		if translatedIndex >= len(SYMBOLS):
			translatedIndex = wrapAroundGreaterE(translatedIndex)
		elif translatedIndex < 0:
			translatedIndex = wrapAroundLess(translatedIndex)

		translated = translated + SYMBOLS[translatedIndex]
	else: 
		translated = translated + symbol


#print(translated)

if __name__ == '__main__':
	print(getSymbolIndex(''))