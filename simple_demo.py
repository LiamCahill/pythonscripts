'''
A simple Gooey example. One required field, one optional.
'''

from gooey import Gooey, GooeyParser


@Gooey()
def main():
    parser = GooeyParser(description='Process some integers.')

    parser.add_argument(
        'required_field',
        metavar='Some Field',
        help='Enter some text!')

    parser.add_argument(
        '-f', '--foo',
        metavar='Some Flag',
        action='store_true',
        help='I turn things on and off')

    parser.add_argument(
        'test',
        metavar = 'myTest',
        action = 'store'
        )

    parser.add_argument(
        'numbers',
        metavar = 'myCount',
        action = 'count'
        )

    args = parser.parse_args()
    print('Hooray!')

    print('You entered ' + args.test)
   

if __name__ == '__main__':
    main()