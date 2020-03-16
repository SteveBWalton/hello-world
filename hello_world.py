#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Program to print hello world.
'''

# System libraries.
import argparse

# Application libraries.


if __name__ == '__main__':
    # Process the command line arguments.
    # This might end the program (--help).
    argParse = argparse.ArgumentParser(prog='hello_world', description='Display hello world.')
    args = argParse.parse_args()

    # Welcome message.
    print('Hello World')
