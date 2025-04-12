import pygame, sys
pygame.init()

class Game:
    def __init__(self):
        self.width = 600
        self.height = 768
        self.scale_factor = 1.5
        self.win = pygame.display.set_mode((self.width, self.height))
        
        self.setBgAndGround()
        
        self.gameLoop()

    def gameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            
    def drawAll(self):
        self.win.blit(self.bg_img,(0,-300))
        self.win.blit(self.ground1_img, self.ground1_rect)
        self.win.blit(self.ground2_img, self.ground2_rect)

    def setBgAndGround(self):
        self.bg_img = pygame.transform.scale_by(pygame.image.load("assets/bg.png").convert(),self.scale_factor)
        self.ground1_img = pygame.transform.scale_by(pygame.image.load("assets/ground.png").convert(),self.scale_factor)
        self.ground2_img = pygame.transform.scale_by(pygame.image.load("assets/ground.png").convert(),self.scale_factor)
        
        self.ground1_rect = self.ground1_img.get_rect()
        self.ground2_rect = self.ground2_img.get_rect()
        
        self.ground1_rect.x = 0
        self.ground2_rect.x = self.ground1_rect.right
        self.ground1_rect.y = 700
        self.ground2_rect.y = 700
    
game = Game()