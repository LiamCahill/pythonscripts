from gooey import Gooey, GooeyParser

@Gooey
def main():
  parser = GooeyParser(description="My Cool GUI Program!")
  parser.add_argument('Filename', widget="FileChooser")
  myFile = input("What is your file path?\n")

if __name__ == '__main__':
	main()