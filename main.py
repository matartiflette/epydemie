from functions import *
from time import *
import pygame
import sys

pygame.init()

# Paramètres

TAILLE_CASE = 30
grille = [[False]*10 for _ in range(10)]
lignes = len(grille)
colonnes = len(grille[0])

largeur = colonnes * TAILLE_CASE
hauteur = lignes * TAILLE_CASE

screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Grille depuis liste")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (50, 150, 255)


grille[2][2] = True


clock = pygame.time.Clock()
CYCLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CYCLE_EVENT, 1000)  # 1 seconde


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == CYCLE_EVENT:
            cycle(grille)

        screen.fill(BLANC)

    for y in range(lignes):
        for x in range(colonnes):
            rect = pygame.Rect(
                x * TAILLE_CASE,
                y * TAILLE_CASE,
                TAILLE_CASE,
                TAILLE_CASE
            )

            if grille[y][x] == True:
                pygame.draw.rect(screen, BLEU, rect)

            pygame.draw.rect(screen, NOIR, rect, 1)  # contour

    pygame.display.flip()
    clock.tick(60)



