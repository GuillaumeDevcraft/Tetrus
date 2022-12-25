# coding=utf-8
# Projet Tetrus Guillaume DELHAYE Idir NAIT MEDDOUR Tomas TARGE
# Fichier principal
import os
import random as rand
from copy import deepcopy
from datetime import datetime as time
from math import *

from utils import *

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
lStairs = [[0, 0, 1, 1],
           [0, 1, 1, 0],
           [1, 1, 0, 0],
           [1, 0, 0, 0]]
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


# classe game contenant une partie, tous ses paramètres et ses fonctions
class Game:
    def __init__(self, size=21):
        self.size = size  # taille du plateau
        self.grid = []  # plateau sous forme de matrice
        # snapshots[0] = options de la partie (nom, forme du plateau, taille du plateau, score)
        # le reste = les grilles
        self.snapshots = [tuple()]

        self.score = 0  # score
        self.trials = 3  # max 3 erreurs successives

        self.shape = "TRIANGLE"  # forme du plateau.
        self.randomBlock = True  # règle définissant les blocs disponibles à chaque tour

        self.path = ""  # Le fichier dans lequel on écrit nos plateaux. Dépend de self.shape au lancement du jeu.
        self.gamerTag = "Inconnu"

        self.blocks = []  # Le jeu de blocs de cette partie

        self.tickCount = 0  # Combien de tours sont passés ? Cela sert pour la fonction read_grid()

        self.ended = False

    # fonction permettant la création d'une partie, vérifie sa taille, son score et sa forme.
    # elle crée aussi le fichier unique où le plateau de la partie sera stockée
    def setup(self):

        if not (21 <= self.size <= 26):
            self.size = 21

        if self.score < 0:
            self.score = 0

        match self.shape:
            case "TRIANGLE":
                self.blocks = deepcopy(gridTriangle)
            case "LOSANGE":
                self.blocks = deepcopy(gridLosange)
            case "CERCLE":
                self.blocks = deepcopy(gridCercle)
            case _:
                self.shape = "TRIANGLE"
                self.blocks = deepcopy(gridTriangle)

        if self.path == "":
            self.path = self.shape.lower() + "_" + time.now().strftime("%d-%m-%Y@%H-%M-%S") + ".txt"

    #Execute l'ensemble des actions d'un tours
    def tick(self):
        # choisit quels blocs à afficher suivant la règle <self.randomBlock>
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
            chosen_block_arr = select_block(blocks_suggested, wanted_block)
            if chosen_block_arr is None:
                self.end_game()
                return None

            accept = ["oui", "o", "yes", "y"]
            print("")
            print_block(chosen_block_arr)
            rep = input(
                "Bien. Souhaitez-vous effectuer une rotation sur ce bloc ? ('oui' pour accepter, autre chose pour refuser) ").lower()
            while rep in accept:
                # Le choix de la rotation
                chosen_block_arr = rotate_block(chosen_block_arr)
                print_block(chosen_block_arr)
                print("")
                if input("Êtes-vous satisafait de cette rotation ? ").lower() in accept:
                    break

            print("")
            print(
                "Parfait ! Écrivez pour finir la position à laquelle vous voulez placer votre bloc (lettre de ligne;numéro de colonne) : ")

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
                print(
                    "Veuillez entrer des coordonnées valides séparées d'un point virgule (lettre de ligne;numéro de colonne) : ")

            print("")
            chosen_block_arr = trim_matrix(chosen_block_arr)
            # is valid ==> break
            if self.valid_position(chosen_block_arr, x,
                                   y - 1):  # y - 1 car les colonnes sont numérotées à partir de 1, pas 0
                self.place_block(chosen_block_arr, x, y - 1)
                self.trials = 3
                break
            else:
                self.trials -= 1
                if self.trials == 0:
                    print("")
                    self.lose_game()
                    return
                print_line("/!\\")
                # "s"*int(self.trials != 1) signifie simplement que s'il reste plusieurs essais au joueur, on affiche un s (int(True) = 1 et int(False) = 0)
                print(f"AÏE ! Votre coup est illégal, il vous reste {self.trials} essai" + "s" * int(
                    self.trials != 1) + " sur 3.")
                print_line("/!\\")

        # Récompenses !
        full_rows = self.row_state()
        full_cols = self.col_state()
        while full_rows != [] or full_cols != []:
            for row_index in full_rows:
                self.score += 2 * self.grid[row_index].count(2)
            for col_index in full_cols:
                occurrences = 0
                for i in range(len(self.grid)):
                    if self.grid[i][col_index] == 2:
                        occurrences += 1

                self.score += 2 * occurrences

            for row_index in full_rows:
                self.row_clear(row_index)
            if full_cols != []:
                for col_index in full_cols:
                    self.col_clear(col_index)
                self.blocks_fall()

            full_rows = self.row_state()
            full_cols = self.col_state()

        self.snapshots.append(deepcopy(self.grid))
        self.tickCount += 1

    #sauvegarde la partie en cours <self.snapshots[1:]> dans un nouveau fichier
    #<self.snapshots[1:]> contient alors <self.gamerTag> <self.shape> <self.size> <self.score> <self.grid>
    def save_grid(self):
        try:
            if not os.path.exists("./games/"):
                os.mkdir("./games")
            with open("./games/" + self.path, "w") as file:
                file.write("/!\\ NE PAS TOUCHER CE FICHIER ! /!\\\n")
                file.write("Nom, Forme du plateau, Taille du plateau, Score final\n")
                file.write(str(self.snapshots[0]).strip("()").replace("'", "") + "\n\n")

                counter = 1
                for grid in self.snapshots[1:]:
                    file.write("g" + str(counter) + "\n")
                    for ligne in grid:
                        file.write(" ".join([str(n) for n in ligne]))
                        file.write("\n")
                    counter += 1
        except IOError:
            print("Oof ! Je n'ai pas réussi à sauvegarder votre partie...")

    # met le contenu du fichier plateau dans la matrice <self.grid>
    def read_grid(self):
        try:
            with open("./games/" + self.path) as file:
                lines = file.readlines()

                for x in range(self.size):
                    l = lines[x].split(" ").pop(self.size - 1)

                    for y in range(self.size):
                        self.grid[x][y] = int(l[y])
        except IOError:
            print(f"Impossible de lire {self.path}. Le dossier games/ a-t-il été créé ?")

    # crée un triangle dans <self.grid>
    def make_triangle(self):
        self.make_losange()
        for _ in range(self.size // 2):
            del self.grid[self.size // 2 + self.size % 2]

    # crée un le cercle dans <self.grid>
    def make_circle(self):
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

    # crée un le losange dans <self.grid>
    def make_losange(self):
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

    # print dans la console les blocks proposés au joueur <blocks>, leurs lettres et demande au joueur d'en choisir un
    def print_HUD(self, blocks):
        print("")
        print("0. ARRÊTER LA PARTIE")
        print("Choisissez un bloc parmi les suivants à l'aide de leur lettre.")

        # On donne à chaque bloc un terrain (un "plot") de la taille de celui qui a besoin du plus d'espace.
        plot_size = max([len(liste) for liste in
                        blocks])  # Les listes par compréhension sont parfaites pour faire des opérations sur chaque élément d'une liste

        separator = (("   " * plot_size) + "╦ ")

        counter = 0
        while True:
            blocks_in_line = blocks[counter:8 + counter]
            print("╔ ", end="")
            print(
                separator.join([alphabet[n + counter] + "." for n in range(len(blocks_in_line))]),
                end=("   " * plot_size + "╗\n")
            )

            for x in range(plot_size):
                total_ligne = []
                for block in blocks_in_line:
                    try:
                        block_str = [str(el) for el in block[x]]
                    except IndexError:
                        block_str = plot_size * ["0"]
                    while len(block_str) < plot_size:
                        block_str += ["0"]
                    final = "  ".join(block_str).replace("0", " ").replace("1", "◼")

                    total_ligne.append(final)

                print("║   " + "  ║   ".join(total_ligne) + "  ║")
            print("╚═══" + "╩═══".join([("═══" * plot_size)] * len(blocks_in_line)) + "╝")

            counter += 8
            if len(blocks) < counter:
                break

    # print le plateau de jeu contenu dans <self.grid> dans la console
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
            print(alphabet[i - 1], end=space)
            line = lines[i - 1]

            line_str = "  ".join(
                [str(el) for el in line])  # Python oblige le contenu de la liste dans join() à être de type string.
            line_str = line_str.replace("2", "◼")
            line_str = line_str.replace("1", "▢")
            line_str = line_str.replace("0", " ")

            # Il y a en réalité un moyen beaucoup plus compact de faire ce que je fais ici, mais pour la lisibilité du code, restons là-dessus
            if i != 6:
                print(line_str)
            else:
                print(line_str, end="      ")
                print(f"<< SCORE : {self.score} >>")

    # return si la ligne est vide ou non
    def row_state(self):
        res = []
        for i in range(len(self.grid)):
            row = self.grid[i]

            # Les lignes ne comptant qu'un bloc plaçable ne sont effaçables que par la colonne qui le traverse.
            if row.count(0) == len(self.grid[0]) - 1:
                continue
            if 1 not in row:
                res.append(i)
        return res

    # vide une ligne <i> dans self.grid
    def row_clear(self, i):
        for o in range(self.size):
            if self.grid[i][o] != 0:
                self.grid[i][o] = 1

    # return si la colonne est vide ou non
    def col_state(self):
        res = []
        for i in range(self.size):
            col_list = []
            for j in range(len(self.grid)):
                col_list.append(self.grid[j][i])

            # Les colonnes ne comptant qu'un bloc plaçable ne sont effaçables que par la ligne qui le traverse.
            if col_list.count(0) == len(self.grid) - 1:
                continue
            if 1 not in col_list:
                res.append(i)
        return res

    # vide une colonne <i> dans self.grid
    def col_clear(self, j):
        for o in range(len(self.grid)):
            if self.grid[o][j] != 0:
                self.grid[o][j] = 1

    # fait tomber tous les blocs volants d'une case et return si des blocs sont tombés et donc s'il faut répéter la fonction
    def blocks_fall(self):
        something_changed = False

        for x in range(len(self.grid) - 1, 0, -1):
            for y in range(self.size):
                if self.grid[x][y] == 1 and self.grid[x - 1][y] == 2:
                    self.grid[x][y] = 2
                    self.grid[x - 1][y] = 1
                    something_changed = True

        if something_changed:
            self.blocks_fall()

    # return si oui ou non un <block> peut entrer dans la grille de jeu si on le place aux coordonnées <x>,<y>
    def valid_position(self, block, x, y):

        for i in range(len(block[0])):
            for j in range(len(block)):
                try:
                    if x - j < 0:  # S'il n'y a même pas la place (verticalement) pour la pièce, alors la position donnée est forcément fausse
                        return False
                    if len(block) - 1 - j < 0:
                        continue
                    if block[len(block) - 1 - j][i] == 1:
                        if self.grid[x - j][y + i] != 1:
                            return False

                except IndexError:
                    continue
        return True

    # place un <block> aux coordonnées <x> <y> dans la matrice <self.grid>
    def place_block(self, block, x, y):
        for i in range(len(block[0])):
            for j in range(len(block)):
                try:
                    self.grid[x - j][y + i] += block[len(block) - 1 - j][i]
                except IndexError:
                    continue

    # arrête la partie <self.set_ended> et le print au joueur
    def lose_game(self):
        print_line()

        print("OOF ! Vous avez perdu.", end=" " * 15)
        print(f"// SCORE : {self.score} //")
        print_line()
        self.set_ended(True)

    # print le score et arrête la partie <self.set_ended>
    def end_game(self):
        print_line()
        print("SCORE :", self.score)
        print_line()

        self.set_ended(True)

    # arrête ou non la partie selon <to> et demande au joueur s'il veut la sauvegarder
    def set_ended(self, to):
        self.ended = to
        if not to: return None

        print("\n")
        rep = input("Sauvegarder la partie ? (\"o\" pour oui, autre chose pour non) ").strip().lower()
        if rep not in ["o", "oui", "y", "yes", "1"]: return None

        self.gamerTag = input("Saisissez votre nom : ").strip()
        self.snapshots[0] = self.gamerTag, self.shape, self.size, self.score
        self.save_grid()


# print une ligne avec un certains <pattern>, <"UW"> par défaut
def print_line(pattern="UW"):
    for i in range(64):
        print(pattern, end="")
    print(pattern)


# Efface la page, en faisant 32 fois un print("")
def jump_page():
    for _ in range(32):
        print("")


# print la page d'accueil
def print_homepage():
    jump_page()
    print("       _____    _                   ")
    print("      |_   _|  | |                  ")
    print("        | | ___| |_ _ __ _   _ ___  ")
    print("        | |/ _ \\ __| '__| | | / __| ")
    print("        | |  __/ |_| |  | |_| \\__ \\ ")
    print("        \\_/\\___|\\__|_|   \\__,_|___/ ")
    print("\n\n\n\n")
    print_line()
    print(" 1: Commencer à jouer")
    print(" 2: Paramétrer le jeu")
    print("")
    print(" 3: Afficher les règles")
    print_line()


# définit les input de la page d'accueil
def input_home_page():
    choice = ""

    # On ne sort pas de cette fonction (donc du programme entier) qu'une fois qu'on a fini de configurer le jeu.
    while choice != "1":
        choice = input()
        if choice == "2":
            print_configuration()
            input_configuration()
        elif choice == "3":
            print_rules()
            input_rules()
    match game.shape:
        case "TRIANGLE":
            game.make_triangle()
        case "LOSANGE":
            game.make_losange()
        case "CERCLE":
            game.make_circle()


# print les règles du jeu
def print_rules():
    jump_page()
    print_line()
    print("     Tetrus, c'est quoi ?")
    print("")
    print("     Le principe est simple. Vous placez les blocs mis à votre disposition sur la grille de jeu.")
    print("")
    print("     Votre objectif est que la partie dure le plus longtemps (et ainsi, que vous ayez le meilleur score).")
    print(
        "     En effet, quand une ligne est remplie, elle est supprimée de la grille et vous gagnez des points. De même")
    print(
        "     pour les colonnes, mais une suppression de colonne a aussi pour effet de faire tomber les cases remplies")
    print("     n'ayant aucun support sous elles.")
    print("")
    print("     À chaque tour, vous disposez de trois essais pour entrer un placement de bloc valide. Si vous échouez trois fois de")
    print("     manière consécutive, vous perdez.")
    print("     Vous pouvez également arrêter une partie prématurément, en tapant \"0\" au lieu d'une lettre de bloc.")
    print("")
    print("     Vous avez à votre disposition différentes options que vous pouvez changer avant le début de la partie,")
    print("     tel que la taille du plateau, sa forme, ou les blocs mis à votre disposition à chaque tour.")
    print("")
    print(
        "     Enfin, vous avez également l'option à chaque fin de partie de sauvegarder votre partie pour la partager.")
    print("")
    print("")
    print("     Entrée: HOME")
    print_line()


# return à la page d'accueil au moindre input
def input_rules():
    input()
    print_homepage()


# print la page de configuration du jeu
def print_configuration():
    alea = "TOUS les blocs"
    if game.randomBlock:
        alea = "Blocs aléatoires"

    jump_page()
    print_line()
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
    print_line()


# définit les input de la page de configuration du jeu
def input_configuration():
    choice = ""

    reponses_possibles = ["1", "2", "3", "4", "5", "6", "7"]

    while choice not in reponses_possibles:
        choice = ""

        while choice != "7":
            choice = input()
            match choice:
                case "1":
                    game.shape = "TRIANGLE"
                    print_configuration()
                case "2":
                    game.shape = "LOSANGE"
                    print_configuration()
                case "3":
                    game.shape = "CERCLE"
                    print_configuration()
                case "4":
                    game.randomBlock = True
                    print_configuration()
                case "5":
                    game.randomBlock = False
                    print_configuration()
                case "6":
                    print_size_choice()
                    input_size_choice()

        print_homepage()


# print le message de saisie de la taille du plateau de jeu
def print_size_choice():
    jump_page()
    print_line()
    print(f"     Choisir la taille du plateau de jeu entre {minSize} et {maxSize}")
    print_line()


# définit les input du choix de la taille du plateau de jeu,tout nombre entre 21 et 16
def input_size_choice():
    okay = False

    while not okay:
        try:
            choice = input()
            if choice == "" or choice == "\n":
                print_configuration()
                return None

            choice = int(choice)
            if minSize <= choice <= maxSize:
                game.size = choice
                okay = True
            else:
                raise ValueError
        except ValueError:
            print("Veuillez écrire un nombre entre 21 et 26 inclus")

    print_configuration()


# exécute le programme et initialise des valeurs statiques
if __name__ == "__main__":

    minSize = 21
    maxSize = 26

    print_homepage()
    game = Game()
    input_home_page()

    # Une fois que le joueur lance la partie...
    game.setup()
    jump_page()

    while not game.ended:
        game.tick()
