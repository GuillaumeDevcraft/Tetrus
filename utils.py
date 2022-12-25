#Projet Tetrus Guillaume DELHAYE Idir NAIT MEDDOUR Tomas TARGE
#Fichier de fonctions utilitaires
def getBoardInMatrice(size):
    matrice = []
    board = open("board.txt", "r")
    lines = board.readlines()

    for l in lines:
        matrice.append(l.split("  ").pop(size - 1))

    return matrice


def valid_position(grid, bloc, i, j):
    output = True
    if len(bloc) > len(grid) - i + 1:  # vérif si pas out of range en hauteur
        return False
    if len(bloc) > len(grid[0]) - j + 1:  # vérif pas out of range en longueur
        return False
    for k in range(len(bloc)):
        for l in range(len(bloc)):
            if bloc[k][l] == 1 and grid[i + k][j + l] != 1:
                output = False
    return output


def rotate_bloc(bloc, dir):
    return dir
