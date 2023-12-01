import os
import itertools
import re
import numpy as np
from itertools import cycle
import math

#f = open("input13-test.txt", "r")
f = open("input13.txt", "r")

#remove new line chars
temp = f.read().splitlines()