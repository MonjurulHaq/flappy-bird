import pygame, sys, time
from bird import Bird
from pipe import Pipe
pygame.init()

class Game:
    def __init__(self):
        self.width = 600
        self.height = 768
        self.scale_factor = 1.5
        self.win = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.moveSpeed=250
        self.bird=Bird(self.scale_factor)
        self.is_enter_pressed = False
        self.pipes=[]
        self.pipes_counter = 71
        self.setBgAndGround()
        
        self.gameLoop()

    def gameLoop(self):
        last_time = time.time()
        while True:
            #calculating delta time
            new_time = time.time()
            dt = new_time-last_time
            last_time = new_time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.is_enter_pressed = True
                        self.bird.update_on = True
                    if event.key == pygame.K_SPACE and self.is_enter_pressed:
                        self.bird.flap(dt)
            
            self.updateAll(dt)
            self.checkCollisions()
            self.drawAll()
            pygame.display.update()
            self.clock.tick(60)
    
    def checkCollisions(self):
        if len(self.pipes):
            if self.bird.rect.bottom > 568:
                self.bird.update_on = False
                self.is_enter_pressed = False
            if (self.bird.rect.colliderect(self.pipes[0].rect_down) or 
            self.bird.rect.colliderect(self.pipes[0].rect_up)):
                self.is_enter_pressed = False
                
        
            
    def updateAll(self,dt):
        if self.is_enter_pressed:
            self.ground1_rect.x -= int(self.moveSpeed*dt)
            self.ground2_rect.x -= int(self.moveSpeed*dt)
            
            if self.ground1_rect.right<0:
                self.ground1_rect.x = self.ground2_rect.right
            if self.ground2_rect.right<0:
                self.ground2_rect.x = self.ground1_rect.right
            if self.pipes_counter>70:
                self.pipes.append(Pipe(self.scale_factor, self.moveSpeed))
                self.pipes_counter = 0
            self.pipes_counter+=1
            #moving pipes
            for pipe in self.pipes:
                pipe.update(dt)
            #removing pipes out of screen 
            if len(self.pipes)!=0:
                if self.pipes[0].rect_up.right<0:
                    self.pipes.pop(0)
                
        self.bird.update(dt)
            
    def drawAll(self):
        self.win.blit(self.bg_img,(0,-300))
        for pipe in self.pipes:
            pipe.drawPips(self.win)
        self.win.blit(self.ground1_img, self.ground1_rect)
        self.win.blit(self.ground2_img, self.ground2_rect)
        self.win.blit(self.bird.image,self.bird.rect)

    def setBgAndGround(self):
        self.bg_img = pygame.transform.scale_by(pygame.image.load("assets/bg.png").convert(),self.scale_factor)
        self.ground1_img = pygame.transform.scale_by(pygame.image.load("assets/ground.png").convert(),self.scale_factor)
        self.ground2_img = pygame.transform.scale_by(pygame.image.load("assets/ground.png").convert(),self.scale_factor)
        
        self.ground1_rect = self.ground1_img.get_rect()
        self.ground2_rect = self.ground2_img.get_rect()
        
        self.ground1_rect.x = 0
        self.ground2_rect.x = self.ground1_rect.right
        self.ground1_rect.y = 568
        self.ground2_rect.y = 568
    
game = Game()