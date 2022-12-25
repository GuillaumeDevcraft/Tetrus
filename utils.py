# Projet Tetrus Guillaume DELHAYE Idir NAIT MEDDOUR Tomas TARGE
# Fichier de fonctions utilitaires
from main import alphabet


# fait tourner une matrice <matrix> d'un certains angle <rot>
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

    # sélectionne le bloc correspondant à la lettre donnée <wanted_block> parmi ceux proposés <options>


def select_block(options, wanted_block):
    while True:
        if len(wanted_block) == 1:
            if wanted_block[0] in alphabet:
                try:
                    chosen_block_arr = options[alphabet.index(wanted_block[0])]
                    break
                except IndexError:
                    pass
            elif wanted_block == "0":
                return None

        print("Votre réponse n'est pas valide. Veuillez choisir entre : " + ", ".join(alphabet[:len(options)]))
        wanted_block = input().lower()
    return chosen_block_arr


# demande au joueur de faire tourner un bloc <block> d'un certains angle
def rotate_block(block):
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


# print un <block> dans la console sous la forme de carrés pleins <◼>
def print_block(block):
    for i in range(len(block)):
        print("  ".join(["◼" if n == 1 else " " for n in block[i]]))


def trim_matrix(matrix, forbidden=0):
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
            try:  # Au cas où <matrix> n'est pas rectangulaire, on met quelque chose pour remplacer
                ligne.append(matrix[x][y])
            except IndexError:
                ligne.append(0)  # Valeur arbitraire de remplacement, choisie pour les besoins du Tetrus
        result.append(ligne)

    return result


assert trim_matrix([
    [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]) == [[1, 1, 1, 0, 1, 0],
       [0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1]
       ]

