import pygame

white = (255, 255, 255) 
black = (0, 0, 0)
sreensize=(400, 300)
clockf=0

left=20
top=0

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

    while top<300:
        while left<400:
            rect = pygame.Rect(left, top, 20, 20)
            pygame.draw.rect(screen, black, rect)
            pygame.display.update()
            left+=40
        if left == 400:
            left=20
        else :
            left=0
        top+=20