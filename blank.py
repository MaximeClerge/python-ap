import pygame

white = (255, 255, 255) 
black = (0, 0, 0)
sreensize=(400, 300)
clockf=0
k=20
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

    while k<380:
        k = k + 40
        rect = pygame.Rect(int(k), 0, 20, 20)
    pygame.draw.rect(screen, black, rect)

    pygame.display.update()
