"""
string
"""
__author__ = 'Alex Hanson'
__version__ = 0.4
import pygame
import sys
import os
from pygame.locals import *
import platform
import random
import time
import datetime as timedelta

pygame.init()

win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Durr Burger Mini Game")

# if using darwin vs nt (mac vs new tech (windows))
if os.name == 'nt' and platform.system() == 'Windows':
    print('this game was tested on your platform and should run as intended.')
elif not (os.name == 'nt') and not ('darwin' in os.name):
    print('this game may not function as intended on your platform, or may function to varying degrees of success.')
if 'darwin' in os.name:
    print(
        'this game may not work on your platform as it is mostly untested on Mac OS. You may proceed, however I can not guarantee any success.')

clock = pygame.time.Clock()
gcache = globals()
cache = str(sys.getsizeof(gcache))
print(cache)
font = pygame.font.Font(None, 30)

player_img = pygame.image.load('images/player.png')
boss = pygame.image.load('images/boss.png')
projectile_img = pygame.image.load('images/projectile.png')
normal_bad = pygame.image.load('images/enemy.png')
bg1 = pygame.image.load('images/Black hole stars.png')
bg = pygame.image.load("images/Black hole.png")
exit_a = pygame.image.load('images/exit.png')
exit_b = pygame.image.load('images/exit hover.png')
exit_c = pygame.image.load('images/exit press.png')
scanlines = pygame.image.load('images/compress/vector scanlines.png')
exitbg = pygame.image.load('images/stars blur.png')
exitbox = pygame.image.load('images/box.png')
exitcnfrm_a = pygame.image.load('images/quit.png')
exitcnfrm_b = pygame.image.load('images/quit hover.png')
exitcnfrm_c = pygame.image.load('images/quit press.png')
back_a = pygame.image.load('images/back.png')
back_b = pygame.image.load('images/back hover.png')
back_c = pygame.image.load('images/back press.png')
shootsnd = pygame.mixer.Sound('music/PMB_Shoot_01.ogg')
pausesnd = pygame.mixer.Sound('music/nsmbwiiPause.ogg')
spawnsnd = pygame.mixer.Sound('music/PMB_Spawn_01.ogg')
score = 0
fps = 60
timer = 0
fpsc = 60
frm_time = 0.0
is_a_crashed = False
attacks = []
fpsavg = 0
fpsc = 60.0
cooldown = float(0)
bullets = []
exit_state = 'normal'

icon = pygame.image.load('images/boss.png')
pygame.display.set_icon(icon)

white = (255, 255, 255)
green = (0, 200, 0)
blue = (0, 160, 220)
black = (0, 0, 0)
red = (200, 0, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 255, 255)
purple = (255, 0, 255)

konami = [True, True, True, True, True, True, True, True, True, True]


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
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


pizza = player(360, 600, 64, 64)


def start():
    pygame.display.set_icon(icon)
    music = pygame.mixer.music.load('music/ambiance.ogg')
    pygame.mixer.music.play(-1)
    global konami
    win.blit(bg, (0, 0))
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
            win.blit(bg1, (0, 0))
            pygame.mixer.music.stop()
            music = pygame.mixer.music.load('music/tunes2.ogg')
            pygame.mixer.music.play(-1)
            spawnsnd.play()
            game()
        clock.tick(fps)
        pygame.display.flip()

def game():
    global projectiles
    global timer
    global fpsavg
    global fpsc
    global frm_time
    global exit_state
    global cooldown
    global bullets
    while not (is_a_crashed):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        fpsavg = clock.get_fps()
        timer += 1
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if 1140 + 130 > mouse[0] > 1140 and 646 + 64 > mouse[1] > 646:
            if click[0]:
                exit_state = 'click'
                redrawgamewindow()
                for i in range(0, 30):
                    pygame.event.pump()
                    pygame.time.delay(5)
                exit_function()
            else:
                exit_state = 'hover'
        else:
            exit_state = 'normal'
        if keys[pygame.K_p]:
            pause()
        if keys[pygame.K_a] and pizza.x > pizza.vel or keys[pygame.K_LEFT] and pizza.x > pizza.vel:
            pizza.x -= pizza.vel
        if keys[pygame.K_d] and pizza.x < 1280 - pizza.width - pizza.vel or keys[
            pygame.K_RIGHT] and pizza.x < 1280 - pizza.width - pizza.vel:
            pizza.x += pizza.vel
        for bullet in bullets:
            if bullet.y > -74:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
        if len(bullets) < 50 and time.time() - cooldown > float(0.322):
            if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
                cooldown = time.time()
                bullets.append(
                    projectile(pizza.x + 13, pizza.y, 25, 74))
                shootsnd.play()
        if timer == 60:
            timer = 0
        fpsc = (fpsavg // 1) + 2
        frm_time = clock.get_time()
        clock.tick(fps)
        redrawgamewindow()

def redrawgamewindow():
    updaterect = pygame.Rect(pizza.x - 32, pizza.y - 32, 96, 96)
    win.blit(bg1, (0, 0))
    for bullet in bullets:
        bullet.draw(win)
    pizza.draw(win)
    # projectile.draw(win)
    font = pygame.font.Font("fonts/Ailerons-Typeface.otf", 40)
    text = font.render("FPS:" + str(fpsc), True, white)
    win.blit(text, (5, 5))
    text = font.render("Frame time:" + str(frm_time) + 'ms', True, white)
    win.blit(text, (5, 55))
    smallText = pygame.font.Font("fonts/BurbankBigCondensed-Black.otf", 40)
    textSurf, textRect = text_objects('High Score', smallText, red)
    textRect.center = (1280 // 2, 35)
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(str(score), smallText, white)
    textRect.center = (1280 // 2, 80)
    win.blit(textSurf, textRect)
    # win.blit(scanlines, (0,0))
    if exit_state == 'normal':
        win.blit(exit_a, (1140, 646))
    if exit_state == 'hover':
        win.blit(exit_b, (1140, 646))
    if exit_state == 'click':
        win.blit(exit_c, (1140, 646))
    pygame.display.flip()
    if timer == 0:
        pygame.display.flip()
    else:
        pygame.display.update(updaterect)

def exit_function():
    pygame.mixer.music.pause()
    while not (False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        win.blit(exitbg, (0, 0))
        win.blit(exitbox, (287, 161))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 744 + 108 > mouse[0] > 744 and 476 + 54 > mouse[1] > 476:
            if click[0]:
                win.blit(exitcnfrm_c, (744, 476))
                win.blit(back_a, (865, 476))
                pygame.display.update()
                for i in range(0, 100):
                    pygame.event.pump()
                    pygame.time.delay(5)
                pygame.display.update()
                pygame.quit()
                sys.exit()

            else:
                win.blit(exitcnfrm_b, (744, 476))
        else:
            win.blit(exitcnfrm_a, (744, 476))
        if 865 + 108 > mouse[0] > 865 and 476 + 54 > mouse[1] > 476:
            if click[0]:
                win.blit(back_c, (865, 476))
                for i in range(0, 100):
                    pygame.event.pump()
                    pygame.time.delay(5)
                    pygame.display.update()
                pygame.mixer.music.unpause()
                game()
            else:
                win.blit(back_b, (865, 476))
        else:
            win.blit(back_a, (865, 476))
        pygame.display.update()
        pygame.event.pump()
        clock.tick(fps)


def pause():
    redrawgamewindow()
    pygame.mixer.music.pause()
    pausesnd.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            pygame.mixer.music.unpause()
            pausesnd.play()
            game()
        pygame.display.update()
        clock.tick(fps)


def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


if __name__ == '__main__':
    start()
