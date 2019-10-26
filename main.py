"""
string
"""
import os
import platform
import pygame
import sys

pygame.init()

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Durr Burger Mini Game")

#if using darwin vs nt (mac vs new tech (windows))
if os.name == 'nt' and platform.system() == 'Windows':
    print('this game was tested on your platform and should run as intended.')
elif not(os.name == 'nt') and not('darwin' in os.name)
    print('this game may not function as intended on your platform, or may function to varying degrees of success.')
if 'darwin' in os.name:
    print('this game may not work on your platform as it is mostly untested on Mac OS. You may proceed, however I can not guarantee any success.')

clock = pygame.time.Clock()
gcache = globals()
cache = str(sys.getsizeof(gcache))
print(cache)

player_img = pygame.image.load('images/player.png')
boss = pygame.image.load('images/boss.png')
projectile_img = pygame.image.load('images/projectile.png')
normal_bad = pygame.image.load('images/enemy.png')
bg1 = pygame.image.load('images/Black hole stars.png')
bg = pygame.image.load("images/Black hole.png")
exit_a = pygame.image.load('images/exit.png')
exit_b = pygame.image.load('images/exit hover.png')
scanlines = pygame.image.load('images/scanlines.png')
score = 0
fps = 60
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
    
pizza = player(360, 650, 64, 64)

def start():
    win.blit(bg1, (0,0))
    pygame.display.flip()
    game()
def redrawgamewindow():
    pizza.draw(win)
    pygame.event.pump()
    #projectile.draw(win)
    pass

def game():
    is_a_crashed = False
    while not(is_a_crashed):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if keys[pygame.K_RETURN]:
            print('pause')
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            print('left')
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            print('right')
        clock.tick(fps)
        redrawgamewindow()

if __name__ == '__main__':
    start()