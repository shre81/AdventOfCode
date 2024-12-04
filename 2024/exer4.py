import os
import numpy as np

f = open("input4.txt", "r")
#f = open("input4-test.txt", "r")

allLst = f.read().splitlines()

print (allLst[0][0])

xd = len(allLst)
yd = len(allLst[0])

print (xd, yd)

#def strParser(lst_of_str, i, j):

'''
#part 1
xmas = 0
testStr = []
for x in range(0,xd):
    for y in range(0, yd):
        if (allLst[x][y] == 'X'):
            testStr.append(allLst[x][y])
            for i in range(-1,2):
                for j in range(-1,2):
                    if ( 0 <= (x+i) < xd) and (0 <= (y+j) < yd):
                        if (allLst[x+i][y+j] == 'M'):
                            testStr.append(allLst[x+i][y+j])
                        
                            nx = x+i
                            ny = y+j
                            #print ('X was at: ', x, y, ' and found M at: ', nx, ny)

                            # check for a here

                            ax = nx + i
                            ay = ny + j

                            sx = ax + i
                            sy = ay + j

                            if (0 <= ax < xd) and (0 <= ay < yd):
                                if (allLst[ax][ay]=='A'):
                                    #print ('found A at :', ax, ay)
                                    if (0 <= sx < xd) and (0 <= sy < yd):
                                        if (allLst[sx][sy]=='S'):
                                            #print ('found S at : ', sx, sy)
                                            xmas = xmas +1
                        
                        for a in range(-1,2):
                            for b in range(-1,2):
                                if (((nx+a) >= xd) or (ny + b) >= yd):
                                    continue
                                elif (allLst[nx+a][ny+b]=='A'):
                                    testStr.append(allLst[nx+a][ny+b])
                                    mx = nx + a
                                    my = ny + b
                                    for c in range(-1,2):
                                        for d in range(-1,2):
                                            if (((mx+c) >= xd) or (my + d) >= yd):
                                                continue
                                            elif (allLst[mx+c][my+d]=='S'):
                                                testStr.append(allLst[mx+c][my+d])
                                                #print (allLst[mx+c][my+d])
                                                px = mx + c
                                                py = my + d
                                                xmas = xmas + 1
                                                break
'''    

#print (xmas)
#print (testStr)



#fullTxt = ''.join(testStr)

#print (fullTxt)

#print (fullTxt.count("XMAS"))

#part 2

xmas = 0
testStr = []

foundX = 0
allMat = []

for x in range(0,xd):
    for y in range(0, yd):
        if (allLst[x][y] == 'A'):

            lud  = (x-1, y-1)#left upper diagonal
            rld = (x+1, y+1) #right lower diagonal

            lld  = (x+1, y-1) #left lower diagonal
            rud  = (x-1, y+1) #right upper diagonal

            #print ("indices are: ", x , y, lud, rld, lld, rud)

            
            if all ([ 0 <= lud[0] < xd, 0 <= lud[1] < yd, 0 <= rld[0] < xd, 0 <= rld[1] < yd, 0 <= lld[0] < xd , 0 <= lld[1] <yd, 0 <= rud[0] < xd, 0 <= rud[1] < yd] ):

                try:

                    if ((allLst[lud[0]][lud[1]]== 'M') and (allLst[rld[0]][rld[1]]== 'S')) or ((allLst[lud[0]][lud[1]]== 'S') and (allLst[rld[0]][rld[1]]== 'M')):
                        if ((allLst[lld[0]][lld[1]]== 'M') and (allLst[rud[0]][rud[1]]== 'S')) or ((allLst[lld[0]][lld[1]]== 'S') and (allLst[rud[0]][rud[1]]== 'M')):
                            foundX = foundX + 1
                            newLst=[allLst[lud[0]][lud[1]], allLst[x][y], allLst[rld[0]][rld[1]], allLst[lld[0]][lld[1]], allLst[x][y], allLst[rud[0]][rud[1]]]
                            #print ("new list is:" , ''.join(newLst))
                            if 'SAS' in ''.join(newLst):
                                print ("not a right match")
                            allMat.append(''.join(newLst))

                except:
                    #print ("Out of bouunds at values: ", lud, rld, lld, rud)
                    break

print (foundX)
#print (allMat)
print (len(allMat))