
def myName(name):
	print("Hello, " + name + ". How are you today?")


def favoriteTeam(team):
	print("Glad to see " + team + " is your favorite!")

def idSide(a,b,c):
	if(a == False):
		#This means we know sides b,c
		multThis()
	elif(b == False):
		multThis()
	else:
		multThis()

def multThis(x,y,z):
	product = x*y*z
	return product

def termtest():
	subprocess.call("ls")
	time.sleep(2)

	rand = random.randint(0,5)
	print(rand)

def roll():
	rolls = 0
	while True:

		dice1 = random.randint(0,100)
		dice2 = random.randint(0,100)
		rolls += 1
		print(dice1, dice2)
		time.sleep(.5)

		if(dice1 == dice2):
			return False