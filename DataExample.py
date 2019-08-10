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
this will show you how to use python3.7+ data class
"""

# standard library imports
import random
import sys
try:
    from dataclasses import dataclass
except ImportError:
    msg1 = "sorry  your version of python is not high enough."
    print(msg1)
    print("python3.7 or higher is reqiured.")
    sys.exit(1)

# pip library imports

# custom library imports

@dataclass
class Cars:
    name: str
    color: str
    mpg: float
    cost: float
    tax_rate: float

    def total_cost(self):
        new_value = round(self.cost + (self.cost * self.tax_rate), 2)
        print(f'The cost with taxes for the {self.name} car will be ${new_value}.')


if __name__ == "__main__":
    # the first class
    p1 = Cars('camery', 'red', 40, 10000.00, .07)
    p2 = Cars('tesla', 'white', 0, 30000.00, .1)
    p1.total_cost()
    p2.total_cost()
