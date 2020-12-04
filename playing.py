import os
import re
import numpy as np

f = open("input3.txt", "r")

temp = f.read().splitlines()

#print(type(temp))

#print (temp[0:50])

#someTupleLst = [(53, 269), (282, 40), (52, 254), (42, 176), (22, 139)]
someTupleLst = [(53, 269), (282, 40), (54, 268), (54, 268), (22, 139)]
product = 1
for items in someTupleLst:
    product = product * items[0]

print (product)
print (53*282*52*42*22)