import sys
import os
import argparse
import gtrs

def main():
    """
    main function
    """
    # parse options and arguments
    parser = argparse.ArgumentParser(description='This geophysics treature(gtrs)')
    parser.add_argument('-c', '--command', type=str,
                        default ='foo',
                        help='command given to the package')
    # only one argument
    arg = parser.parse_args()
    # todo
    if arg.command == 'foo':
        usage()

def usage():
    pass


if __name__ == "__main__":
    main()