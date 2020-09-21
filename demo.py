#!/usr/bin/env python3
import re


def main():
    #print("Hello")

    name = input("Please input your name. ")
    print(len(name))
    
    name_test(name)

def name_test(string):

    if re.match("^[a-zA-Z0-9_]*$", string):
        return True
    else: return False 

if __name__ == "__main__":
    main()
    