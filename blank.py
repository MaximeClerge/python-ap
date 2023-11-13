import pygame
from time import sleep
import random as rd

WHITE = (255, 255, 255) #Couleur Blanche RGB
BLACK = (0, 0, 0) #Couleur Noir RGB
GREEN = (0, 255, 0) #Couleut Verte RGB
RED = (255, 0, 0) #Couleut Rouge RGB
LEN=300
HEIGHT=400
clockf=3 #Vitesse du jeux/vitesse de l'horloge
TILE=20

snake=[(5,10),(6,10),(7,10)] #Liste modélisant le serpent 

HAUT = (0,-1)
BAS = (0,1)
DROIT = (1,0)
GAUCHE = (-1,0)

snake_dir = DROIT
snakehead = snake[-1]

def spwan_new_fruit(): #fonction créant les coordonnée d'un fruit sur le plateau placée aléatoirement 
    global fruit
    fruit = [rd.randint(0,19),rd.randint(0,14)]
    return 

spwan_new_fruit()

pygame.init()
screen = pygame.display.set_mode((HEIGHT,LEN))
clock = pygame.time.Clock()
  
while True:

    clock.tick(clockf)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit(0)
            if event.key == pygame.K_w:
                snake_dir = HAUT
            if event.key == pygame.K_a:
                snake_dir = GAUCHE
            if event.key == pygame.K_d:
                snake_dir = DROIT
            if event.key == pygame.K_s:
                snake_dir = BAS
        if event.type == pygame.WINDOWCLOSE :
            quit(0)
        pass

    screen.fill(WHITE)
    
    for top in range(0,LEN,TILE):
        for left in range (0,HEIGHT,TILE):
            if (top + left )//20%2==0 :
                rect = pygame.Rect(left, top, TILE, TILE)  #Creation du pavage 
                pygame.draw.rect(screen, BLACK, rect)  

    fruitpxl = pygame.Rect(fruit[0]*TILE, fruit[1]*TILE, TILE, TILE) 
    pygame.draw.rect(screen, RED, fruitpxl)

    snakehead=snake[-1]
    newsnakehead = [snakehead[0]+snake_dir[0],snakehead[1]+snake_dir[1]]

    if newsnakehead == fruit:
        snake = snake + [newsnakehead]
        spwan_new_fruit()
    else :
        snake = snake[1:] + [newsnakehead]
    for i in range(len(snake)):
        snakdrw = pygame.Rect(snake[i][0]*TILE, snake[i][1]*TILE, TILE, TILE)
        pygame.draw.rect(screen, GREEN, snakdrw)


    pygame.display.update()
