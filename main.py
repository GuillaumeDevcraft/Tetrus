from math import *

# m = Matrice
# n1_n2 : n1 est l'angle et n2 la taille de la matrice

mPoint = [[1]]

mCarre_2 = [[1, 1],
            [1, 1]]
mL_2 = [[1, 0],
        [1, 1]]
mLInverse_2 = [[0, 1],
               [1, 1]]
mVertical_2 = [[1, 0],
               [1, 0]]

mL_3 = [[1, 0, 0],
        [1, 0, 0],
        [1, 1, 1]]
mLInverse_3 = [[0, 0, 1],
               [0, 0, 1],
               [1, 1, 1]]
mV_3 = [[1, 0, 1],
        [1, 1, 0],
        [1, 0, 0]]
mVInverse_3 = [[0, 1, 0],
               [0, 1, 1],
               [0, 0, 1]]
mZ90_3 = [[0, 1, 0],
          [1, 1, 0],
          [1, 0, 0]]
mVertical_3 = [[1, 0, 0],
               [1, 0, 0],
               [1, 0, 0]]
mBarre_3 = [[0, 0, 1],
            [0, 1, 0],
            [1, 0, 0]]
mPlus_3 = [[0, 1, 0],
           [1, 1, 1],
           [0, 1, 0]]

mCarre_4 = [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]
mPlus_4 = [[0, 1, 1, 0],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [0, 1, 1, 0]]
mU_4 = [[1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]]
mVertical_4 = [[1, 0, 0, 0],
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
maxSize = 26
minSize = 21
randomBlock = True;
size = 21
form = "TRIANGLE"


def triangle(d):
    par = d % 2

    for y in range(d):
        for x in range(d * 2 + par):
            if x < d - y - 1 + par or x > d + y:
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
            printGameboard()
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
    print("     Choisir forme du plateau :      "+form)
    print("         1 : Triangle")
    print("         2 : Losange")
    print("         3 : Cercle")
    print("     Choisir Règles du jeu :         "+alea)
    print("         4 : Blocs aléatoires")
    print("         5 : TOUT les blocs")
    print("")
    print("         6 : LANCER")
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
    print("         min "+str(minSize))
    print("         max "+str(maxSize))
    printLine()

def inputSizeChoice():
    try:
        choice = int(input())
        if(minSize<choice<maxSize):
            size = choice
            printGameboard()
        else:
            inputSizeChoice()

    except ValueError:
        inputSizeChoice()


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

printHomepage()