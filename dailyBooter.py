import subprocess

def startApplications():
	subprocess.call(['open /Applications/iTerm.app', '-l'], shell = True)
	subprocess.call(['open /Applications/UlyssesMac.app', '-l'], shell = True)

def main():
	startApplications()
	

if __name__ == '__main__':
	main()