# coding=utf-8

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

gridCommon = [tl, tDot, tLine, tSquare, tStair, tT, tL]
gridCircle = [cu, cG, cll, cBottle, cLine, cL, cCircle, cSquare, cRectangle, cU]
gridTriangle = [trLine, trCross, trLineSmall, trS, trDiagonal, trDiagonalreversed, trSReversed]
gridSquare = [lSquare, ll, lx, lt, lline, lStairs, lT, lTriangle]


class Game:
    def __init__(self, size=21):
        self.size = size
        self.grid = []
        self.score = 0
        self.error = 0  # max 3 erreurs successives
        self.path = "board.txt"
        self.shape = "TRIANGLE"  # forme du plateau
        self.randomBlock = True

    def save_grid(self, path):
        with open(path, "w") as file:
            for val in self.grid:
                file.write("  ".join(val))
                file.write("\n")

    def read_grid(self):
        with open(self.path) as b:
            lines = b.readlines()

            for x in range(self.size):
                l = lines[x].split("  ").pop(self.size - 1)

                for y in range(self.size):
                    self.grid[x][y] = int(l[y])

    def makeTriangle(self):
        peer = self.size % 2

        file = open(self.path, "w")

        s = self.size//2+peer
        for y in range(s):
            ligne = []
            for x in range(s * 2 - peer):
                if x < s - y - 2 + peer or x > s + y - 1:
                    file.write("0  ")
                else:
                    file.write("1  ")

            file.write("\n")

    def makeCircle(self):
        center = self.size // 2
        if self.size % 2 == 0:
            center -= 0.5

        file = open(self.path, "w")

        for x in range(self.size):
            for y in range(self.size):
                if sqrt((x - center) ** 2 + (y - center) ** 2) < self.size / 2:
                    file.write("1  ")
                else:
                    file.write("0  ")
            file.write("\n")

    def makeLosange(self):
        mid = self.size / 2
        par = self.size % 2

        file = open(self.path, "w")

        for y in range(self.size):
            for x in range(self.size):
                if y <= self.size / 2:
                    if mid - y - 2 + par < x < mid + y - par + 1:
                        file.write("1  ")
                    else:
                        file.write("0  ")
                else:
                    if -self.size + mid + y - 1 + par < x < self.size - y + mid - par:
                        file.write("1  ")
                    else:
                        file.write("0  ")

            file.write("\n")

    def print_grid(self):
        print("SCORE :", self.score)
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
        lines = file.readlines()
        for i in range(1, len(lines)+1):
            space = "   "
            if i < 10:
                space += " "
            print(i, end=space)
            line = lines[i - 1]
            line = line.replace("1", "ᴥ")
            line = line.replace("0", " ")

            print(line, end="")

    def row_states(self):
        for i in range(len(self.grid)):
            l = self.grid[i]

            if 1 not in l:
                self.score += 8

    def row_clear(self, i):
        for o in range(len(self.grid)):
            if self.grid[i][o] == 2:
                self.grid[i][o] = 1
                self.score += 2

    def col_state(self):
        for i in range(len(self.grid)):
            l = self.grid[i]

            if "1" not in l:
                self.score += 8

    def col_clear(self, i):

        for o in range(len(self.grid)):
            if self.grid[o][i] == 2:
                self.grid[i][o] = 1
                self.score += 2

    def fallBlocks(self):
        felt = False

        for x in range(self.size):
            for y in range(1, self.size):
                if self.grid[x][y] == 2 and self.grid[x][y - 1] == 1:
                    self.grid[x][y] == 1
                    self.grid[x][y - 1] == 2
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
            print("Bloc" + i + "   :")

            for l in b:
                for c in l:
                    print(c + "  ")
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
                self.grid[i + x][j + y] = bloc[x][y]

    def endGame(self):
        print("SCORE : ", self.score)


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
    choice = ""

    # On ne devrait pas sortir de cette fonction (donc du programme entier) une fois qu'on a fini de configurer le jeu.
    while choice != "1":
        choice = input()
        if choice == "2":
            printConfiguration()
            inputConfiguration()
    match game.shape:
        case "TRIANGLE":
            game.makeTriangle()
        case "LOSANGE":
            game.makeLosange()
        case "CERCLE":
            game.makeCircle()
    game.print_grid()


def printRules():
    jumpPage()
    printLine()
    printLine()
    print("")
    print("     1: HomePage")


def inputRules():
    choice = ""
    reponses_possibles = ["1"]

    while choice not in reponses_possibles:
        choice = input()
        printHomepage()


def printConfiguration():
    alea = "TOUS les blocs"
    if game.randomBlock:
        alea = "Blocs aléatoires"

    jumpPage()
    printLine()
    print("     Choisir forme du plateau :      ", game.shape)
    print("         1 : Triangle")
    print("         2 : Losange")
    print("         3 : Cercle")
    print("     Choisir Règles du jeu :         ", alea)
    print("         4 : Blocs aléatoires")
    print("         5 : TOUS les blocs")
    print(f"         6 : Taille du plateau (Actuelle : {game.size})")
    print("")
    print("         7 : HOME")
    printLine()


def inputConfiguration():
    choice = ""
    stayPage = True

    reponses_possibles = ["1", "2", "3", "4", "5", "6", "7"]

    while choice not in reponses_possibles:
        choice = ""

        while choice != "7":
            choice = input()
            match choice:
                case "1":
                    game.shape = "TRIANGLE"
                case "2":
                    game.shape = "LOSANGE"
                case "3":
                    game.shape = "CERCLE"
                case "4":
                    game.randomBlock = True
                case "5":
                    game.randomBlock = False
                case "6":
                    printSizeChoice()
                    inputSizeChoice()

        printHomepage()
        inputHomePage()


def printSizeChoice():
    jumpPage()
    printLine()
    print(f"     Choisir la taille du plateau de jeu entre {str(minSize)} et {str(maxSize)}")
    printLine()


def inputSizeChoice():
    okay = False

    while not okay:
        try:
            choice = input()
            if choice == "":
                printConfiguration()
                break

            choice = int(input())
            if minSize <= choice <= maxSize:
                game.size = choice
                okay = True
            else:
                raise ValueError
        except ValueError:
            print("Veuillez écrire un nombre entre 21 et 26 inclus")


def printBlocksChoice():
    blocksToDisplay = []

    jumpPage()
    printLine()
    printLine()
    print("")


def isInPoly(points, x, y):
    # source : https://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html
    # Randolph Franklin
    count = 0

    npol = len(points)
    for i in range(0, npol, 1):
        j = (i + 1) % npol
        if ((((points[i][1] <= y) and (y < points[j][1])) or
             ((points[j][1] <= y) and (y < points[i][1]))) and
                (x < (points[j][0] - points[i][0]) * (y - points[i][1]) / (points[j][1] - points[i][1]) + points[i][
                    0])):
            count += 1

    return not count % 2 == 0


trianglePoly = [[0, 0], [9, 9], [0, 9], [9, 0]]


def poly(points):
    board = open("board.txt", "a")

    for y in range(game.size):
        for x in range(game.size):
            if isInPoly(points, x, y):
                board.write("1  ")
            else:
                board.write("0  ")
        board.write("\n")
    board.close()


def print_blocs(shapelist):
    for i in range(1, len(gridCommon) + 1):
        temp2 = []
        temp2.append(replaceBlocs(gridCommon[i]))
    for j in range(len(temp2)):
        print(j + 1)
        for k in range(len(temp2[j])):
            print
            for l in range(len(temp2[j][k])):
                print(temp2[j][k][l], end="")
    for i in range(1, len(shapelist) + 1):
        temp1 = []
        temp1.append(replaceBlocs(shapelist[i]))
    for j in range(len(temp1)):
        print(j + 1 + len(gridCommon))
        for k in range(len(temp1[j])):
            print
            for l in range(len(temp1[j][k])):
                print(temp1[j][k][l], end="")


def select_bloc():
    pass


# associer select bloc à partie logique en parralèle à printblocs

def replaceBlocs(list):
    for i in range(len(list)):
        temp1 = []
        for j in range(len(list[i])):
            if list[i][j] == 1:
                temp2 = "■"
            else:
                temp2 = " "
            temp1.append(temp2)
    return temp1


if __name__ == "__main__":
    board = open("board.txt", "a")
    maxSize = 26
    minSize = 21

    printHomepage()
    game = Game()
    inputHomePage()
