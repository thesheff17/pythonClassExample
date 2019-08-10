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
This will show you how to use to read an ini file
"""

# standard library imports
import random
import sys
from dataclasses import dataclass
from configparser import ConfigParser
import codecs

# pip library imports

# custom library imports

@dataclass
class Cars:
    name: str
    color: str
    mpg: float
    cost: float
    tax_rate: float
    doors: int

    def total_cost(self):
        new_value = self.cost + (self.cost * self.tax_rate)
        print(f'The cost with taxes for the {self.name} car will be ${new_value}.')
        print(f'The car has {self.doors} doors.')


if __name__ == "__main__":

    parser = ConfigParser()
    with codecs.open('cars.ini', 'r', encoding='utf-8') as f:
        parser.read_file(f)

    # print all headers:
    for section_name in parser.sections():
        print(section_name)

    # a list of objects
    my_list = [] 
    for section in parser.sections():

        # the section 'doors' has a DEFAULT value. This way if most of the values are the same
        # you can set a default value.  Then where its different you can overwrite it. 
        # see corvette for overwrite
        p1 = Cars(section, parser.get(section, 'color'), parser.getfloat(section, 'mpg'),
                  parser.getfloat(section, 'cost'), parser.getfloat(section, 'tax_rate'),
                  parser.getint(section, 'doors'))
        my_list.append(p1)

    # loop through objects and get total costs of each car:
    for each in my_list:
        each.total_cost()
