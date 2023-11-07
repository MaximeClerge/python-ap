import pygame

white = (255, 255, 255) 
black = (0, 0, 0)
sreensize=(400, 300)
clockf=0
k=20
l=0
pygame.init()

screen = pygame.display.set_mode(sreensize)

clock = pygame.time.Clock()

while True:

    clock.tick(clockf)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit()
        if event.type == pygame.WINDOWCLOSE :
            quit()
        pass

    screen.fill(white)

    while l<300:
        while k<400:
            rect = pygame.Rect(k, l, 20, 20)
            pygame.draw.rect(screen, black, rect)
            pygame.display.update()
            k+=40
            print(k)
        if k == 400:
            k=20
        else :
            k=0
        l+=20
