lst1 = [7, 7, 7, 7]
lst2 = [7, 7, 7, 7]

#iLst1 = iter(lst1)
#iLst2 = iter(lst2)

s = zip(lst1, lst2)

itrLst1 = iter(lst1)
itrLst2 = iter(lst2)
print (lst1, lst2)
#i = next(itrLst1, -9999)
#j = next(itrLst2, -9999)

done_looping = False
while not done_looping:
    i = next(itrLst1, -999)
    j = next(itrLst2, -999)
    if (i == -999) and (j != -999):
        print ("ran out of i")
        done_looping = True
    elif (i != -999) and (j == -999):
        print ("ran out of j")
        done_looping = True
    elif (i == -999) and (j == -999):
        print ("both empty lists")
        done_looping = True
    else:
        print(i, j)
