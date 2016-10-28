from math import sqrt

def ColourDiff(tup1,tup2):
    
    r1,g1,b1 = tup1
    r2,g2,b2 = tup2
    rChange = (r1 - r2) ** 2
    gChange = (g1 - g2) ** 2
    bChange = (b1 - b2) ** 2
    rMean = (r1 + r2) // 2
    
    return int(round(sqrt((2 + rMean // 256 ) * rChange + 4 * gChange + (2 + (255 - rMean) // 256) * bChange)))

def DiffTable(tup):
    (lt1, lt2) = tup
    table = []
    
    for colour1 in lt1:
        row = []
        for colour2 in lt2:
            row += [ColourDiff(colour1, colour2)]
        table += [row]
    return table
