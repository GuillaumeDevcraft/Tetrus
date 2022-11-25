from math import *

b10 = [[1]]

b20 = [[1, 1],
       [1, 1]]
b21 = [[1, 0],
       [1, 1]]
b22 = [[0, 1],
       [1, 1]]
b23 = [[0, 1],
       [0, 1]]

b30 = [[1, 0, 0],
       [1, 0, 0],
       [1, 1, 1]]
b31 = [[0, 0, 1],
       [0, 0, 1],
       [1, 1, 1]]
b32 = [[1, 0, 1],
       [1, 1, 0],
       [1, 0, 0]]
b33 = [[0, 1, 0],
       [0, 1, 1],
       [0, 0, 1]]
b34 = [[0, 0, 1],
       [0, 1, 1],
       [0, 1, 0]]
b35 = [[0, 1, 0],
       [0, 1, 0],
       [0, 1, 0]]
b36 = [[0, 0, 1],
       [0, 1, 0],
       [1, 0, 0]]
b37 = [[0, 1, 0],
       [1, 1, 1],
       [0, 1, 0]]

b40 = [[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]]
b41 = [[0, 1, 1, 0],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 1, 1, 0]]
b42 = [[1, 0, 0, 1],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [1, 1, 1, 1]]
b43 = [[1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]
b44 = [[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]]
b45 = [[0, 0, 0, 0],
       [1, 0, 0, 1],
       [1, 0, 0, 1],
       [1, 1, 1, 1]]
b46 = [[1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 1, 1, 1]]
b47 = [[1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 1],
       [1, 1, 1, 1]]
b48 = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 1, 1, 0]]
b49 = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 1, 1, 1]]
b410 = [[1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 0, 1]]
b411 = [[0, 0, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 1]]
b412 = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 1, 1]]
b413 = [[1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
b414 = [[0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 0],
        [1, 1, 0, 0]]
b415 = [[1, 1, 1, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0]]

b50 = [[1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0],
       [1, 0, 0, 0, 0]]

board = open("board.txt", "a")

def triangle(d):
    par = d % 2

    for y in range(d):
        for x in range(d * 2 + par):
            if (x < d - y - 1 + par or x > d + y):
                board.write("0  ")
            else:
                board.write("1  ")

        board.write("\n")


f = open("board.txt", "a")

def losange(d):
    mid = d / 2
    par = d % 2

    for y in range(d):
        for x in range(d):
            if (y <= d / 2):
                if (x > mid - y - 2 + par and x < mid + y - par + 1):
                    board.write("1  ")
                else:
                    board.write("0  ")
            else:
                if (x > -d + mid + y - 1 + par and x < d - y + mid - par):
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
            if (sqrt((x - center) ** 2 + (y - center) ** 2) < d / 2):
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
    printLine()
    print(" 1: Commencer à jouer")
    print(" 2: Règles du jeu")
    printLine()


size = 21
form = "TRIANGLE"
randomBloc = True


def printConfiguration():
    printLine()
    print("     Choisir forme du plateau")
    print("         1 : Triangle")
    print("         2 : Losange")
    print("         3 : Cercle")
    print("     Choisir Règles du jeu")
    print("         4 : Blocs aléatoires")
    print("         5 : TOUT les blocs")
    print("")
    print("         6 : LANCER")
    printLine()


def inputSize():
    while size < 21 or size > 26:
        printLine()
        print("     Choisir la Taille du plateau de jeu Entre :")
        print("         min 21")
        print("         max 26")
        printLine()
        size = int(input())


def printGameboard():
    print(end="     ")
    for i in range(1,10):
        print(i, end="  ")
    for i in range(10,size):
        print(i, end=" ")
    print(size)

    for i in range(size):
        print(end="  ")
    print("")

    board = open("board.txt", "r")
    lines = board.readlines()
    for i in range(1,size + 1):
        space = "   "
        if(i<10):
            space +=" "
        print(i, end=space)
        line = lines[i - 1]
        line = line.replace("1", "ᴥ")
        line = line.replace("0", " ")

        print(line,end="")

printConfiguration()