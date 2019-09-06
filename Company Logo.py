#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


if __name__ == '__main__':
    s = input()
    c = Counter(sorted(s))
    [print(k,v) for k,v in c.most_common(3)]
    #print(c.most_common(3))

