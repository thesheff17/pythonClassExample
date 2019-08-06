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
example on how to use pyyaml
https://pyyaml.org/wiki/PyYAMLDocumentation
"""

# standard library imports
import __main__ as main
import random
import logging

# automatically detect file name being called
fileName = main.__file__
fileName = fileName.replace("./", "")
fileName = fileName.replace(".py", "")
fileName = fileName + ".log"

# logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
while len(logger.handlers) > 0:
    del logger.handlers[0]
ch = logging.FileHandler(fileName)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s \
                              - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
logger.addHandler(ch)

# pip library imports
# you will get a warning about load being depcrecated and use safe_load
# you have to trust your yaml and I want this to work with the c library LibYAML
# https://pyyaml.org/wiki/LibYAML

# error I'm scripting around: YAMLLoadWarning: calling yaml.load() without Loader=... is 
# deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load 
# for full details.

from yaml import load, YAMLError
try:
    from yaml import CLoader as Loader
    logging.info('loaded the c yaml library')
except ImportError:
    from yaml import Loader, warnings
    warnings({'YAMLLoadWarning': False})
    logging.info('loaded the python yaml library')

# custom library imports

class Yamlexample:
    """
    what does your class do?
    """

    version = '0.1'

    def __init__(self):
        """
        comments
        """

        with open("stuff.yaml", 'r') as stream:
            try:
                self.data = load(stream, Loader=Loader)
            except YAMLError as exc:
                print(exc)
 
        print ("ran the constructor...")

    def do_something(self):
        """
        comments
        """

        print ()
        print (self.data)

        print (f'upper threshold {self.data["upper"]}')

        randnum = random.randrange(0, self.data["upper"])
        print (f'random number: {randnum}')

        print ("ran the do_something method()...")

    def get_house_items(self):
        """
        this will print out the house items
        """

        print ()

        # this returns a list
        for item in self.data['house']:
            print (f'an item in the house {item}')

    def load_in_line(self):
        cars = load("""
                      - tesla
                      - ford
                      - chevy
                      - toyota
                      - honda
                    """) 

        print ()
        print ("car types:")
        for car in cars:
            print (car)

if __name__ == "__main__":
    # the first class
    p1 = Yamlexample()
    p1.do_something()
    p1.get_house_items()
    p1.load_in_line()
