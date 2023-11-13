import pygame
from time import sleep

WHITE = (255, 255, 255) #Couleur Blanche RGB
BLACK = (0, 0, 0) #Couleur Noir RGB
GREEN = (0, 255, 0) #Couleut Verte RGB
LEN=300
HEIGHT=400
clockf=3 #Vitesse du jeux/vitesse de l'horloge
TILE=20

snake=[(5,10),(6,10),(7,10)]

HAUT = (0,-1)
BAS = (0,1)
DROIT = (1,0)
GAUCHE = (-1,0)

snake_dir = DROIT
snakehead = snake[-1]

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


    snakehead=snake[-1]
    newsnakehead = [snakehead[0]+snake_dir[0],snakehead[1]+snake_dir[1]]
    snake = snake[1:] + [newsnakehead]

    snakdrw = pygame.Rect(snake[0][0]*TILE, snake[0][1]*TILE, TILE, TILE)
    pygame.draw.rect(screen, GREEN, snakdrw)
    snakdrw = pygame.Rect(snake[1][0]*TILE, snake[1][1]*TILE, TILE, TILE)
    pygame.draw.rect(screen, GREEN, snakdrw)
    snakdrw = pygame.Rect(snake[2][0]*TILE, snake[2][1]*TILE, TILE, TILE)
    pygame.draw.rect(screen, GREEN, snakdrw)


    pygame.display.update()
