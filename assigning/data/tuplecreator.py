from random import choice

def MaketheList(N):
    lst = []
    for _ in range(N):
        x = choice(range(256))
        y = choice(range(256))
        z = choice(range(256))
        lst += [(x,y,z)]
    return lst
    
def MakeTheTuple(N):
    return(MakeTheList(N), MakeTheList(N))
