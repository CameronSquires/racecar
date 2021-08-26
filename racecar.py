import pygame
import sys
import random

VEL = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30
SPEED = 6
WIDTH = 300
HEIGHT = 300
fpsClock = pygame.time.Clock()
GAMEDISPLAY = pygame.display.set_mode((WIDTH,HEIGHT))




class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((WIDTH/2, 250, 20, 20))
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            if self.rect.x >= 0:
                self.rect.move_ip(-SPEED, 0)
        if key[pygame.K_d]:
            if self.rect.x <= 280:
                self.rect.move_ip(SPEED, 0)
    def draw(self, gamescreen):
        pygame.draw.rect(GAMEDISPLAY, WHITE, self.rect)

class Obstacle(object):
    def __init__(self):
        self.rect = pygame.rect.Rect(random.randint(20, 280), 0, random.randint(30,85), random.randint(20,40))
    def move(self):
        self.rect.move_ip(0, -VEL)
    def draw(self, gamescreen):
        pygame.draw.rect(GAMEDISPLAY, WHITE, self.rect)
    def redraw(self):
        self.rect = pygame.rect.Rect(random.randint(20, 280), 0, random.randint(30,85), random.randint(20,40))


pygame.init()



pts = 0



def gameover():
    global VEL
    global SPEED
    global gameoverscreen
    VEL = 0
    SPEED = 0
    player.rect.move_ip(-999, 999)
    obs.rect.move_ip(-999, -999)
    gameoverscreen = "yes"
    


def spawnobs():
    obs.draw(GAMEDISPLAY)
    obs.redraw()


pygame.display.set_caption("RACECAR")

player = Player()
obs = Obstacle()

gameoverscreen = "no"

while True:
    GAMEDISPLAY.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    player.draw(GAMEDISPLAY)
    player.move()
    obs.draw(GAMEDISPLAY)
    obs.move()

    if player.rect.colliderect(obs):
        gameover()

    if obs.rect.y >= 300:
        pts += 1
        spawnobs()
    if gameoverscreen == "no":
        font = pygame.font.Font("Hhenum-Regular.otf", 22)
        scoredisplay = font.render((f"Score: {pts}"), 1, WHITE)
        GAMEDISPLAY.blit(scoredisplay, (10,10))
        VEL = -1 * (pts / 3 + 5)
    if gameoverscreen == "yes":    
        font = pygame.font.Font("Hhenum-Regular.otf", 22)
        scoredisplay = font.render((f"Game Over. Final Score: {pts}"), 1, WHITE)
        GAMEDISPLAY.blit(scoredisplay, (10,10))
        VEL = 0
    
    

    pygame.display.update()
    fpsClock.tick(FPS)