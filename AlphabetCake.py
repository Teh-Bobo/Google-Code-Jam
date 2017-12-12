#!python

TESTFILE = r"A-small-practice.in"

class GridSquare:
    def __init__(self,letter,x,y):
        self.letter = letter
        self.x = x
        self.y = y
    def __repr__(self):
        return "{} {} {}".format(self.letter,str(self.x),str(self.y))
def genCakes(fName):
    with open(fName) as f:
        NUMCAKES = int(f.readline())
        for i in range(NUMCAKES):
            numRows, numCols = f.readline().split(" ")
            yield [list(f.readline())[:-1] for x in range(int(numRows))]

def findLetters(cake):
    return [GridSquare(letter,x,y) for x,line in enumerate(cake)\
            for y,letter in enumerate(line) if letter != "?"]
def findUpmost(gs,cake):
    for sub,row in enumerate(reversed(cake[:gs.x])):
        if row[gs.y] != "?":
            return gs.x-sub
    return 0 #Ran off the top
def findBottommost(gs,cake):
    for sub,row in enumerate(cake[gs.x:]):
        if row[gs.y] != "?":
            return gs.x+sub
    return len(cake) #Ran off the bottom

cakeNum = 0
for cake in genCakes(TESTFILE):
    cakeNum += 1
    if cakeNum > 5:
        break
    print("Case #{}:".format(cakeNum))
    for l in findLetters(cake):
        print("{}: UP:{} DOWN:{}".format(l,findUpmost(l,cake),findBottommost(l,cake)))
    for line in cake:
        print("".join(line))
