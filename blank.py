import pygame
import random as rd

COULEURBOARD1 = (255, 255, 255) #Couleur du plateau n1
COULEURBOARD2 = (0, 0, 0) #Couleur du plateau n2
COULEURSNAKE = (0, 255, 0) #Couleur du serpent
COULEURSCOREBOARD = (255, 0, 0) #Couleur du score board
COULEURFRUIT = (255, 0, 0) #Couleur des fruit

LEN=300 #largeur plateau
HEIGHT=400 #hauteur plateau
TILE=20 #taille des tuile

CLOCKF=6 #Vitesse du jeux/vitesse de l'horloge

TAILLEFONT=72 #taille du scoreboard
PLACEMENTSCOREBOARD=(186,3) #Placement du scoreboard

HAUT = (0,-1) #Création des vecteur direction
BAS = (0,1)
DROITE = (1,0)
GAUCHE = (-1,0)

snake=[(5,10),(6,10),(7,10)] #Liste modélisant le serpent 

snake_dir = DROITE #Inisialisation d'une direction de depart 
snakehead = snake[-1] 

game = {
    'mode':  "MODE_START",
    'score': 0
} # Mise en place d'un systeme de point 
# De plus possible amélioration furtur avec un systeme de restart  avec dictionnaire 'game'

def spwan_new_fruit(): #fonction créant les coordonnée d'un fruit sur le plateau placée aléatoirement 
    global fruit #Mise en place d'une variable global 
    fruit = [rd.randint(0,HEIGHT/TILE-1),rd.randint(0,LEN/TILE-1)]
    return 

spwan_new_fruit()

pygame.init()
screen = pygame.display.set_mode((HEIGHT,LEN))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Latex", TAILLEFONT) #Font du scoreboard


if game['mode'] == "MODE_START": #Debut du jeux
    while True:

        clock.tick(CLOCKF)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit(0)
                if event.key == pygame.K_UP:
                    snake_dir = HAUT
                if event.key == pygame.K_LEFT:
                    snake_dir = GAUCHE
                if event.key == pygame.K_RIGHT:
                    snake_dir = DROITE
                if event.key == pygame.K_DOWN:
                    snake_dir = BAS
            if event.type == pygame.WINDOWCLOSE :
                quit(0)
            pass

        screen.fill(COULEURBOARD1)
        
        for top in range(0,LEN,TILE):
            for left in range (0,HEIGHT,TILE):
                if (top + left )//20%2==0 :
                    rect = pygame.Rect(left, top, TILE, TILE)  #Creation du pavage 
                    pygame.draw.rect(screen, COULEURBOARD2, rect)  

        fruitpxl = pygame.Rect(fruit[0]*TILE, fruit[1]*TILE, TILE, TILE) 
        pygame.draw.rect(screen, COULEURFRUIT, fruitpxl) #Dessin du fruit ROUGE 

        snakehead = snake[-1]
        newsnakehead = [snakehead[0]+snake_dir[0],snakehead[1]+snake_dir[1]] 

        if newsnakehead == fruit:   #Prise en compte du contact avec les fruit on garde tout l'ancien Snake puis on rajoute juste la tête
            snake = snake + [newsnakehead]
            spwan_new_fruit() #ajoute d'un nouveau fruit sur le plateau 
            game['score'] += 1 # fruit= +1 au score 
        else :
            snake = snake[1:] + [newsnakehead]
        for i in range(len(snake)):
            snakdrw = pygame.Rect(snake[i][0]*TILE, snake[i][1]*TILE, TILE, TILE)
            pygame.draw.rect(screen, COULEURSNAKE, snakdrw)

        text = font.render(str(game['score']),1,COULEURSCOREBOARD) #Score board 
        screen.blit(text,PLACEMENTSCOREBOARD)   #Mise en place du texte sur l'ecran

        pygame.display.update()
