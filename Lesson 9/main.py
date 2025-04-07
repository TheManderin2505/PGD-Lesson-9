import pygame

pygame.init()

SCREENWIDTH = 800
SCREENHEIGHT = 600


SCREEN = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])
pygame.display.set_caption("Sprite Test 1")

while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        #if event.type == pygame.