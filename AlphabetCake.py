#!python

TESTFILE = r"A-small-practice.in"

class GridSquare:
    def __init__(self,letter,x,y):
        self.letter = letter
        self.x = x
        self.y = y
    def __repr__(self):
        return str(self.letter)
    def __mul__(self,other): #returns the area of cake taken up by the two points
        return (abs(self.x-other.x)+1)*(abs(self.y-other.y)+1)
    def isQuestion(self):
        return self.letter == "?"
    def all(self):
        return "{} {} {}".format(self.letter,str(self.x),str(self.y))
def genCakes(fName):
    with open(fName) as f:
        NUMCAKES = int(f.readline())
        for i in range(NUMCAKES):
            numRows, numCols = f.readline().split(" ")
            yield [[GridSquare(letter,x,y) for y,letter in enumerate(f.readline()[:-1])]\
                   for x in range(int(numRows))]

def findLetters(cake):
    return [cake[x][y] for x,line in enumerate(cake)\
            for y,letter in enumerate(line) if not letter.isQuestion()]
def findUpmost(gs,cake):
    for sub,row in enumerate(reversed(cake[:gs.x])):
        if not row[gs.y].isQuestion():
            return gs.x-sub
    return 0 #Ran off the top
def findLeftmost(gs,cake):
    for sub,letter in enumerate(reversed(cake[gs.x][:gs.y])):
        if not letter.isQuestion():
            return gs.y-sub
    return 0 #Ran off the left
def findBottommost(gs,cake):
    for add,row in enumerate(cake[gs.x+1:]):
        if not row[gs.y].isQuestion():
            return gs.x+add
    return len(cake)-1 #Ran off the bottom
def findRightmost(gs,cake):
    for add,letter in enumerate(cake[gs.x][gs.y+1:]):
        if not letter.isQuestion():
            return gs.y+add
    return len(cake[gs.x])-1 #Ran off the right
def findUpperCorner(gs,cake):
    up = findUpmost(gs,cake)
    if up == gs.x:
        return gs
    biggest = gs
    biggestArea = 1
    leftest = 0
    for sub,row in enumerate(reversed(cake[up:gs.x+1])):
        left = row[findLeftmost(row[gs.y],cake)]
        if left.y < leftest:
            left = row[leftest]
        else:
            leftest = left.y
        area = gs * left
        if area > biggestArea:
            biggestArea = area
            biggest = left
    rightest = len(cake[0])-1
    for sub,row in enumerate(reversed(cake[up:gs.x+1])):
        right = row[findRightmost(row[gs.y],cake)]
        if right.y >= rightest:
            right = row[rightest]
        else:
            rightest = right.y
        area = gs * right
        if area > biggestArea:
            biggestArea = area
            biggest = right
    return biggest
    

cakeNum = 0
for cake in genCakes(TESTFILE):
    cakeNum += 1
    if cakeNum > 5:
        break
    print("Case #{}:".format(cakeNum))
    for l in findLetters(cake):
        print("{}: UP:{} DOWN:{} RIGHT:{} LEFT:{} UPPERCORNER:{} UPPER AREA:{}"\
              .format(l.all(),findUpmost(l,cake),findBottommost(l,cake),\
                      findRightmost(l,cake),findLeftmost(l,cake),\
                      findUpperCorner(l,cake).all(),findUpperCorner(l,cake)*l))
    for line in cake:
        print("".join(map(str,line)))
