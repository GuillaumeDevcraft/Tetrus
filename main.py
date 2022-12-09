# coding=utf8

from math import *

# formes t=tous c=cercle l=losange
tl = [[0, 0, 0, 0],
      [0, 0, 0, 0],
      [1, 0, 0, 0],
      [1, 1, 0, 0]]
tL = [[0, 0, 0, 0],
      [1, 0, 0, 0],
      [1, 0, 0, 0],
      [1, 1, 0, 0]]
tT = [[0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 1, 0, 0],
      [1, 1, 1, 0]]
tStair = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 0, 0],
          [0, 1, 1, 0]]
tDot = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0]]
tSquare = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [1, 1, 0, 0],
           [1, 1, 0, 0]]
tLine = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [1, 1, 1, 1]]
cSquare = [[0, 0, 0, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 1, 1, 1, 0],
           [1, 1, 1, 1, 0],
           [1, 1, 1, 1, 0]]
cCircle = [[0, 0, 0, 0, 0],
           [0, 1, 1, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 1, 1, 1, 0],
           [0, 1, 1, 0, 0]]
cL = [[0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0],
      [0, 0, 0, 1, 0],
      [0, 0, 0, 1, 0],
      [1, 1, 1, 1, 0]]
cRectangle = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [1, 1, 1, 1, 0],
              [1, 1, 1, 1, 0]]
cU = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [1, 0, 0, 0, 1],
      [1, 1, 1, 1, 1]]
cLine = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1]]
cll = [[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 0, 0, 0, 1],
       [1, 1, 1, 1, 1]]
cu = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [1, 0, 0, 1, 0],
      [1, 0, 0, 1, 0],
      [1, 1, 1, 1, 0]]
cG = [[0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 0, 0, 1, 0],
      [1, 1, 1, 1, 0]]
cBottle = [[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 1, 1, 0, 0]]
lStairs = [[0, 0, 0, 0, 0],
           [0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 0, 0, 0, 0]]
lT = [[0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 1, 1, 1, 0],
      [1, 1, 1, 1, 0],
      [1, 0, 0, 0, 0]]
lline = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1]]
lt = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 1, 1, 0, 0],
      [1, 0, 0, 0, 0]]
lTriangle = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 1, 1, 1, 0],
             [1, 1, 1, 1, 1]]
lSquare = [[0, 0, 0, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 1, 1, 1, 0],
           [1, 1, 1, 1, 0],
           [1, 1, 1, 1, 0]]
lx = [[0, 0, 0, 0, 0],
      [1, 0, 0, 1, 0],
      [0, 1, 1, 0, 0],
      [0, 1, 1, 0, 0],
      [1, 0, 0, 1, 0]]
ll = [[0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [1, 1, 1, 1, 0],
      [0, 0, 0, 1, 0]]
trS = [[0, 1, 1],
       [0, 1, 0],
       [1, 1, 0]]
trSReversed = [[1, 1, 0],
               [0, 1, 0],
               [0, 1, 1]]
trDiagonal = [[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]]
trDiagonalreversed = [[0, 0, 1],
                      [0, 1, 0],
                      [1, 0, 0]]
trLine = [[1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]]
trCross = [[0, 1, 0],
           [1, 1, 1],
           [0, 1, 0]]
trLineSmall = [[0, 0, 0],
               [0, 0, 0],
               [1, 1, 0]]

gridCircle = []
gridTriangle = []
gridSquare = []

board = open("board.txt", "a")
maxSize = 26
minSize = 21
randomBlock = True
size = 21
form = "TRIANGLE"


class Game:
    def __init__(self, size=21):
        self.grid = []
        self.size = size
        self.score = 0
        self.error = 0 #max 3 erreurs successives
        self.path = "board.txt"
        self.grid = "TRIANGLE" #forme du plateau

    def save_grid(self, path):
        with open(path, "w") as file:
            for val in self.grid:
                file.write("  ".join(val))
                file.write("\n")

    def read_grid(self):
        board = open(self.path, "r")
        lines = board.readlines()

        for x in range(len(size)):
            l = lines[x].split("  ").pop(size - 1)

            for y in range(len(size)):
                self.grid[x][y] = int(l[y])

    def makeTriangle(self, d):
        par = d % 2

        for y in range(d):
            ligne = []
            for x in range(d * 2 + par):
                if x < d - y - 1 + par or x > d + y:
                    ligne.append("0  ")
                else:
                    ligne.append("1  ")

            self.grid.append(ligne)

    def print_grid(self):
        print("SCORE :"+self.score)
        print()
        print("0    : ARRETER LE JEU")

        print(end="     ")
        for i in range(1, 10):
            print(i, end="  ")
        for i in range(10, self.size):
            print(i, end=" ")
        print(self.size)

        for i in range(self.size):
            print(end="  ")
        print(" ")

        file = open(self.path, "r")
        lines = board.readlines()
        for i in range(1, self.size + 1):
            space = "   "
            if i < 10:
                space += " "
            print(i, end=space)
            line = lines[i - 1]
            line = line.replace("1", "ᴥ")
            line = line.replace("0", " ")

            print(line, end="")

    def row_states(self):
        for i in range(len(board)):
            l = board[i]

            if 1 not in l:
                self.score += 8

    def row_clear(self, i):
        for o in range(len(board)):
            if board[i][o] == 2:
                board[i][o] = 1
                self.score += 2


    def col_state(self):
        for i in range(len(board)):
            l = board[i]

            if "1" not in l:
                self.score += 8

    def col_clear(self, i):

        for o in range(len(board)):
            if board[o][i] == 2:
                board[i][o] = 1
                self.score += 2

    def fallBlocks(self):
        felt = False

        for x in range(size):
            for y in range(1,size):
                if board[x][y] == 2 and board[x][y-1] == 1:
                    board[x][y] == 1
                    board[x][y - 1] == 2
                    felt = True

        return felt

    def print_blocs(self):
        blocs = []

        match self.grid:
            case "TRIANGLE":
                blocs = gridTriangle
            case "CARRE":
                blocs = gridSquare
            case "CERCLE":
                blocs = gridCircle
            case "POLY":
                blocs = gridTriangle
            case _:
                return

        for i in range(len(blocs)):
            b = blocs[i]
            print("Bloc"+i+"   :")

            for l in b:
                for c in l:
                    print(c+"  ")
                print()

            print("-------------------")

        print()

    def valid_position(self, bloc, i, j):
        output = True
        if len(bloc) > len(self.grid) - i + 1:  # vérif si pas out of range en hauteur
            return False
        if len(bloc) > len(self.grid[0]) - j + 1:  # vérif pas out of range en longueur
            return False
        for k in range(len(bloc)):
            for l in range(len(bloc)):
                if bloc[k][l] == 1 and self.grid[i + k][j + l] != 1:
                    output = False
        return output

    def emplace_bloc(self, bloc, i, j):
        L = len(bloc)
        l = len(bloc[0])

        for x in range(L):
            for y in range(l):
                self.grid[i+x][j+y] = bloc[x][y]

    def endGame(self):
        print("SCORE : "+self.score)

def losange(d):
    mid = d / 2
    par = d % 2

    for y in range(d):
        for x in range(d):
            if y <= d / 2:
                if mid - y - 2 + par < x < mid + y - par + 1:
                    board.write("1  ")
                else:
                    board.write("0  ")
            else:
                if -d + mid + y - 1 + par < x < d - y + mid - par:
                    board.write("1  ")
                else:
                    board.write("0  ")

        board.write("\n")


def circle(d):
    center = d // 2
    if d % 2 == 0:
        center -= 0.5

    for x in range(d):
        for y in range(d):
            if sqrt((x - center) ** 2 + (y - center) ** 2) < d / 2:
                board.write("1  ")
            else:
                board.write("0  ")
        board.write("\n")


def printLine():
    for i in range(64):
        print("UW", end="")
    print("UW")


def jumpPage():
    for i in range(32):
        print("")


def printHomepage():
    jumpPage()
    printLine()
    print(" 1: Commencer à jouer")
    print(" 2: Paramétrer le jeu")
    printLine()



def inputHomePage():
    choice = input()
    match choice:
        case "1":
            Game
        case "2":
            print
        case _:
            inputHomePage()



def printRules():
    jumpPage()
    printLine()
    printLine()
    print("")
    print("     1: HomePage")



def inputRules():
    choice = input()
    match choice:
        case "1":
            printHomepage()
            inputHomePage()
        case _:
            inputRules()



def printConfiguration():
    alea = "TOUT les blocs"
    if randomBlock:
        alea = "Blocs aléatoires"

    jumpPage()
    printLine()
    print("     Choisir forme du plateau :      " + form)
    print("         1 : Triangle")
    print("         2 : Losange")
    print("         3 : Cercle")
    print("     Choisir Règles du jeu :         " + alea)
    print("         4 : Blocs aléatoires")
    print("         5 : TOUT les blocs")
    print("")
    print("         6 : LANCER LE JEU")
    printLine()



def inputConfiguration():
    choice = input()
    stayPage = True

    match choice:
        case "1":
            form = "TRIANGLE"
        case "2":
            form = "LOSANGE"
        case "3":
            form = "CERCLE"
        case "4":
            randomBlock = True
        case "5":
            randomBlock = False
        case "6":
            stayPage = False
            printSizeChoice()

    if stayPage:
        printConfiguration()
        inputConfiguration()



def printSizeChoice():
    jumpPage()
    printLine()
    print("     Choisir la Taille du plateau de jeu Entre :")
    print("         min " + str(minSize))
    print("         max " + str(maxSize))
    printLine()


def inputSizeChoice():
    try:
        choice = int(input())
        if (minSize < choice < maxSize):
            size = choice
            Game
        else:
            inputSizeChoice()

    except ValueError:
        inputSizeChoice()


def printBlocksChoice():
    blocksToDisplay = []

    jumpPage()
    printLine()
    printLine()
    print("")


def isInPoly(points, x, y):
    #source : https://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html
    #Randolph Franklin
    count = 0

    npol = len(points)
    for i in range(0, npol, 1):
        j = (i+1)%npol
        if ((((points[i][1] <= y) and (y < points[j][1])) or
             ((points[j][1] <= y) and (y < points[i][1]))) and
                (x < (points[j][0] - points[i][0]) * (y - points[i][1]) / (points[j][1] - points[i][1]) + points[i][0])):
            count += 1

    return not count%2==0

trianglePoly = [[0,0],[9,9],[0,9],[9,0]]
def poly(points):
    board = open("board.txt", "a")

    for y in range(size):
        for x in range(size):
            if isInPoly(points,x,y):
                board.write("1  ")
            else:
                board.write("0  ")
        board.write("\n")
    board.close()

poly(trianglePoly)