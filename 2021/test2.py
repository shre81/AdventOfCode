def (tuplPair, linTyp):
    # linTyp can be of 4 types - 'h' - horizontal line, x is constant
    #                          -  'v' - vertical line, y is constant
    #                          - 'dd' - differing diagonal, downward slope
    #                          - 'sd' - increasing diagonal, upward slope
    if linTyp == 'h':
        xFac = 0
        yFac = +1
    elif linTyp == 'v':
        xFac = +1
        yFac = 0
    elif linTyp == 'dd':
        xFac = +1
        yFac = -1
    else:
        xFac = +1
        yFac = +1
    
    if linTyp in ('h'):
        for dist in range(0, abs(tuplPair[1][1]-tuplPair[0][1])):
            if (tuplPair[1][1]-tuplPair[0][1]) < 0:
                tmpXIndx = tuplPair[0][0] + xFac
                tmpYIndx = tuplPair[0][1] + yFac * dist
                fldArr[]
            elif (tuplPair[1][1]-tuplPair[0][1]) > 0:
                tmpXIndx = tuplPair[0][0] + xFac
                tmpYIndx = tuplPair[0][1] + -1*yFac * dist
            else:
                break