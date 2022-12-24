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
        self.trials = 3  # max 3 erreurs successives
        self.shape = "CERCLE"  # forme du plateau.
        self.path = "" # Le fichier dans lequel on écrit nos plateaux. Dépend de self.shape au lancement du jeu.
        self.randomBlock = False
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
        if self.randomBlock:
            rand.shuffle(self.blocks)
            blocks_suggested = self.blocks[:3]
        else:
            blocks_suggested = self.blocks
            
        while True:
            self.print_grid()
            print("")
            self.print_HUD(blocks_suggested)

            wanted_block = input().lower()

            # Le choix du bloc
            chosen_block_arr = self.select_block(blocks_suggested, wanted_block)

            accept = ["oui", "o", "yes", "y"]
            print("")
            print_block(chosen_block_arr)
            rep = input("Bien. Souhaitez-vous effectuer une rotation sur ce bloc ('oui' pour accepter, autre chose pour refuser) ? ").lower()
            while rep in accept:
                # Le choix de la rotation
                chosen_block_arr = self.rotate_block(chosen_block_arr)
                print_block(chosen_block_arr)
                print("")
                if input("Êtes-vous satisafait de cette rotation ? ").lower() in accept:
                    break
            

            print("")
            print("Parfait ! Écrivez pour finir la position à laquelle vous voulez placer votre bloc (lettre de ligne;numéro de colonne) : ")

            # Le choix des coordonnées
            while True:
                try:
                    coords = input().strip("()").split(";")
                    if len(coords) == 2:
                        if (coords[0].lower() in alphabet[:self.size]) and (int(coords[1]) in range(1, self.size + 1)):
                            x, y = int(alphabet.index(coords[0])), int(coords[1])
                            break
                except ValueError:
                    pass
                print("Veuillez entrer des coordonnées valides séparées d'un point virgule (lettre de ligne;numéro de colonne) : ")

            chosen_block_arr = trim_matrix(chosen_block_arr)
            #is valid ==> break
            if (self.valid_position(chosen_block_arr, x, y - 1)): # y - 1 car les colonnes sont numérotées à partir de 1, pas 0
                self.place_block(chosen_block_arr, x, y - 1)
                self.trials = 3
                break
            else:
                self.trials -= 1
                if self.trials == 0:
                    print("")
                    self.loseGame()
                    return
                printLine("/!\\")
                # "s"*int(self.trials != 1) signifie simplement que s'il reste plusieurs essais au joueur, on affiche un s (int(True) == 0)
                print(f"AÏE ! Votre coup est illégal, il vous reste maintenant {self.trials} essai" + "s"*int(self.trials != 1) + " sur 3.")
                printLine("/!\\")



        self.tickCount += 1

    def select_block(self, options, wanted_block):
        while True:
            if 0 < len(wanted_block) == 1:
                if wanted_block[0] in alphabet:
                    try:
                        chosen_block_arr = options[alphabet.index(wanted_block[0])]
                        break
                    except IndexError:
                        pass
                    
            print("Votre réponse n'est pas valide. Veuillez choisir entre : " + ", ".join(alphabet[:len(options)]))
            wanted_block = input().lower()
        return chosen_block_arr

    def rotate_block(self, block):
        print("Veuillez entrer une rotation (0, 90, 180, -90) : ")
        while True:
            try:
                rotation = int(input())
                if rotation % 90 == 0:
                    block = rotate_matrix(block, rotation)
                    break
            except ValueError:
                pass
            print("Veuillez entrer une rotation valide (0, 90, 180, -90) : ")
        
        print("")
        print(f"Rotation de {rotation}°...")
        return block


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

        counter = 0
        while True:
            blocksInLine = blocks[counter:10 + counter]
            print("╔ ",end="")
            print(
                separator.join([alphabet[n + counter] + "." for n in range(len(blocksInLine))]),
                end = ("   "*plotSize + "╗\n")
            )

            for x in range(plotSize):
                totalLigne = []
                for block in blocksInLine:
                    try:
                        blockStr = [str(el) for el in block[x]]
                    except IndexError:
                        blockStr = plotSize * ["0"]
                    while len(blockStr) < plotSize:
                        blockStr += ["0"]
                    final = "  ".join(blockStr).replace("0", " ").replace("1", "◼")

                    totalLigne.append(final)

                print("║   " + "  ║   ".join(totalLigne) + "  ║")
            print("╚═══" + "╩═══".join([("═══"*plotSize)]*len(blocksInLine)) + "╝")

            counter += 10
            if len(blocks) < counter:
                break

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
            lineStr = lineStr.replace("2", "◼")
            lineStr = lineStr.replace("1", "▢")
            lineStr = lineStr.replace("0", " ")

            # Il y a en réalité un moyen beaucoup plus compact de faire ce que je fais ici, mais pour la lisibilité du code, restons là-dessus
            if i != 6:
                print(lineStr)
            else:
                print(lineStr, end="      ")
                print(f"<< SCORE : {self.score} >>")


    def row_state(self):
        res = []
        for i in range(len(self.grid)):
            l = self.grid[i]

            if 1 not in l:
                res.append(i)
        return res

    def row_clear(self, i):
        for o in range(len(self.grid)):
            if self.grid[i][o] == 2:
                self.grid[i][o] = 1

    def col_state(self):
        res = []
        for i in range(len(self.grid)):
            l = self.grid[i]

            if 1 not in l:
                res.append(i)
        return res

    def col_clear(self, j):
        for o in range(len(self.grid)):
            if self.grid[o][j] == 2:
                self.grid[j][o] = 1
                self.score += 2

    def blocks_fall(self):
        felt = False

        for x in range(self.size):
            for y in range(1, self.size):
                if board[x][y] == 2 and board[x][y - 1] == 1:
                    board[x][y] == 1
                    board[x][y - 1] == 2
                    felt = True

        return felt

    def valid_position(self, block, x, y):
        """Vérifie si <block> peut entrer dans la grille de jeu si on le place aux coordonnées <x>,<y>
        """
        for i in range(len(block)):
            for j in range(len(block[i])):
                try:
                    if x - j < 0: # S'il n'y a même pas la place (verticalement) pour la pièce, alors la position donnée est forcément fausse
                        return False
                    if block[len(block) - 1 - j][i] == 1:
                        if self.grid[x - j][y + i] != 1:
                            return False
                    
                except IndexError:
                    continue
        return True

    def place_block(self, block, x, y):
        for i in range(len(block)):
            for j in range(len(block[i])):
                try:
                    self.grid[x - j][y + i] += block[len(block) - 1 - j][i]
                except IndexError:
                    continue

    def loseGame(self):
        printLine()

        print("OOF ! Vous avez perdu.", end=" "*15)
        print(f"// SCORE : {self.score} //")
        printLine()
        self.ended = True
    
    def endGame(self):
        printLine()
        print("SCORE :", self.score)
        printLine()

        self.ended = True


def printLine(pattern="UW"):
    for i in range(64):
        print(pattern, end="")
    print(pattern)


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

def print_block(block):
    for i in range(len(block)):
        print("  ".join(["◼" if n == 1 else " " for n in block[i]]))


if __name__ == "__main__":

    minSize = 21
    maxSize = 26

    printHomepage()
    game = Game()
    inputHomePage()

    # Une fois que le joueur lance la partie...
    game.setup()
    jumpPage()

    while not game.ended:
        game.tick()

