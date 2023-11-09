import pygame
from time import sleep

white = (255, 255, 255) #Couleur Blanche RGB
black = (0, 0, 0) #Couleur Noir RGB
green = (0, 255, 0) #Couleut Verte RGB
LEN=300
HEIGHT=400
clockf=0 #Vitesse du jeux/vitesse de l'horloge
tile=20
left=20
top=0

snake=[(5,10),(6,10),(7,10)]

Pos=[]  #Creation d'une liste avec la position de tout les carreau du plateau
ligne=[]
for i in range(0,400,20):
    for j in range(0,300,20):
        ligne.append(j)
    Pos.append(ligne)
    ligne=[]

pygame.init()

screen = pygame.display.set_mode((HEIGHT,LEN))

clock = pygame.time.Clock()

while True:

    clock.tick(clockf)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit(0)
        if event.type == pygame.WINDOWCLOSE :
            quit(0)
        pass

    screen.fill(white)
    
    for top in range(0,LEN,tile):
        for left in range (0,HEIGHT,tile):
            if (top + left )//20%2==0 :
                rect = pygame.Rect(left, top, tile, tile)  #Creation du pavage 
                pygame.draw.rect(screen, black, rect)   

    
    pygame.display.update()
