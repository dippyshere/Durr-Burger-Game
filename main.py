"""
string
"""
import pygame, sys, os, random, time
pygame.init()

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Durr Burger Mini Game")

clock = pygame.time.Clock()
gcache = globals()
cache = str(sys.getsizeof(gcache))
print(cache)

player_img = pygame.image.load('images/player.png')
boss = pygame.image.load('images/boss.png')
projectile_img = pygame.image.load('images/projectile.png')
normal_bad = pygame.image.load('images/enemy.png')
bg1 = pygame.image.load('images/black hole stars.png')
bg = pygame.image.load('images/black hole.png')
exit_a = pygame.image.load('images/exit.png')
exit_b = pygame.image.load('images/exit hover.png')
scanlines = pygame.image.load('images/scanlines.png')
score = 0
#music = pygame.mixer.music.load('audio/game.ogg')

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.shoot = False
        self.die = False
    def draw(self, win):
        win.blit(player_img, (self.x, self.y))
class projectile(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.timer = 120
    def draw(self, win):
        win.blit(projectile_img, (self.x, self.y))
    
pizza = (360, 650, 64, 64)

def start():
    win.blit(bg1, (0,0))
    pygame.display.flip()
    game()
def redrawGame():
    pizza.draw(win)
    #projectile.draw(win)
    pass

def game():
    is_a_crashed = True
    while not(is_a_crashed):
        clock.tick(60)
        redrawGame()
    pass

if __name__ == '__main__':
    start()
