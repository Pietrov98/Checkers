import pygame
from pygame.locals import *
from board import *
import time
import os
first_run_bool = True

class Menu():
    def __init__(self):
        self.screen = pygame.display.set_mode((900, 800))
        pygame.mixer.pre_init(22050, -16, 2, 256)
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.quit()
        pygame.mixer.init(22050, -16, 2, 256)
        self.clock = pygame.time.Clock()
        self.background_menuImg = pygame.image.load('menu.png')
        self.new_game_buttonImg = pygame.image.load('play.png')
        self.end_game_buttonImg = pygame.image.load('end.png')
        self.menu_sound = pygame.mixer.Sound('theme_song.wav')
        pygame.display.set_caption('Checkers')
        self.run_game = True
    def end_button(self, coord):
        if coord[0] >= 350 and coord[0] <= 535 and coord[1] >= 550 and coord[1] <= 615:
            self.run_game = False
    def new_game_button(self, coord):
        if coord[0] >= 350 and coord[0] <= 535 and coord[1] >= 425 and coord[1] <= 485:
            board_run_game(self.screen)
            first_run_bool = True
            self.first_run()
    def first_run(self):
        self.menu_sound.play()
        time.sleep(1)
        self.screen.blit(self.background_menuImg, [0 ,0])
        pygame.display.update()
        time.sleep(1)
        self.screen.blit(self.new_game_buttonImg, [0 ,0])
        pygame.display.update()
        time.sleep(1)
        self.screen.blit(self.end_game_buttonImg, [0 ,0])
        pygame.display.update()

x = 290
y = 24
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
menu = Menu()
while menu.run_game:
    pygame.time.delay(100)
    if first_run_bool == True:
        #menu.menu_sound.play()
        menu.first_run()
        first_run_bool = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu.run_game = False
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print(mouse)
            menu.new_game_button(mouse)
            menu.end_button(mouse)
        menu.screen.blit(menu.background_menuImg, [0 ,0])
        menu.screen.blit(menu.new_game_buttonImg, [0 ,0])
        menu.screen.blit(menu.end_game_buttonImg, [0 ,0])
        pygame.display.flip()
        pygame.display.update()
        menu.clock.tick(60)
pygame.quit()
