import argparse
from gooey import Gooey
from functools import reduce

@Gooey
def main():
    parser = argparse.ArgumentParser(description='Do stuff with numbers.')
    parser.add_argument('-a','--add', help='Add numbers together', required=False, nargs='+')
    parser.add_argument('-m','--multiply', help='Multiply numbers together', required=False, nargs='+')

    args = vars(parser.parse_args())

    if args['add']:
        # did it on one-line to save space
        print(sum(list(map(int, args['add']))))

    if args['multiply']:
        # did it one one-line to save space
        print(reduce(lambda a, b: a * b, list(map(int, args['multiply']))))
        

if __name__ == '__main__':
    main()