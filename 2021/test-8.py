
sample = ['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb']

uniqDct = {2:1, 4:4, 3:7, 7:8}
itms = 'abcdefg'

sorSample = [''.join(sorted(i)) for i in sample]

for itms in sorSample:
    for keys in uniqDct.keys():
        if(len(itms) == keys):
        #print (itms)
            #sorStr.remove(itms)
            print ("removed item:", itms, "and returning: ", uniqDct[keys])
        #returnDct[itms] = uniqDct[keys]