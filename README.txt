                            ╔═══════════════════════════════════════════════════════════╗
                            ║                                                           ║
                            ║    ████████╗███████╗████████╗██████╗ ██╗   ██╗███████╗    ║
                            ║    ╚══██╔══╝██╔════╝╚══██╔══╝██╔══██╗██║   ██║██╔════╝    ║
                            ║       ██║   █████╗     ██║   ██████╔╝██║   ██║███████╗    ║
                            ║       ██║   ██╔══╝     ██║   ██╔══██╗██║   ██║╚════██║    ║
                            ║       ██║   ███████╗   ██║   ██║  ██║╚██████╔╝███████║    ║
                            ║       ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ║
                            ║                                                           ║
                            ╚═══════════════════════════════════════════════════════════╝


Mise en garde ! Les caractères de différentes tailles sur PyCharm font bugger l'interface, nous ne vous conseillons pas cet IDE.
À la place, il est préférable d'y jouer à partir de Visual Studio Code, ou n'importe quelle console capable d'afficher
des caractères UTF-8 tous de la même largeur.



[Pour jouer] 
    - Installez Python 3.10.9

    - Exécutez main.py et laissez vous guider par les menus.

Note : Pour être sûr de pouvoir sauvegarder vos parties, ne placez pas les scripts dans un dossier d'administrateur.



Présentation :

Bienvenue sur Tetrus ! Un jeu où vous posez blocs pour détruire des lignes et gagner des points !
Ce jeu possède des similitudes avec Tetris.
Le principe est simple. Vous placez les blocs mis à votre disposition sur la grille de jeu.

Votre objectif est que la partie dure le plus longtemps (et ainsi, que vous ayez le meilleur score).
En effet, quand une ligne est remplie, elle est supprimée de la grille et vous gagnez des points. 
De même pour les colonnes, mais une suppression de colonne a aussi pour effet de faire tomber les cases remplies
n'ayant aucun support sous elles.

À chaque tour, vous disposez de trois essais pour entrer un placement de bloc valide. Si vous échouez trois fois de
manière consécutive, vous perdez. Pour sélectionner un bloc, il suffit d'entrer la lettre d'un 
des blocs proposés (elles sont affichées à côté de chaque bloc).
Vous pouvez également arrêter une partie prématurément, en tapant 0 au lieu d'une lettre de bloc.

Vous avez à votre disposition différentes options que vous pouvez changer avant le début de la partie,
tel que la taille du plateau, sa forme, ou les blocs mis à votre disposition à chaque tour.

Enfin, vous avez également l'option à chaque fin de partie de sauvegarder votre partie pour la partager.



Auteurs = ["Guillaume DELHAYE", "Idir NAIT MEDDOUR", "Tomas TARGE"]
