"""
string
"""
from typing import Union, List, Any, Tuple

from pygame.font import FontType
from pygame.ftfont import Font

__author__ = 'Alex Hanson'
__version__ = 1.0
import pygame
import sys
import os
# from pygame.locals import *
import platform
import random
import time

pygame.init()

win: None = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Durr Burger Mini Game")

# if using darwin vs nt (mac vs new tech (windows))
if os.name == 'nt' and platform.system() == 'Windows':
    print('this game was tested on your platform and should run as intended.')
elif not (os.name == 'nt') and not ('darwin' in os.name):
    print('this game may not function as intended on your platform, or may function to varying degrees of success.')
if 'darwin' in os.name:
    print(
        "this game may not work on your platform as it is mostly untested on Mac OS. You may proceed, however I can "
        "not guarantee any success.")

clock = pygame.time.Clock()
gcache = globals()
cache = str(sys.getsizeof(gcache))
print(cache)
font = pygame.font.Font(None, 30)

player_img = pygame.image.load('images/player.png')
boss = pygame.image.load('images/boss.png')
projectile_img = pygame.image.load('images/projectile.png')
normal_bad = pygame.image.load('images/enemy.png')
bg1 = pygame.image.load('images/Black hole stars.png').convert()
bg = pygame.image.load("images/Black hole.png").convert()
exit_a = pygame.image.load('images/exit.png')
exit_b = pygame.image.load('images/exit hover.png')
exit_c = pygame.image.load('images/exit press.png')
# scanlines = pygame.image.load('images/compress/vector scanlines.png')
exitbg = pygame.image.load('images/stars blur.png').convert()
exitbox = pygame.image.load('images/box.png')
exitcnfrm_a = pygame.image.load('images/quit.png')
exitcnfrm_b = pygame.image.load('images/quit hover.png')
exitcnfrm_c = pygame.image.load('images/quit press.png')
back_a = pygame.image.load('images/back.png')
back_b = pygame.image.load('images/back hover.png')
back_c = pygame.image.load('images/back press.png')
splatter: object = pygame.image.load('images/splat.png')
shootsnd = pygame.mixer.Sound('music/PMB_Shoot_01.ogg')
pausesnd = pygame.mixer.Sound('music/nsmbwiiPause.ogg')
spawnsnd = pygame.mixer.Sound('music/PMB_Spawn_01.ogg')
deathsnd = pygame.mixer.Sound('music/PMB_Death_01.ogg')
hitsnd = pygame.mixer.Sound('music/PMB_Explo_01.ogg')
enemy = [pygame.image.load('images/enemy/Frame 1.png'), pygame.image.load('images/enemy/Frame 2.png'),
         pygame.image.load('images/enemy/Frame 3.png'), pygame.image.load('images/enemy/Frame 4.png'),
         pygame.image.load('images/enemy/Frame 5.png'), pygame.image.load('images/enemy/Frame 6.png'),
         pygame.image.load('images/enemy/Frame 7.png'), pygame.image.load('images/enemy/Frame 8.png'),
         pygame.image.load('images/enemy/Frame 9.png'), pygame.image.load('images/enemy/Frame 10.png'),
         pygame.image.load('images/enemy/Frame 11.png'), pygame.image.load('images/enemy/Frame 12.png'),
         pygame.image.load('images/enemy/Frame 13.png'), pygame.image.load('images/enemy/Frame 14.png'),
         pygame.image.load('images/enemy/Frame 15.png'), pygame.image.load('images/enemy/Frame 16.png'),
         pygame.image.load('images/enemy/Frame 17.png'), pygame.image.load('images/enemy/Frame 18.png'),
         pygame.image.load('images/enemy/Frame 19.png'), pygame.image.load('images/enemy/Frame 20.png'),
         pygame.image.load('images/enemy/Frame 21.png'), pygame.image.load('images/enemy/Frame 22.png'),
         pygame.image.load('images/enemy/Frame 23.png'), pygame.image.load('images/enemy/Frame 24.png'),
         pygame.image.load('images/enemy/Frame 25.png'), pygame.image.load('images/enemy/Frame 26.png'),
         pygame.image.load('images/enemy/Frame 27.png'), pygame.image.load('images/enemy/Frame 28.png'),
         pygame.image.load('images/enemy/Frame 29.png'), pygame.image.load('images/enemy/Frame 30.png'),
         pygame.image.load('images/enemy/Frame 31.png'), pygame.image.load('images/enemy/Frame 32.png'),
         pygame.image.load('images/enemy/Frame 33.png'), pygame.image.load('images/enemy/Frame 34.png'),
         pygame.image.load('images/enemy/Frame 35.png'), pygame.image.load('images/enemy/Frame 36.png'),
         pygame.image.load('images/enemy/Frame 37.png'), pygame.image.load('images/enemy/Frame 38.png'),
         pygame.image.load('images/enemy/Frame 39.png'), pygame.image.load('images/enemy/Frame 40.png'),
         pygame.image.load('images/enemy/Frame 41.png'), pygame.image.load('images/enemy/Frame 42.png'),
         pygame.image.load('images/enemy/Frame 43.png'), pygame.image.load('images/enemy/Frame 44.png'),
         pygame.image.load('images/enemy/Frame 45.png'), pygame.image.load('images/enemy/Frame 46.png'),
         pygame.image.load('images/enemy/Frame 47.png'), pygame.image.load('images/enemy/Frame 48.png'),
         pygame.image.load('images/enemy/Frame 49.png'), pygame.image.load('images/enemy/Frame 50.png'),
         pygame.image.load('images/enemy/Frame 51.png'), pygame.image.load('images/enemy/Frame 52.png'),
         pygame.image.load('images/enemy/Frame 53.png'), pygame.image.load('images/enemy/Frame 54.png'),
         pygame.image.load('images/enemy/Frame 55.png'), pygame.image.load('images/enemy/Frame 56.png'),
         pygame.image.load('images/enemy/Frame 57.png'), pygame.image.load('images/enemy/Frame 58.png'),
         pygame.image.load('images/enemy/Frame 59.png'), pygame.image.load('images/enemy/Frame 60.png'),
         pygame.image.load('images/enemy/Frame 61.png'), pygame.image.load('images/enemy/Frame 62.png'),
         pygame.image.load('images/enemy/Frame 63.png'), pygame.image.load('images/enemy/Frame 64.png'),
         pygame.image.load('images/enemy/Frame 65.png'), pygame.image.load('images/enemy/Frame 66.png'),
         pygame.image.load('images/enemy/Frame 67.png'), pygame.image.load('images/enemy/Frame 68.png'),
         pygame.image.load('images/enemy/Frame 69.png'), pygame.image.load('images/enemy/Frame 70.png'),
         pygame.image.load('images/enemy/Frame 71.png'), pygame.image.load('images/enemy/Frame 72.png'),
         pygame.image.load('images/enemy/Frame 73.png'), pygame.image.load('images/enemy/Frame 74.png'),
         pygame.image.load('images/enemy/Frame 75.png'), pygame.image.load('images/enemy/Frame 76.png'),
         pygame.image.load('images/enemy/Frame 77.png'), pygame.image.load('images/enemy/Frame 78.png'),
         pygame.image.load('images/enemy/Frame 79.png'), pygame.image.load('images/enemy/Frame 80.png'),
         pygame.image.load('images/enemy/Frame 81.png'), pygame.image.load('images/enemy/Frame 82.png'),
         pygame.image.load('images/enemy/Frame 83.png'), pygame.image.load('images/enemy/Frame 84.png'),
         pygame.image.load('images/enemy/Frame 85.png'), pygame.image.load('images/enemy/Frame 86.png'),
         pygame.image.load('images/enemy/Frame 87.png'), pygame.image.load('images/enemy/Frame 88.png'),
         pygame.image.load('images/enemy/Frame 89.png'), pygame.image.load('images/enemy/Frame 90.png'),
         pygame.image.load('images/enemy/Frame 91.png'), pygame.image.load('images/enemy/Frame 92.png'),
         pygame.image.load('images/enemy/Frame 93.png'), pygame.image.load('images/enemy/Frame 94.png'),
         pygame.image.load('images/enemy/Frame 95.png'), pygame.image.load('images/enemy/Frame 96.png'),
         pygame.image.load('images/enemy/Frame 97.png'), pygame.image.load('images/enemy/Frame 98.png'),
         pygame.image.load('images/enemy/Frame 99.png'), pygame.image.load('images/enemy/Frame 100.png'),
         pygame.image.load('images/enemy/Frame 101.png'), pygame.image.load('images/enemy/Frame 102.png'),
         pygame.image.load('images/enemy/Frame 103.png'), pygame.image.load('images/enemy/Frame 104.png'),
         pygame.image.load('images/enemy/Frame 105.png'), pygame.image.load('images/enemy/Frame 106.png'),
         pygame.image.load('images/enemy/Frame 107.png'), pygame.image.load('images/enemy/Frame 108.png'),
         pygame.image.load('images/enemy/Frame 109.png'), pygame.image.load('images/enemy/Frame 110.png'),
         pygame.image.load('images/enemy/Frame 111.png'), pygame.image.load('images/enemy/Frame 112.png'),
         pygame.image.load('images/enemy/Frame 113.png'), pygame.image.load('images/enemy/Frame 114.png'),
         pygame.image.load('images/enemy/Frame 115.png'), pygame.image.load('images/enemy/Frame 116.png'),
         pygame.image.load('images/enemy/Frame 117.png'), pygame.image.load('images/enemy/Frame 118.png'),
         pygame.image.load('images/enemy/Frame 119.png'), pygame.image.load('images/enemy/Frame 120.png')]
score: int = 0
fps = 60
timer = 0
burgers_missed = 0
fpsc = 60
frm_time = 0.0
shots_fired_total = 0
shots_hit = 0
is_a_crashed: bool = False
fpsavg = 0
shots_missed = 0
cooldown: float = float(0)
bullets: List[Any] = []
enemy_list: List[Any] = []
splat_list: List[Any] = []
percentage_hit = 0.0
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
purple: Tuple[int, int, int] = (255, 0, 255)
epic_colour = (40, 52, 72)

konami: List[bool] = [False, False, False, False, False, False, False, False, False, False]


class player(object):
    death: bool

    def __init__(self, x: object, y: object, width: object, height: object) -> object:
        """

        :rtype: object
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
        self.death = False
        self.invulnerable = False
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win: object) -> object:
        win.blit(player_img, (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(projectile_img, (self.x, self.y))


class yes(object):
    def __init__(self, x: object, y: object, width: object, height: object) -> object:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2
        self.timer = 0
        assert isinstance(self.height, object)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(enemy[self.timer], (self.x, self.y))


class splat(object):
    def __init__(self, x: object, y: object, width: object, height: object) -> object:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lifespan = 30

    def draw(self, win):
        win.blit(splatter, (self.x, self.y))
        font = pygame.font.Font("fonts/BurbankBigCondensed-Black.otf", 20)
        text = font.render("100", True, purple)
        win.blit(text, (self.x + self.width // 4, self.y + 64 + 5))


pizza: player = player(640 - 32, 720, 64, 64)
death_enemy = splat(100,100,64,64)


def start() -> object:
    pygame.display.set_icon(icon)
    music = pygame.mixer.music.load('music/ambiance.ogg')
    pygame.mixer.music.play(-1)
    global konami
    win.blit(bg, (0, 0))
    pygame.display.flip()
    while True:
        font = pygame.font.Font("fonts/BurbankBigCondensed-Black.otf", 40)
        text = font.render("Enter code to begin.", True, epic_colour)
        win.blit(text, (10, 670))
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
        assert isinstance(konami, object)
        if keys[pygame.K_RETURN] and all(konami):
            win.blit(bg1, (0, 0))
            pygame.mixer.music.stop()
            music = pygame.mixer.music.load('music/tunes2.ogg')
            pygame.mixer.music.play(-1)
            spawnsnd.play()
            game()
        clock.tick(fps)
        pygame.display.flip()


def game():
    global timer, fpsavg, fpsc, frm_time, exit_state, cooldown, bullets, score, enemy_list, splat_list, shots_fired_total, shots_hit, shots_missed, burgers_missed, percentage_hit
    oh_my_eggs = time.time()
    timer_of_invulnerability: float = time.time()
    while pizza.y > 600:
        pizza.y -= 0.98960910440376
        clock.tick(fps)
        redrawgamewindow()
        fpsavg = clock.get_fps()
        fpsc = (fpsavg // 1)
        frm_time = clock.get_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pizza.y = 600
    while not is_a_crashed:
        mouse: None = pygame.mouse.get_pos()
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
        if keys[pygame.K_EQUALS] or keys[pygame.K_p]:
            pause()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if pizza.x > pizza.vel and not pizza.death:
                pizza.x -= pizza.vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if pizza.x < 1280 - pizza.width - pizza.vel and not pizza.death:
                pizza.x += pizza.vel
        for bullet in bullets:
            if bullet.y > -74:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
                shots_missed += 1
        if len(bullets) < 50 and time.time() - cooldown > float(0.522):
            if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
                if not pizza.death:
                    shots_fired_total += 1
                    cooldown = time.time()
                    bullets.append(
                        projectile(pizza.x + 13, pizza.y, 25, 74))
                    shootsnd.play()
        for foo in enemy_list:
            if foo.y < 720:
                foo.y += foo.vel
                foo.timer += 1
                if 120 <= foo.timer:
                    foo.timer: int = 0
            else:
                assert isinstance(enemy_list.pop, object)
                assert isinstance(enemy_list, object)
                # noinspection PyCallingNonCallable
                enemy_list.pop(enemy_list.index(foo))
                burgers_missed += 1
            #if pygame.Rect.colliderect(pizza.hitbox, pygame.Rect(foo.x, foo.y, foo.width, foo.height)):
            assert isinstance(foo.width, object)
            if foo.x < pizza.x < foo.x + foo.width and foo.y < pizza.y < foo.y + foo.width or foo.x < pizza.x + pizza.width < foo.x + foo.width and foo.y < pizza.y + pizza.height < foo.y + foo.width:
                if not pizza.invulnerable:
                    pizza.invulnerable = True
                    print('hit')
                    pizza.death = True
                    pizza.x = 640 - 32
                    pizza.y = 720 + 98.960910440376
                    deathsnd.play()
        for foo in enemy_list:
            for bullet in bullets:
                if foo.x < bullet.x < foo.x + foo.width and foo.y < bullet.y < foo.y + foo.width or foo.x < bullet.x + bullet.width < foo.x + foo.width and foo.y < bullet.y + bullet.height < foo.y + foo.width:
                    enemy_list.pop(enemy_list.index(foo))
                    bullets.pop(bullets.index(bullet))
                    score += 100
                    shots_hit += 1
                    splat_list.append(
                        splat(foo.x, foo.y, 64, 64))
                    hitsnd.play()
        for foo in splat_list:
            foo.lifespan -= 1
            if foo.lifespan <= 0:
                splat_list.pop(splat_list.index(foo))
        if not time.time() - oh_my_eggs < float(random.uniform(1.55, 3.55)):
            oh_my_eggs = time.time()
            enemy_list.append(
                yes(random.randint(62, 1168), random.randint(-150, -62), 62, 62))
        if timer == 60:
            timer = 0
        if pizza.death:
            if pizza.y > 600:
                pizza.y -= 0.98960910440376
            else:
                pizza.death = False
                pizza.y = 600
                pizza.invulnerable = True
                timer_of_invulnerability = time.time()
            if int(pizza.y) == 720:
                pizza.invulnerable = True
                deathsnd.stop()
                spawnsnd.play()
        if time.time() - timer_of_invulnerability >= float(4) and pizza.invulnerable and pizza.y <= 600:
            pizza.invulnerable = False
        fpsc = (fpsavg // 1)
        frm_time = clock.get_time()
        clock.tick(fps)
        redrawgamewindow()


def redrawgamewindow() -> object:
    global percentage_hit
    updaterect = pygame.Rect(pizza.x - 32, pizza.y - 32, 96, 96)
    win.blit(bg1, (0, 0))
    for bullet in bullets:
        bullet.draw(win)
    for foo in enemy_list:
        foo.draw(win)
    for foo in splat_list:
        foo.draw(win)
    if pizza.y > 600:
        pizza.invulnerable = True
    pizza.draw(win)
    # font = pygame.font.Font("fonts/Ailerons-Typeface.otf", 20)
    font = pygame.font.Font("fonts/BurbankBigCondensed-Black.otf", 20)
    text = font.render("FPS: " + str(fpsc), True, white)
    win.blit(text, (5, 5))
    text = font.render("Frame time: " + str(frm_time) + 'ms', True, white)
    win.blit(text, (5, 25))
    text = font.render("Projectiles on screen: " + str(len(bullets)), True, white)
    win.blit(text, (5, 45))
    text = font.render("Enemies on screen: " + str(len(enemy_list)), True, white)
    win.blit(text, (5, 65))
    text = font.render("Splats on screen: " + str(len(splat_list)), True, white)
    win.blit(text, (5, 85))
    text = font.render("Pizza X: " + str(pizza.x) + ' Pizza Y: ' + str(pizza.y), True, white)
    win.blit(text, (5, 105))
    text = font.render("Pizza.isInvulnerable: {0}".format(str(pizza.invulnerable)), True, white)
    win.blit(text, (5, 125))
    text = font.render('Display Driver: ' + str(pygame.display.get_driver()), True, white)
    win.blit(text, (5, 145))
    text = font.render('time.time(): ' + str(time.time()), True, white)
    win.blit(text, (5, 165))
    try:
        text = font.render('Accuracy calculator:  ' + 'Shots Fired: ' + str(shots_fired_total) + ' Shots Hit: ' + str(shots_hit) + ' Shots Missed: ' + str(shots_missed) + ' Burgers missed: ' + str(burgers_missed) + ' Accuracy Percentage: ' + str((shots_hit/shots_fired_total * 100)//1) + '%', True, white)
        win.blit(text, (5, 185))
        percentage_hit = (shots_hit / shots_fired_total * 100) // 1
    except:
        text = font.render('Accuracy calculator:  ' + 'Shots Fired: ' + str(shots_fired_total) + ' Shots Hit: ' + str(shots_hit) + ' Shots Missed: ' + str(shots_missed) + ' Burgers missed: ' + str(burgers_missed) + ' Accuracy Percentage: 0%', True, white)
        win.blit(text, (5, 185))
    smallText: Union[Font, FontType] = pygame.font.Font("fonts/BurbankBigCondensed-Black.otf", 40)
    textSurf, textRect = text_objects('High Score', smallText, red)
    textRect.center = (1280 // 2, 35)
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(str(score), smallText, white)
    textRect.center = (1280 // 2, 80)
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects('Accuracy', smallText, blue)
    textRect.center = (1280 // 2 - 300, 35)
    win.blit(textSurf, textRect)
    textSurf, textRect = text_objects(str(percentage_hit) + '%', smallText, white)
    textRect.center = (1280 // 2 - 300, 80)
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
    while not False:
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
