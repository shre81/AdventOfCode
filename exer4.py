import os
import itertools
import re
import numpy as np

f = open("input4.txt", "r")

#remove new line chars
temp = f.read().split("\n\n")

sample = temp[0]

test = sample.split("\n")
test2 = test[0].split(" ")
#print (test2)

itemsDct = {}
charsOI = ['\n', ' ']

sample2 = temp[25]
print (sample2)

sample3 = sample2.replace("\n", " ")

lst_of_str = sample3.split()

print (lst_of_str)

samDct = {}
for items in lst_of_str:
    twoStr = items.split(":")
    samDct[twoStr[0]] = twoStr[1]

print (samDct)

masterDct = {}
for idx,items in enumerate(temp): #parse through the 260 item list
    lst_of_str = (items.replace("\n", " ")).split()
    strDct = {}
    for strs in lst_of_str:
        twoStr = strs.split(":")
        strDct[twoStr[0]] = twoStr[1]
    masterDct[idx] = strDct

lst_of_valid_keys = ['pid', 'ecl', 'hcl', 'byr', 'eyr', 'iyr', 'hgt']
validLst = []

for k,v in masterDct.items():
    keysOfInt = list(v.keys())
    if set(lst_of_valid_keys).issubset(set(keysOfInt)):
        validLst.append(k)

print (len(validLst)) #Right answer: 222

#Part 2

lst_of_valid_keys = ['pid', 'ecl', 'hcl', 'byr', 'eyr', 'iyr', 'hgt']
validDct2 = {}
invalidDct = {}

for k,v in masterDct.items():
    byrValid = 0
    iyrValid = 0
    eyrValid = 0
    hgtValid = 0
    hclValid = 0
    eclValid = 0
    pidValid = 0
    keysOfInt = list(v.keys())
    if set(lst_of_valid_keys).issubset(set(keysOfInt)):
        if (int(v['byr']) >= 1920) and (int(v['byr']) <= 2002):
            byrValid = 1
        if (int(v['iyr']) >= 2010) and (int(v['iyr']) <= 2020):
            iyrValid = 1
        if (int(v['eyr']) >= 2020) and (int(v['eyr']) <= 2030):
            eyrValid = 1
        if v['hgt'][-2:] == 'cm':
            if (int(v['hgt'][0:-2]) >= 150) and (int(v['hgt'][0:-2]) <= 193):
                hgtValid = 1
        elif v['hgt'][-2:] == 'in':
            if (int(v['hgt'][0:-2]) >= 59) and (int(v['hgt'][0:-2]) <= 76):
                hgtValid = 1
       
        regex = r"^#([a-f]|[\d]){6}"
        matches = re.match(regex, v['hcl'], re.MULTILINE)
        
        if matches is None:
            hclValid = 0
        else:
            hclValid = 1
        
        if v['ecl'] in ['amb', 'blu' ,'brn' ,'gry' ,'grn' ,'hzl', 'oth']:
            eclValid = 1
        else:
            eclValid = 0
        
        regStr = r"\b\d{9}\b" #This is where i got stuck! 
        m = re.match(regStr, v['pid'])
        if m is None:
            pidValid = 0
        else:
            pidValid = 1

        if (pidValid == 1) and (eclValid == 1) and (hclValid == 1) and (hgtValid == 1) and (eyrValid == 1) and (iyrValid == 1) and (byrValid == 1):
            validDct2[k] = v
        else:
            invalidDct[k] = v


print (len(validDct2), len(invalidDct))

            