import pygame

pygame.init()

SCREENWIDTH = 800
SCREENHEIGHT = 600


SCREEN = pygame.display.set_mode([SCREENWIDTH,SCREENHEIGHT])
pygame.display.set_caption("Sprite Test 1")

class Player(pygame.sprite.Sprite):
    #property
    def __init__(self):
        #super extracts stuff from sprite
        super().__init__()
        self.image = pygame.image.load("rocket.png")
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect =  self.image.get_rect()

        #function
        def update(self,keys_pressed):
            if(keys_pressed[pygame.K_UP]):
                self.rect.move_ip(0,-5)

            if(keys_pressed[pygame.K_DOWN]):
                self.rect.move_ip(0,5)

            if(keys_pressed[pygame.K_LEFT]):
                self.rect.move_ip(-5,0)
            
            if(keys_pressed[pygame.K_RIGHT]):
                self.rect.move_ip(5,0)

            #Boundary
            if self.rect.left < 0:
                self.rect.left = 0
            
            if self.rect.right > SCREENWIDTH:
                self.rect.right = SCREENWIDTH

            if self.rect.top < 0:
                self.rect.top = 0
            
            if self.rect.bottom > SCREENHEIGHT:
                self.rect.bottom= SCREENHEIGHT

#create a group

spriteg = pygame.sprite.Group()            
            
def game_start():

    while True:
        #create object
        rocket = Player()
        spriteg.add(rocket)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys_pressed= pygame.key.get_pressed()
        rocket.update(keys_pressed)

        SCREEN.blit(pygame.image.load("space.png"),(0,0))
        spriteg.draw(SCREEN)  
        pygame.display.update()


game_start()