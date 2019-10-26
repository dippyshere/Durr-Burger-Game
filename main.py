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
elif not(os.name == 'nt') and not('darwin' in os.name):
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
timer = 0

white = (255, 255, 255)
green = (0, 200, 0)
blue = (0, 160, 220)
black = (0, 0, 0)
red = (200,0,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,255,255)
purple = (255,0,255)

konami = [True, True, True, True, True, True, True, True, True, True]
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
    global konami
    win.blit(bg, (0,0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            konami[0] = True
            konami[1] = True
        if keys[pygame.K_DOWN]:
            konami[2] = True
            konami[3] = True
        if keys[pygame.K_LEFT]:
            konami[4] = True
            konami[6] = True
        if keys[pygame.K_RIGHT]:
            konami[5] = True
            konami[7] = True
        if keys[pygame.K_b]:
            konami[8] = True
        if keys[pygame.K_a]:
            konami[9] = True
        if keys[pygame.K_RETURN] and all(konami) == True:
            win.blit(bg1, (0,0))
            game()
        clock.tick(fps)
        pygame.display.flip()
def redrawgamewindow():
    smallText = pygame.font.Font("fonts/Ailerons-Typeface.otf",40)
    textSurf, textRect = text_objects("FPS: " + str(fpsc), smallText)
    textRect.center = (200, 200)
    win.blit(textSurf, textRect)
    updaterect = pygame.Rect(pizza.x - 32, pizza.y - 32, 96, 96)
    win.blit(bg1, (0,0))
    pizza.draw(win)
    pygame.event.pump()
    #projectile.draw(win)
    pygame.display.flip()
    #if timer == 0:
    #    pygame.display.flip()
    #else:
    #    pygame.display.update(updaterect)

def game():
    global timer
    global fpsc
    is_a_crashed = False
    while not(is_a_crashed):
        fpsc = clock.get_fps()
        timer += 1
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():                                                                                                                          
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if keys[pygame.K_RETURN]:
            print('pause')
        if keys[pygame.K_a] or keys[pygame.K_LEFT] and pizza.x > pizza.vel:
            pizza.x -= pizza.vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and pizza.x < 1280 - pizza.width - pizza.vel:
            pizza.x += pizza.vel
        if timer == 60:
            timer = 0
        clock.tick(fps)
        redrawgamewindow()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

if __name__ == '__main__':
    start()