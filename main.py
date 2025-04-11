import pygame, sys
pygame.init()

class Game:
    def __init__(self):
        self.width = 500
        self.height = 680
        self.win = pygame.display.set_mode((self.width, self.height))
        self.gameLoop()

    def gameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

game = Game()