import pygame
import logging
import sys
import random as rd
import argparse

parser = argparse.ArgumentParser(description='Commande permettant de regler les different parametre du jeux')
parser.add_argument('--bg-color-1',default=(255,255,255) ,help="argument for the first color of the background checkerboard.")
parser.add_argument('--bg-color-2', default=(0,0,0),help="argument for the second color of the background checkerboard.")
parser.add_argument('--height', default=300 ,type=int,help="argument for the window height.")
parser.add_argument('--width', default=400 ,type=int,help="argument for the window width.")
parser.add_argument('--fps', default=6 ,type=int,help="argument for the number of frames per second.")
parser.add_argument('--tile-size', default=20 ,type=int,help="argument the size of a square tile.")
parser.add_argument('--fruit-color', default=(255, 0, 0),help="argument the size of a square tile.")
parser.add_argument('--snake-length', default=3 ,type=int,help="argument the size of a square tile.")
parser.add_argument('--snake-color', default=(0, 255, 0) ,help="argument the size of a square tile.")
parser.add_argument('--gameover-on-exit',help='A flag.', action='store_true')
parser.add_argument('-g', '--debug',default=False , help='Set debug mode.',action='store_true')

args = parser.parse_args()
print(args)


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stderr)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
if args.debug:
    logger.setLevel(logging.DEBUG)


#CONSTANTE
COULEURSCOREBOARD = (255,0,0)#Couleur du score board
TAILLEFONT=72 #taille du scoreboard
PLACEMENTSCOREBOARD=(0,0) #Placement du scoreboard
FRUIT_1 = [3, 3]
FRUIT_2 = [10,10]
HAUT = (0,-1) #Création des vecteur direction
BAS = (0,1)
DROITE = (1,0)
GAUCHE = (-1,0)
snake=[]

for i in range (args.snake_length):
    snake+= [(i,0)] #Liste modélisant le serpent 

snake_dir = DROITE #Inisialisation d'une direction de depart 
snakehead = snake[-1] 

game = {
    'mode':  "MODE_START",
    'score': 0
} # Mise en place d'un systeme de point 
# De plus possible amélioration furtur avec un systeme de restart  avec dictionnaire 'game'

pygame.init()
screen = pygame.display.set_mode((args.width,args.height))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Latex", TAILLEFONT) #Font du scoreboard

logger.debug("Start main loop.")

fruit = FRUIT_1


if True==True :        
    while True:

        clock.tick(args.fps)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    logger.info("Game over.")
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
                logger.info("Game over.")
                quit(0)
            pass

        screen.fill(args.bg_color_1)
            
        for top in range(0,args.height,args.tile_size):
            for left in range (0,args.width,args.tile_size):
                if (top + left )//args.tile_size%2==0 :
                    rect = pygame.Rect(left, top, args.tile_size, args.tile_size)  #Creation du pavage 
                    pygame.draw.rect(screen, args.bg_color_2, rect)  
                        

        snakehead = snake[-1]
        if snakehead in snake[:-1]: #Regarde si la tête est appartient au coprs et si oui fini le jeux 
            logger.info("Game over - Snake collided with itself.")
            quit(0)
        
        newsnakehead = [snakehead[0]+snake_dir[0],snakehead[1]+snake_dir[1]] 
            
        if args.gameover_on_exit==True:
            if newsnakehead[0]<0 or newsnakehead[1]<0 or newsnakehead[0]*args.tile_size>args.width or newsnakehead[1]*args.tile_size>args.height :
                logger.info("Game over.")
                quit(0)
        else :
            if newsnakehead[0]*args.tile_size>args.width:
                newsnakehead = [newsnakehead[0]-args.width/args.tile_size-1,newsnakehead[1]]
            if newsnakehead[0]<0:
                newsnakehead = [newsnakehead[0]+args.width/args.tile_size,newsnakehead[1]]
            if newsnakehead[1]*args.tile_size>args.height :
                newsnakehead = [newsnakehead[0],newsnakehead[1]-args.height/args.tile_size-1]
            if newsnakehead[1]<0:
                newsnakehead = [newsnakehead[0],newsnakehead[1]+args.height/args.tile_size]
            

        if newsnakehead == fruit:   #Prise en compte du contact avec les fruit on garde tout l'ancien Snake puis on rajoute juste la tête
            snake = snake + [newsnakehead]
            if fruit == FRUIT_1 :
                fruit = FRUIT_2 
            else :
                fruit = FRUIT_1
            logger.debug("Snake has eaten a fruit.")
            print(fruit)
            game['score'] += 1 # fruit= +1 au score 
        else :
            snake = snake[1:] + [newsnakehead]

        text = font.render(str(game['score']),1,COULEURSCOREBOARD) #Score board 
        screen.blit(text,PLACEMENTSCOREBOARD)   #Mise en place du texte sur l'ecran

        fruitpxl = pygame.Rect(fruit[0]*args.tile_size, fruit[1]*args.tile_size, args.tile_size, args.tile_size) 
        pygame.draw.rect(screen, args.fruit_color, fruitpxl) #Dessin du fruit ROUGE 

        for i in range(len(snake)):
            snakdrw = pygame.Rect(snake[i][0]*args.tile_size, snake[i][1]*args.tile_size, args.tile_size, args.tile_size)
            pygame.draw.rect(screen, args.snake_color, snakdrw)


        pygame.display.update()
