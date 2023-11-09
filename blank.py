import pygame
from time import sleep

white = (255, 255, 255) #Couleur Blanche RGB
black = (0, 0, 0) #Couleur Noir RGB
green = (0, 255, 0) #Couleut Verte RGB
sreensize=(400, 300) #taille ecran 
clockf=0 #Vitesse du jeux/vitesse de l'horloge

left=20
top=0

Pos=[]  #Creation d'une liste avec la position de tout les carreau du plateau
ligne=[]
for i in range(0,400,20):
    for j in range(0,300,20):
        ligne.append(j)
    Pos.append(ligne)
    ligne=[]

pygame.init()

screen = pygame.display.set_mode(sreensize)

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
    
    while top<300:
        while left<400:
            rect = pygame.Rect(left, top, 20, 20)  #Creation du pavage 
            pygame.draw.rect(screen, black, rect)   
            left+=40
        if left == 400:
            left=20
        else :
            left=0
        top+=20

        for l in range(0,3): #Creation du serpent
            snake=pygame.Rect(Pos[5+l][5+l], Pos[10][10], 20, 20)
            pygame.draw.rect(screen, green, snake)
            pygame.display.update()