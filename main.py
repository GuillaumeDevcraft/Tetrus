# coding=utf-8

from math import *
from copy import deepcopy
import random as rand

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

gridCercle += gridCommon
gridTriangle += gridCommon
gridLosange += gridCommon

# Variable purement utilitaire, pour éviter de se répéter
alphabet = "abcdefghijklmnopqrstuwxyz"

class Game:
    def __init__(self, size=21):
        self.size = size
        self.grid = []
        self.score = 0
        self.error = 3  # max 3 erreurs successives
        self.shape = "TRIANGLE"  # forme du plateau.
        self.path = "" # Le fichier dans lequel on écrit nos plateaux. Dépend de self.shape au lancement du jeu.
        self.randomBlock = True
        self.blocks = [] # Le jeu de blocs de cette partie

        self.tickCount = 0 # Combien de tours sont passés ? Cela sert pour la fonction read_grid()

        self.ended = False

    def setup(self):
        self.path = self.shape.lower() + ".txt"
        match self.shape:
            case "TRIANGLE":
                self.blocks = deepcopy(gridTriangle)
            case "LOSANGE":
                self.blocks = deepcopy(gridLosange)
            case "CERCLE":
                self.blocks = deepcopy(gridCercle)
            case _:
                self.blocks = deepcopy(gridCommon) # Ce cas ne devrait jamais se produire.

    def tick(self):
        while True:
            self.print_grid()

            if self.randomBlock:
                rand.shuffle(self.blocks)
                blocks_suggested = self.blocks[:3]
                self.print_HUD(blocks_suggested)
            else:
                blocks_suggested = self.blocks
                self.print_HUD(blocks_suggested)

            print("")

            wanted_block = input().lower()

            # Le choix du bloc
            while True:
                if 0 < len(wanted_block) == 1:
                    if wanted_block[0] in alphabet:
                        try:
                            chosen_block_arr = blocks_suggested[alphabet.index(wanted_block[0])]
                            break
                        except IndexError:
                            pass
                        
                print("Votre réponse n'est pas valide. Veuillez choisir entre : " + ", ".join(alphabet[:len(blocks_suggested)]))
                wanted_block = input().lower()

            print("")
            print("Bien. Maintenant, choisissez une rotation de votre bloc (0, 90, 180, -90) : ")
            for i in range(len(chosen_block_arr)):
                print("  ".join(["◼" if n == 1 else " " for n in chosen_block_arr[i]]))


            # Le choix de la rotation
            while True:
                try:
                    rotation = int(input())
                    if rotation % 90 == 0:
                        chosen_block_arr = rotate_matrix(chosen_block_arr, rotation)
                        break
                except ValueError:
                    pass
                print("Veuillez entrer une rotation valide (0, 90, 180, -90) : ")

            print("")
            for i in range(len(chosen_block_arr)):
                print("  ".join(["◼" if n == 1 else " " for n in chosen_block_arr[i]]))
            print("Parfait ! Écrivez pour finir la position à laquelle vous voulez placer votre bloc (lettre de ligne;numéro de colonne) : ")

            # Le choix des coordonnées
            while True:
                try:
                    coords = input().split(";")
                    if len(coords) == 2:
                        if (coords[0].lower() in alphabet[:len(self.size)]) and (int(coords[1]) in range(1, self.size + 1)):
                            x, y = coords[0], coords[1]
                            break
                except ValueError:
                    pass
                print("Veuillez entrer des coordonnées valides séparées d'un point virgule (lettre de ligne;numéro de colonne) : ")

            chosen_block_arr = trim_matrix(chosen_block_arr)
            #is valid ==> break
            if (self.valid_position(chosen_block_arr, alphabet.index(x), y)):
                pass
            

        self.tickCount += 1

    def save_grid(self):
        with open(self.path, "w") as file:
            for ligne in self.grid:
                file.write(" ".join(ligne))
                file.write("\n")
            file.write("\n")

    def read_grid(self):
        with open(self.path) as b:
            lines = b.readlines()

            for x in range(self.size):
                l = lines[x].split(" ").pop(self.size - 1)

                for y in range(self.size):
                    self.grid[x][y] = int(l[y])


    def makeTriangle(self):
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


    def print_HUD(self, blocks):
        print("")
        print("Choisissez un bloc parmi les suivants à l'aide de leur lettre.")

        # On donne à chaque bloc un terrain (un "plot") de la taille de celui qui a besoin du plus d'espace.
        plotSize = max([len(liste) for liste in blocks]) # Les listes par compréhension sont parfaites pour faire des opérations sur chaque élément d'une liste
        
        separator = (("   " * plotSize) + "╦ ")

        print("╔ ",end="")
        print(
            separator.join([alphabet[n] + "." for n in range(len(blocks))]),
            end = ("   "*plotSize + "╗\n")
        )

        for x in range(plotSize):
            totalLigne = []
            for block in blocks:
                try:
                    blockStr = [str(el) for el in block[x]]
                except IndexError:
                    blockStr = plotSize * ["0"]
                while len(blockStr) < plotSize:
                    blockStr += ["0"]
                final = "  ".join(blockStr).replace("0", " ").replace("1", "◼")
                
                totalLigne.append(final)
            
            print("║   " + "  ║   ".join(totalLigne) + "  ║")
        print("╚═══" + "╩═══".join([("═══"*plotSize)]*len(blocks)) + "╝")

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
            space = "    "
            print(alphabet[i-1], end=space)
            line = lines[i - 1]

            lineStr = "  ".join([str(el) for el in line]) # Python oblige le contenu de la liste dans join() à être de type string.
            lineStr = lineStr.replace("1", "▢")
            lineStr = lineStr.replace("0", " ")

            # Il y a en réalité un moyen beaucoup plus compact de faire ce que je fais ici, mais pour la lisibilité du code, restons là-dessus
            if i != 6:
                print(lineStr)
            else:
                print(lineStr, end="      ")
                print(f"<< SCORE : {self.score} >>")


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

    ################################ FINISH ME #############################
    def valid_position(self, block, x, y):
        for i in range(len(block)):
            for j in range(len(block[i])):
                if block[j][i] == 1:
                    if self.grid[x][y]

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


def trim_matrix(matrix, forbidden = 0):
    """Crée une nouvelle matrice sans l'excédent de <forbidden> de <matrix>.
    Par exemple, voici matrice1 :
    0001110100
    0100120300
    0000010000
    0000000000

    et voilà trim_matrix(matrice1, 0) :
    0011101
    1001203
    0000100
    """

    result = []

    # Étape 1. Récupérer les coordonnées X et Y des valeurs non illégales (càd, pas égales à <forbidden>) dans leur tableau respectif
    legal_coordX = []
    legal_coordY = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] != forbidden:
                legal_coordX.append(x)
                legal_coordY.append(y)
    
    # Étape 2. Déterminer le rectangle à copier au sein de <matrix>
    coordCorner1 = (min(legal_coordX), min(legal_coordY))
    coordCorner2 = (max(legal_coordX), max(legal_coordY))
    size = (coordCorner2[0] - coordCorner1[0] + 1, coordCorner2[1] - coordCorner1[1] + 1)

    # Étape 3. Copier le rectangle mentionné ci-dessus dans une nouvelle matrice
    for x in range(coordCorner1[0], coordCorner1[0] + size[0]):
        ligne = []
        for y in range(coordCorner1[1], coordCorner1[1] + size[1]):
            try: # Au cas où <matrix> n'est pas rectangulaire, on met quelque chose pour remplacer
                ligne.append(matrix[x][y])
            except IndexError:
                ligne.append(0) # Valeur arbitraire de remplacement, choisie pour les besoins du Tetrus
        result.append(ligne)
    
    return result

assert trim_matrix([
        [0,0,0,1,1,1,0,1,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0]
    ]) == [[1,1,1,0,1,0],
           [0,1,0,0,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,1]
           ]


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


def rotate_matrix(matrix, rot):
    """La matrice doit être rectangulaire, sinon une exception va être levée
    """
    match rot % 360:
        case 0:
            return matrix
        case 90:
            result = []
            for y in range(len(matrix[0])):
                new_line = []
                for x in range(len(matrix) - 1, -1, -1):
                    new_line.append(matrix[x][y])
                result.append(new_line)
            return result
        case 180:
            result = []
            for ligne in matrix:
                ligne.reverse()
                result.insert(0, ligne)
            return result
        case 270:
            return rotate_matrix(rotate_matrix(matrix, 90), 180)
        

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
    game.setup()
    jumpPage()
    game.print_grid()

    while not game.ended:
        game.tick()

