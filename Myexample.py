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
what does your program do?
"""

# standard library imports
import random

# pip library imports

# custom library imports


class Myexample:
    """
    what does your class do?
    """

    version = '0.1'

    def __init__(self):
        """
            comments
        """
        print ("ran the constructor...")

    def do_something(self):
        """
        comments
        """

        print ("ran the do_something method()...")

    def use_rando(self, amount):
        """
        example of a method that takes in an integer.

        :type name: int
        :param name: the random number to make a value up to
        """

        # get a random number
        random_value = random.randrange(0,amount)

        # example of using f string
        print (f'random number between 0 and : {amount}: {random_value}')
        return random_value

    def second_rando(self):
        """
        do something else with a random number and 
        example of calling a method inside your own class.
        """

        output = self.use_rando(5)

        # example of re using a variable name in a different method.  Since it is in a different
        # method the scope do not collide.

        print (f'The random number: {output} multiplied by 5 is: {output * 5}')
        # print (statement)


if __name__ == "__main__":
    # the first class
    p1 = Myexample()
    p1.do_something()
    p1.use_rando(5)
    p1.second_rando()
