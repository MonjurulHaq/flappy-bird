import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, sclar_factor):
        super(Bird,self).__init__()
        self.img_list = [pygame.transform.scale_by(pygame.image.load("assets/birdup.png").convert_alpha(),sclar_factor),
                         pygame.transform.scale_by(pygame.image.load("assets/birddown.png").convert_alpha(),sclar_factor)]
        self.image_index = 0
        self.image = self.img_list[self.image_index]
        self.rect = self.image.get_rect(center = (100,100))
        self.y_speed = 0
        self.gravity = 10
        self.flap_speed = 250
        
    def update(self, dt):
        self.applyGravity(dt)
    
    def applyGravity(self, dt):
        self.y_speed += self.gravity *dt
        self.rect.y += self.y_speed