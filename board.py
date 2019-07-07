from checkers_rules import *
import time
from pygame.locals import *
import pygame

def board_run_game(screen):
    pygame.mixer.pre_init(22050, -16, 2, 256)
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.quit()
    pygame.mixer.init(22050, -16, 2, 256)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((900, 800))
    background_boardImg = pygame.image.load('Plansza.png')
    fatalityImg = pygame.image.load('fatality.png')
    player1Img = pygame.image.load('playerone.png')
    player2Img = pygame.image.load('playertwo.png')
    fightImg = pygame.image.load('fight.png')
    player_one_crystalImg = pygame.image.load('turn_one.png')
    player_two_crystalImg = pygame.image.load('turn_two.png')
    have_kill_oneImg = pygame.image.load('have_kill1.png')
    have_kill_twoImg = pygame.image.load('have_kill2.png')
    punch_sound = pygame.mixer.Sound('punch.wav')
    fatality_sound = pygame.mixer.Sound('fatality.wav')
    player1_sound = pygame.mixer.Sound('player1win.wav')
    player2_sound = pygame.mixer.Sound('player2win.wav')
    fight_sound = pygame.mixer.Sound('fight.wav')
    finish_him_sound = pygame.mixer.Sound('finish_him.wav')
    pygame.display.set_caption('Checkers')
    kill_ind = ["", "", "", "", "", "", "", "", ""]
    end_butt_bool = True
    screen.blit(fightImg, [100, 0])
    fight_sound.play()
    pygame.display.update()
    time.sleep(1.3)
    while end_butt_bool:
        game = Game()
        Game.player = 1
        Game.index_b, Game.index_w = -1, -1 #index wybranego pionka
        Game.white_kill, Game.black_kill = False, False
        run = True
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    end_butt_bool = False
                    print("proba 1, 2, 3")
                    pygame.quit()
                    break
                if event.type == MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    run = game.reset_button(mouse)
                    end_butt_bool = game.end_button(mouse)
                    if end_butt_bool == False:
                        run = False
                        break
                    game.select_checker(mouse);
                    walls = game.check_walls()
                    if not(walls[1] == "right" and walls[2] == "left") and not(isinstance(game.whites[Game.index_w], Queen)) and Game.player == 1:
                        kill_ind = game.posibility_to_kill(walls)
                    elif not(walls[1] == "right" and walls[2] == "left") and not(isinstance(game.blacks[Game.index_b], Queen)) and Game.player == 2:
                        kill_ind = game.posibility_to_kill(walls)
                    elif isinstance(game.whites[Game.index_w], Queen) and not(walls[1] == "right" and walls[2] == "left" and walls[5] == "right-down" and walls[6] == "left-down") and Game.player == 1:
                        kill_ind = game.posibility_to_kill(walls)
                    elif isinstance(game.blacks[Game.index_b], Queen) and not(walls[1] == "right" and walls[2] == "left" and walls[5] == "right-down" and walls[6] == "left-down") and Game.player == 2:
                        kill_ind = game.posibility_to_kill(walls)
                    game.game_loop(mouse, walls, kill_ind, screen, punch_sound, fatality_sound, fatalityImg, finish_him_sound)
                screen.blit(background_boardImg, [0, 0])
                if Game.player == 1:
                    screen.blit(player_one_crystalImg, [0, 0])
                    if Game.have_to_kill_w == True:
                        screen.blit(have_kill_oneImg, [0, 0])
                elif Game.player == 2:
                    screen.blit(player_two_crystalImg, [0, 0])
                    if Game.have_to_kill_b == True:
                        screen.blit(have_kill_twoImg, [0, 0])
                game.draw(screen)
                pygame.display.flip()
                pygame.display.update()
                clock.tick(60)
                if game.black_alives == 0:
                    print("Wygraly biale")
                    time.sleep(0.5)
                    player1_sound.play()
                    screen.blit(player1Img, (0, 0))
                    pygame.display.update()
                    time.sleep(3)
                    run = False
                    break
                elif game.white_alives == 0:
                    print("Wygraly czarne")
                    time.sleep(0.5)
                    player2_sound.play()
                    screen.blit(player2Img, (0, 0))
                    pygame.display.update()
                    time.sleep(3)
                    run = False
                    break
                
