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
gridCercle = [cu, cG, cll, cBottle, cLine, cL, cCircle, cSquare, cRectangle, cU]
gridTriangle = [trLine, trCross, trLineSmall, trS, trDiagonal, trDiagonalreversed, trSReversed]
gridLosange = [lSquare, ll, lx, lt, lline, lStairs, lT, lTriangle]

# gridCircle.append(gridCommon)
# gridTriangle.append(gridCommon)
# gridSquare.append(gridCommon)

class Game:
    def __init__(self, size=21):
        self.size = size
        self.grid = []
        self.score = 0
        self.error = 3  # max 3 erreurs successives
        self.shape = "TRIANGLE"  # forme du plateau.
        self.path = "" # Le fichier dans lequel on écrit nos plateaux. Dépend de self.shape au lancement du jeu.
        self.randomBlock = True

        self.ended = False

    def tick(self):
        pass
        # self.print_grid()
        # self.print_HUD()

    def save_grid(self):
        with open(self.path, "w") as file:
            for ligne in self.grid:
                file.write(" ".join(ligne))
                file.write("\n")

    def read_grid(self):
        with open(self.path) as b:
            lines = b.readlines()

            for x in range(self.size):
                l = lines[x].split(" ").pop(self.size - 1)

                for y in range(self.size):
                    self.grid[x][y] = int(l[y])

    def makeTriangle(self):
        """
        renderSize = (self.size//2 + 1)
        par = renderSize % 2

        for y in range(renderSize):
            ligne = []
            for x in range(renderSize * 2 + par):
                if x < renderSize - y - 1 + par or x > renderSize + y:
                    ligne.append(0)
                else:
                    ligne.append(1)

            self.grid.append(ligne)
        """
        self.makeLosange()
        for _ in range(self.size // 2):
            del self.grid[self.size // 2 + self.size % 2]
        

    def makeCircle(self):
        center = self.size // 2
        if self.size % 2 == 0:
            center -= 0.5

        for x in range(self.size):
            ligne = []
            for y in range(self.size):
                if sqrt((x - center) ** 2 + (y - center) ** 2) < self.size / 2:
                    ligne.append(1)
                else:
                    ligne.append(0)
            
            self.grid.append(ligne)

    def makeLosange(self):
        mid = self.size / 2
        # par comme "parité"
        par = self.size % 2

        for y in range(self.size):
            ligne = []
            for x in range(self.size):
                if y <= self.size / 2:
                    if mid - y - 2 + par < x < mid + y - par + 1:
                        ligne.append(1)
                    else:
                        ligne.append(0)
                else:
                    if -self.size + mid + y - 1 + par < x < self.size - y + mid - par:
                        ligne.append(1)
                    else:
                        ligne.append(0)

            self.grid.append(ligne)

    def print_HUD(self):
        print(f"SCORE : {self.score}")
        print("")
        print("0    : ARRÊTER LE JEU")

    def print_grid(self):
        
        print(end="     ")
        for i in range(1, 10):
            print(i, end="  ")
        for i in range(10, self.size):
            print(i, end=" ")
        print(self.size)

        for i in range(self.size):
            print(end="  ")
        print(" ")

        lines = self.grid
        for i in range(1, len(self.grid) + 1):
            space = "   "
            if i < 10:
                space += " "
            print(i, end=space)
            line = lines[i - 1]

            lineStr = "  ".join([str(el) for el in line]) # Python oblige le contenu de la liste dans join() à être de type string.
            lineStr = lineStr.replace("1", "▢")
            lineStr = lineStr.replace("0", " ")

            print(lineStr)

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

        for x in range(self.size):
            for y in range(1, self.size):
                if board[x][y] == 2 and board[x][y - 1] == 1:
                    board[x][y] == 1
                    board[x][y - 1] == 2
                    felt = True

        return felt

    def print_blocs(self):
        blocs = []

        match self.shape:
            case "TRIANGLE":
                blocs = gridTriangle
            case "CARRE":
                blocs = gridLosange
            case "CERCLE":
                blocs = gridCercle
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
        if len(bloc) > len(self.grid) - i + 1:  # vérif si pas out of range en hauteur
            return False
        if len(bloc) > len(self.grid[0]) - j + 1:  # vérif pas out of range en longueur
            return False
        for k in range(len(bloc)):
            for l in range(len(bloc)):
                if bloc[k][l] == 1 and self.grid[i + k][j + l] != 1:
                    return False
        return True

    def emplace_bloc(self, bloc, i, j):
        L = len(bloc)
        l = len(bloc[0])

        for x in range(L):
            for y in range(l):
                self.grid[i + x][j + y] = bloc[x][y]

    def endGame(self):
        print("")
        printLine()
        print("SCORE : ", self.score)
        printLine()

        self.ended = True


def printLine():
    for i in range(64):
        print("UW", end="")
    print("UW")


def jumpPage():
    """Efface la page, en faisant 32 fois un print("")"""
    for _ in range(32):
        print("")


def printHomepage():
    jumpPage()
    printLine()
    print(" 1: Commencer à jouer")
    print(" 2: Paramétrer le jeu")
    print("")
    print(" 3: Afficher les règles")
    printLine()


def inputHomePage():
    choice = ""

    # On ne devrait pas sortir de cette fonction (donc du programme entier) une fois qu'on a fini de configurer le jeu.
    while choice != "1":
        choice = input()
        if choice == "2":
            printConfiguration()
            inputConfiguration()
        elif choice == "3":
            printRules()
            inputRules()
    match game.shape:
        case "TRIANGLE":
            game.makeTriangle()
        case "LOSANGE":
            game.makeLosange()
        case "CERCLE":
            game.makeCircle()


def printRules():
    jumpPage()
    printLine()
    print("     Tetrus, c'est quoi ?")
    print("")
    print("     Entrée: HOME")
    printLine()


def inputRules():
    input()
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
    print("")
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
                    printConfiguration()
                case "2":
                    game.shape = "LOSANGE"
                    printConfiguration()
                case "3":
                    game.shape = "CERCLE"
                    printConfiguration()
                case "4":
                    game.randomBlock = True
                    printConfiguration()
                case "5":
                    game.randomBlock = False
                    printConfiguration()
                case "6":
                    printSizeChoice()
                    inputSizeChoice()

        printHomepage()


def printSizeChoice():
    jumpPage()
    printLine()
    print(f"     Choisir la taille du plateau de jeu entre {minSize} et {maxSize}")
    printLine()


def inputSizeChoice():
    okay = False

    while not okay:
        try:
            choice = input()
            if choice == "" or choice == "\n":
                printConfiguration()
                return None

            choice = int(choice)
            if minSize <= choice <= maxSize:
                game.size = choice
                okay = True
            else:
                raise ValueError
        except ValueError:
            print("Veuillez écrire un nombre entre 21 et 26 inclus")
    
    printConfiguration()


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


# associer select bloc à partie logique en parallèle à printblocs

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

    minSize = 21
    maxSize = 26

    printHomepage()
    game = Game()
    inputHomePage()

    # Une fois que le joueur lance la partie...
    game.path = game.shape.lower() + ".txt"
    jumpPage()
    game.print_grid()

    while not game.ended:
        game.tick()

