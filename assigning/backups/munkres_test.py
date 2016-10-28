from munkres import Munkres
from ColourCost import *

# returns the list of tuples [(row,col), (row,col)] of the matching
def Final(tup):
    inputtable = DiffTable(tup)
    m = Munkres()
    return m.compute(inputtable)
    
