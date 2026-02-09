

def show_grille(lst):
    for elt in lst:
        print(elt)

def show_voisin(grille,x, y):
    liste_voisins = []
    taille = len(grille)

    if x > 0 and grille[x-1][y] == False:
        liste_voisins.append([x-1, y,grille[x-1][y]])

    if x < taille-1 and grille[x+1][y] == False:
        liste_voisins.append([x+1, y,grille[x+1][y]])

    if y > 0 and grille[x][y-1] == False:
        liste_voisins.append([x, y-1,grille[x][y]-1])

    if y < taille-1 and grille[x][y+1] == False:
        liste_voisins.append([x, y+1,grille[x][y+1]])

    return liste_voisins



def contamine(grille,x,y):
    grille[x][y] = True


def get_contamine(grille,taille_x,taille_y):
    liste = []
    for i in range(taille_x):
        for j in range(taille_y):
            if grille[i][j] == True:
                liste.append([i,j])
    return liste


def cycle(grille):

    liste_contamine = get_contamine(grille, 100, 100)
    a_contaminer = []

    for element in liste_contamine:
        for elt in show_voisin(grille, element[0], element[1]):
            if elt[2] == False:
                a_contaminer.append([elt[0], elt[1]])

    for elt in a_contaminer:
        contamine(grille, elt[0], elt[1])
