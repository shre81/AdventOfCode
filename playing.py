import os
import re
import numpy as np

sampleDct = {232: {'eyr': '2021', 'iyr': '2017', 'pid': '717543257', 'ecl': 'hzl', 'cid': '144', 'hgt': '161cm', 'hcl': '#49a793', 'byr': '1966'}, 
233: {'eyr': '2025', 'ecl': 'brn', 'pid': '391973520', 'iyr': '2012', 'cid': '77', 'hgt': '60in', 'hcl': '#602927', 'byr': '1928'}, 
234: {'pid': '784483994', 'iyr': '2013', 'ecl': 'grn', 'hgt': '161cm', 'eyr': '2024', 'hcl': '#cfa07d', 'byr': '1991'}, 
237: {'eyr': '2029', 'iyr': '2010', 'pid': '572128647', 'ecl': 'gry', 'byr': '1996', 'hcl': '#623a2f', 'hgt': '152cm'}, 
239: {'eyr': '2029', 'pid': '233353682', 'iyr': '2011', 'ecl': 'gry', 'byr': '1968', 'hcl': '#efcc98', 'hgt': '181cm'}, 
243: {'ecl': 'hzl', 'eyr': '2024', 'pid': '537492791', 'iyr': '2020', 'hgt': '186cm', 'hcl': '#cfa07d', 'byr': '1952'}, 
247: {'pid': '904825661', 'iyr': '2010', 'ecl': 'oth', 'byr': '1923', 'eyr': '2020', 'hcl': '#b6652a', 'hgt': '70in'}, 
249: {'ecl': 'amb', 'iyr': '2016', 'pid': '613754206', 'hgt': '164cm', 'eyr': '2025', 'hcl': '#18171d', 'byr': '1975'}, 
250: {'eyr': '2027', 'iyr': '2017', 'pid': '287108745', 'ecl': 'amb', 'cid': '191', 'hgt': '174cm', 'hcl': '#623a2f', 'byr': '1938'}, 
252: {'ecl': 'amb', 'eyr': '2025', 'pid': '506927066', 'iyr': '2018', 'cid': '93', 'hgt': '177cm', 'hcl': '#b6a3ce', 'byr': '1967'}, 
253: {'eyr': '2030', 'pid': '587635596', 'iyr': '2012', 'ecl': 'hzl', 'cid': '106', 'byr': '1964', 'hcl': '#fb5993', 'hgt': '173cm'}}


lst_of_valid_keys = ['pid', 'ecl', 'hcl', 'byr', 'eyr', 'iyr', 'hgt']
validLst2 = []

for k,v in sampleDct.items():
    byrValid = 0
    iyrValid = 0
    eyrValid = 0
    hgtValid = 0
    hclValid = 0
    eclValid = 0
    pidValid = 0
    keysOfInt = list(v.keys())
    if set(lst_of_valid_keys).issubset(set(keysOfInt)):
        print (int(v['byr']), int(v['iyr']), int(v['eyr']), v['hgt'], v['hcl'], v['ecl'], v['pid'])
        if (int(v['byr']) >= 1920) and (int(v['byr']) <= 2002):
            byrValid = 1
            print('byr valid')
        if (int(v['iyr']) >= 2010) and (int(v['iyr']) <= 2020):
            iyrValid = 1
            print('iyr valid')
        if (int(v['eyr']) >= 2020) and (int(v['eyr']) <= 2030):
            eyrValid = 1
            print('eyr valid')
        if v['hgt'][-2:] == 'cm':
            if (int(v['hgt'][0:-2]) >= 150) and (int(v['hgt'][0:-2]) <= 193):
                hgtValid = 1
                print('hgt valid')

        elif v['hgt'][-2:] == 'in':
            if (int(v['hgt'][0:-2]) >= 59) and (int(v['hgt'][0:-2]) <= 76):
                hgtValid = 1
                print('hgt valid')
       
        regex = r"^#([a-f]|[\d]){6}"
        matches = re.match(regex, v['hcl'], re.MULTILINE)
        
        if matches is None:
            hclValid = 0
        else:
            hclValid = 1
            print('hcl valid')
        
        if v['ecl'] in ['amb', 'blu' ,'brn' ,'gry' ,'grn' ,'hzl', 'oth']:
            eclValid = 1
            print('ecl valid')
        else:
            eclValid = 0
        
        regStr = r"\d{9}"
        m = re.match(regStr, v['pid'])
        #print(m, v['pid'])
        
        if m is None:
            pidValid = 0
        else:
            pidValid = 1
            print('pid valid')

        if (pidValid == 1) and (eclValid == 1) and (hclValid == 1) and (hgtValid == 1) and (eyrValid == 1) and (iyrValid == 1) and (byrValid == 1):
            validLst2.append(k)


print (len(validLst2))
            