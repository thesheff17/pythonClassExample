#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019, Dan Sheffner 
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.


"""
example of how to use argparse in python

provide examples on how to run the script:
./Argexample.py --upper 10
"""

# standard library imports
import argparse
import random

# pip library imports

# custom library imports


class Argexample:
    """
    what does your class do?
    """

    version = '0.1'

    def __init__(self, upper_range):
        """
        comments
        """
    
        self.upper_range = upper_range
        self.rand_num = random.randrange(upper_range)

    def do_something(self):
        """
        comments
        """

        print (f'the upper range variable is: {self.upper_range}')
        print (f'the random number is: {self.rand_num}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--upper", help = "the upper number on the random number threshold", 
                        type = int)
    args = parser.parse_args()

    # pass the args.upper to the constructor
    p1 = Argexample(args.upper)
    p1.do_something()

