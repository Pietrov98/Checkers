import pygame
import time
from pygame.locals import *
from checkers_exceptions import *

WHITE    = (127, 114, 114)
RED      = (183, 69, 69)
YELLOW   = (178, 183, 51)
BLACK    = (0, 0, 0)

class Checker:
    def __init__(self):pass
    def make_move(self):pass 
    def kill(self):pass

class Pawn(Checker):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def make_move(self, player, must_kill, coord, field_width, walls):
        pos = lambda x, y: int(x + y) #lambda1
        if player == 1 and (Game.index_w != -1):
            if(must_kill == False) and not(walls[1] == "right" and walls[2] == "left"):
                if coord[1] >= pos(self.y, field_width / 2) and coord[1] <= pos(self.y, 3 * field_width / 2):
                    if coord[0] >= (pos(self.x, field_width / 2)) and coord[0] <= pos(self.x, 3 * field_width / 2): 
                        if walls[1] != "right":
                            self.x = pos(self.x, field_width)
                            self.y = pos(self.y, field_width)
                            self.color = BLACK
                            Game.player = 2
                            return True
                    elif coord[0] >= pos(self.x, -3 * field_width / 2) and coord[0] <= pos(self.x, -field_width / 2):
                        if walls[2] != "left":
                            self.x = pos(self.x, - field_width)
                            self.y = pos(self.y, field_width)
                            self.color = BLACK
                            Game.player = 2
                            return True
        if player == 2 and (Game.index_b != -1):
            if(must_kill == False) and not(walls[1] == "right" and walls[2] == "left"):
                if coord[1] <= pos(self.y, - field_width / 2) and coord[1] >= pos(self.y, -3 * field_width / 2):
                    if coord[0] >= pos(self.x, field_width / 2) and coord[0] <= pos(self.x, 3 * field_width / 2): 
                        if walls[1] != "right":
                            self.x = pos(self.x, field_width)
                            self.y = pos(self.y, -field_width)
                            self.color = BLACK
                            Game.player = 1
                            return True
                    elif coord[0] >= (pos(self.x, -3 * field_width / 2)) and coord[0] <= pos(self.x, -field_width / 2):
                        if walls[2] != "left":
                            self.x = pos(self.x, - field_width)
                            self.y = pos(self.y, - field_width)
                            self.color = BLACK
                            Game.player = 1
                            return True
                            
    def kill(self, player, coord, field_width, kill_ind, j):
        pos = lambda x, y: int(x + y) #lambda2
        if player == 1:
            if kill_ind[1] == "right":
                if coord[1] >= pos(self.y, 3 * field_width / 2) and coord[1] <= pos(self.y, 5 * field_width / 2):
                    if coord[0] >= pos(self.x, 3 * field_width / 2) and coord[0] <= pos(self.x, 5 * field_width / 2): 
                        self.x = pos(self.x, 2 * field_width)
                        self.y = pos(self.y, 2 * field_width)
                        self.color = BLACK
                        Game.index_w = j
                        Game.white_kill = True
                        return kill_ind[3]
            if kill_ind[2] == "left":
                if coord[1] >= pos(self.y, 3 * field_width / 2) and coord[1] <= pos(self.y, 5 * field_width / 2):
                    if coord[0] <= pos(self.x, -3 * field_width / 2) and coord[0] >= pos(self.x, -5 * field_width / 2): 
                        self.x = pos(self.x, -2 * field_width)
                        self.y = pos(self.y, 2 * field_width)
                        self.color = BLACK
                        Game.index_w = j
                        Game.white_kill = True
                        return kill_ind[4]

        if player == 2:
            if kill_ind[1] == "right":
                if coord[1] <= pos(self.y, -3 * field_width / 2) and coord[1] >= pos(self.y, -5 * field_width / 2):
                    if coord[0] >= pos(self.x, 3 * field_width / 2) and coord[0] <= pos(self.x, 5 * field_width / 2):
                        self.x = pos(self.x, 2 * field_width)
                        self.y = pos(self.y, -2 * field_width)
                        self.color = BLACK
                        Game.index_b = j
                        Game.black_kill = True
                        return kill_ind[3]
            if kill_ind[2] == "left":
                if coord[1] <= pos(self.y, -3 * field_width / 2) and coord[1] >= pos(self.y, -5 * field_width / 2):
                    if coord[0] <= pos(self.x, -3 * field_width / 2) and coord[0] >= pos(self.x, -5 * field_width / 2): 
                        self.x = pos(self.x, -2 * field_width)
                        self.y = pos(self.y, -2 * field_width)
                        self.color = BLACK
                        Game.index_b = j
                        Game.black_kill = True
                        return kill_ind[4]
        
    
class Queen(Checker):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def make_move(self, player, must_kill, coord, field_width, walls):
        if player == 1 and (Game.index_w != -1):
            if(must_kill == False) and not(walls[1] == "right" and walls[2] == "left" and walls[5] == "right-down" and walls[6] == "left-down"):
                if coord[1] >= int(self.y + field_width / 2) and coord[1] <= int(self.y + 3 * field_width / 2):
                    if coord[0] >= (int(self.x + field_width / 2)) and coord[0] <= int(self.x + 3 * field_width / 2): 
                        if walls[1] != "right":
                            self.x = int(self.x + field_width)
                            self.y = int(self.y + field_width)
                            self.color = BLACK
                            Game.player = 2
                            return True
                    elif coord[0] >= int(self.x - 3 * field_width / 2) and coord[0] <= int(self.x - field_width / 2):
                        if walls[2] != "left":
                            self.x = int(self.x - field_width)
                            self.y = int(self.y + field_width)
                            self.color = BLACK
                            Game.player = 2
                            return True
                if coord[1] <= int(self.y - field_width / 2) and coord[1] >= int(self.y - 3 * field_width / 2):
                    if coord[0] >= int(self.x + field_width / 2) and coord[0] <= int(self.x + field_width + field_width / 2): 
                        if walls[5] != "right-down":
                            self.x = int(self.x + field_width)
                            self.y = int(self.y - field_width)
                            self.color = BLACK
                            Game.player = 2
                            return True
                    elif coord[0] >= int(self.x - 3 * field_width / 2) and coord[0] <= int(self.x - field_width / 2):
                        if walls[6] != "left-down":
                            self.x = int(self.x - field_width)
                            self.y = int(self.y - field_width)
                            self.color = BLACK
                            Game.player = 2
                            return True
        if player == 2 and (Game.index_b != -1):
            if(must_kill == False) and not(walls[1] == "right" and walls[2] == "left" and walls[5] == "right-down" and walls[6] == "left-down"):
                if coord[1] <= int(self.y - field_width / 2) and coord[1] >= int(self.y - 3 * field_width / 2):
                    if coord[0] >= int(self.x + field_width / 2) and coord[0] <= int(self.x + 3 * field_width / 2): 
                        if walls[1] != "right":
                            self.x = int(self.x + field_width)
                            self.y = int(self.y - field_width)
                            self.color = BLACK
                            Game.player = 1
                            return True
                    elif coord[0] >= int(self.x - 3 * field_width / 2) and coord[0] <= int(self.x - field_width / 2):
                        if walls[2] != "left":
                            self.x = int(self.x - field_width)
                            self.y = int(self.y - field_width)
                            self.color = BLACK
                            Game.player = 1
                            return True
                if coord[1] >= int(self.y + field_width / 2) and coord[1] <= int(self.y + 3 * field_width / 2):
                    if coord[0] >= (int(self.x + field_width / 2)) and coord[0] <= int(self.x + 3 * field_width / 2): 
                        if walls[5] != "right-down":
                            self.x = int(self.x + field_width)
                            self.y = int(self.y + field_width)
                            self.color = BLACK
                            Game.player = 1
                            return True
                    elif coord[0] >= int(self.x - 3 * field_width / 2) and coord[0] <= int(self.x - field_width / 2):
                        if walls[6] != "left-down":
                            self.x = int(self.x - field_width)
                            self.y = int(self.y + field_width)
                            self.color = BLACK
                            Game.player = 1
                            return True
    def kill(self, player, coord, field_width, kill_ind, j):
        if player == 1:
            if kill_ind[1] == "right":
                if coord[1] >= int(self.y + 3 * field_width / 2) and coord[1] <= int(self.y + 5 * field_width / 2):
                    if coord[0] >= int(self.x + 3 * field_width / 2) and coord[0] <= int(self.x + 5 * field_width / 2): 
                        self.x = int(self.x + 2 * field_width)
                        self.y = int(self.y + 2 * field_width)
                        self.color = BLACK
                        Game.index_w = j
                        Game.white_kill = True
                        return kill_ind[3]
            if kill_ind[2] == "left":
                if coord[1] >= int(self.y + 3 * field_width / 2) and coord[1] <= int(self.y + 5 * field_width / 2):
                    if coord[0] <= int(self.x - 3 * field_width / 2) and coord[0] >= int(self.x - 5 *field_width / 2): 
                        self.x = int(self.x - 2 * field_width)
                        self.y = int(self.y + 2 * field_width)
                        self.color = BLACK
                        Game.index_w = j
                        Game.white_kill = True
                        return kill_ind[4]
            if kill_ind[5] == "right-down":
                if coord[1] <= int(self.y - 3 * field_width / 2) and coord[1] >= int(self.y - 5 * field_width / 2):
                    if coord[0] >= int(self.x + 3 * field_width / 2) and coord[0] <= int(self.x + 5 * field_width / 2):
                        self.x = int(self.x + 2 * field_width)
                        self.y = int(self.y - 2 * field_width)
                        self.color = BLACK
                        Game.index_w = j
                        Game.white_kill = True
                        return kill_ind[7]
            if kill_ind[6] == "left-down":
                if coord[1] <= int(self.y - 3 * field_width / 2) and coord[1] >= int(self.y - 5 * field_width / 2):
                    if coord[0] <= int(self.x - 3 * field_width / 2) and coord[0] >= int(self.x - 5 * field_width / 2): 
                        self.x = int(self.x - 2 * field_width)
                        self.y = int(self.y - 2 * field_width)
                        self.color = BLACK
                        Game.index_w = j
                        Game.white_kill = True
                        return kill_ind[8]
        if player == 2:
            if kill_ind[1] == "right":
                if coord[1] <= int(self.y - 3 * field_width / 2) and coord[1] >= int(self.y - 5 * field_width / 2):
                    if coord[0] >= int(self.x + 3 * field_width / 2) and coord[0] <= int(self.x + 5 * field_width / 2):
                        self.x = int(self.x + 2 * field_width)
                        self.y = int(self.y - 2 * field_width)
                        self.color = BLACK
                        Game.index_b = j
                        Game.black_kill = True
                        return kill_ind[3]
            if kill_ind[2] == "left":
                if coord[1] <= int(self.y - 3 * field_width / 2) and coord[1] >= int(self.y - 5 * field_width / 2):
                    if coord[0] <= int(self.x - 3 * field_width / 2) and coord[0] >= int(self.x - 5 * field_width / 2): 
                        self.x = int(self.x - 2 * field_width)
                        self.y = int(self.y - 2 * field_width)
                        self.color = BLACK
                        Game.index_b = j
                        Game.black_kill = True
                        return kill_ind[4]
            if kill_ind[5] == "right-down":
                if coord[1] >= int(self.y + 3 * field_width / 2) and coord[1] <= int(self.y + 5 * field_width / 2):
                    if coord[0] >= int(self.x + 3 * field_width / 2) and coord[0] <= int(self.x + 5 * field_width / 2): 
                        self.x = int(self.x + 2 * field_width)
                        self.y = int(self.y + 2 * field_width)
                        self.color = BLACK
                        Game.index_b = j
                        Game.black_kill = True
                        return kill_ind[7]
            if kill_ind[6] == "left-down":
                if coord[1] >= int(self.y + 3 *  field_width / 2) and coord[1] <= int(self.y + 5 * field_width / 2):
                    if coord[0] <= int(self.x - 3 * field_width / 2) and coord[0] >= int(self.x - 5 *field_width / 2): 
                        self.x = int(self.x - 2 * field_width)
                        self.y = int(self.y + 2 * field_width)
                        self.color = BLACK
                        Game.index_b = j
                        Game.black_kill = True
                        return kill_ind[8]
            

class Game:
    player = 1
    index_b, index_w = -1, -1 #index wybranego pionka
    white_kill, black_kill = False, False
    have_to_kill_w, have_to_kill_b = False, False
    def __init__(self):
        self.black_alives, self.white_alives = 8, 8 #pozostale na planszy
        self.blacks, self.whites = [], [] #listy pionkow
        self.width = 800 #wielkosc planszy
        self.field_width = self.width / 8 #wielkosc pola
        self.selected_w, self.selected_b = 1, 1 #aktualnie wybrany pionek (obiekt)
        self.prev_selected_w, self.prev_selected_b = 1, 1 #poprzednio wybrany pionek (obiekt)
        self.white_must_kill, self.black_must_kill = False, False #informacja, że musi nastąpić bicie przeciwnika
        self.white_must_kill_second, self.black_must_kill_second = False, False
        self.kill_counter_w, self.kill_counter_b = 0, 0 #index tego ktory zabil
        self.white_pawnImg = pygame.image.load('white_pawn.png')
        self.black_pawnImg = pygame.image.load('black_pawn.png')
        self.crownImg = pygame.image.load('crown.png')

        lista1 = [Pawn(int((j + 0.5) * self.field_width), int(self.field_width / 2), BLACK) for j in range(0, 8, 2)]
        lista2 = [Pawn(int((j + 0.5) * self.field_width), int(self.field_width + self.field_width / 2), BLACK) for j in range(1, 8, 2)]
        self.whites = lista1 + lista2

        lista1 = [Pawn(int((j + 0.5) * self.field_width), int(13 * self.field_width / 2), BLACK) for j in range(0, 8, 2)]
        lista2 = [Pawn(int((j + 0.5) * self.field_width), int(15 *  self.field_width / 2), BLACK) for j in range(1, 8, 2)]
        self.blacks = lista1 + lista2
        
    def draw(self, screen):
        for i in range(8):
            #screen.blit(self.black_pawnImg, (self.whites[i].x, self.whites[i].y))
            screen.blit(self.white_pawnImg, (self.whites[i].x - 40, self.whites[i].y - 40))
            pygame.draw.circle(screen, self.whites[i].color, (self.whites[i].x, self.whites[i].y), 40, 3)
            if isinstance(self.whites[i], Queen):
                screen.blit(self.crownImg, (self.whites[i].x - 50, self.whites[i].y - 53))
            screen.blit(self.black_pawnImg, (self.blacks[i].x - 40, self.blacks[i].y - 40))
            pygame.draw.circle(screen, self.blacks[i].color, (self.blacks[i].x, self.blacks[i].y), 40, 3)
            if isinstance(self.blacks[i], Queen):
                screen.blit(self.crownImg, (self.blacks[i].x - 50, self.blacks[i].y - 53))
            
    def select_checker(self, coord):
        pos = lambda x, y: int(x + y)
        if self.player == 1:
            for i in range(8):
                if coord[0] >= pos(self.whites[i].x, -self.field_width / 2) and coord[0] <= pos(self.whites[i].x, self.field_width / 2):
                    if  coord[1] >= pos(self.whites[i].y, -self.field_width / 2) and coord[1] <= pos(self.whites[i].y, self.field_width / 2):
                        if self.selected_w > 1:
                            self.prev_selected_w.color = BLACK
                            self.selected_w -= 1
                        self.whites[i].color = YELLOW
                        self.prev_selected_w = self.whites[i]
                        self.selected_w += 1
                        Game.index_w = i
                        break
        elif self.player == 2:
            for i in range(8):
                if coord[0] >= pos(self.blacks[i].x, -self.field_width / 2) and coord[0] <= pos(self.blacks[i].x, self.field_width / 2):
                    if  coord[1] >= pos(self.blacks[i].y, -self.field_width / 2) and coord[1] <= pos(self.blacks[i].y,  self.field_width / 2):
                        if self.selected_b > 1:
                            self.prev_selected_b.color = BLACK
                            self.selected_b -= 1
                        self.blacks[i].color = YELLOW
                        self.prev_selected_b = self.blacks[i]
                        self.selected_b += 1
                        Game.index_b = i
                        break

    def posibility_to_kill(self, walls):
         #kill_ind [j, prawo, lewo, i-prawo, i-lewo] j-aktualnego, iobok prawo, i obok lewo
        if Game.player == 1:
           
            j = Game.index_w #wybrany bialy pionek1
            result = [j, "", "", "", "", "", "", "", ""]
            if walls[1] != "right":
                for i in range(0, 8):
                    if self.blacks[i].x == (self.whites[j].x + self.field_width) and self.blacks[i].y == (self.whites[j].y + self.field_width):
                        self.white_must_kill = True
                        result[1] = "right"
                        result[3] = i
                        break
            if walls[2] != "left":
                for i in range(0, 8):
                    if self.blacks[i].x == (self.whites[j].x - self.field_width) and self.blacks[i].y == (self.whites[j].y + self.field_width):
                        self.white_must_kill = True
                        result[2] = "left"
                        result[4] = i
                        break
            if isinstance(self.whites[j], Queen):
                if walls[5] != "right-down":
                    for i in range(0, 8):
                        if self.blacks[i].x == (self.whites[j].x + self.field_width) and self.blacks[i].y == (self.whites[j].y - self.field_width):
                            self.black_must_kill = True
                            result[5] = "right-down"
                            result[7] = i
                            break
                if walls[6] != "left-down":
                    for i in range(0, 8):
                        if self.blacks[i].x == (self.whites[j].x - self.field_width) and self.blacks[i].y == (self.whites[j].y - self.field_width):
                            self.black_must_kill = True
                            result[6] = "left-down"
                            result[8] = i
                            break
            return result
        elif Game.player == 2:
            j = Game.index_b
            result = [j, "", "", "", "", "", "", "", ""]
            if walls[1] != "right":
                for i in range(0, 8):
                    if self.whites[i].x == (self.blacks[j].x + self.field_width) and self.whites[i].y == (self.blacks[j].y - self.field_width):
                        self.black_must_kill = True
                        result[1] = "right"
                        result[3] = i
                        break
            if walls[2] != "left":
                for i in range(0, 8):
                    if self.whites[i].x == (self.blacks[j].x - self.field_width) and self.whites[i].y == (self.blacks[j].y - self.field_width):
                        self.black_must_kill = True
                        result[2] = "left"
                        result[4] = i
                        break
            if isinstance(self.blacks[j], Queen):
                if walls[5] != "right-down":
                    for i in range(0, 8):
                        if self.whites[i].x == (self.blacks[j].x + self.field_width) and self.whites[i].y == (self.blacks[j].y + self.field_width):
                            self.black_must_kill = True
                            result[5] = "right-down"
                            result[7] = i
                            break
                if walls[6] != "left-down":
                    for i in range(0, 8):
                        if self.whites[i].x == (self.blacks[j].x - self.field_width) and self.whites[i].y == (self.blacks[j].y + self.field_width):
                            self.black_must_kill = True
                            result[6] = "left-down"
                            result[8] = i
                            break
            return result
       
    def someone_can_kill(self):
        if Game.player == 1:
            j = Game.index_w
            for i in range(0, 8):
                if self.whites[i].x != -100 and self.whites[i].y != -100:
                    Game.index_w = i
                    if isinstance(self.whites[i], Queen):
                        walls = self.check_walls()
                        if not(walls[1] == "right" and walls[2] == "left" and walls[5] == "right-down" and walls[6] == "left-down"):
                            kill_ind = self.posibility_to_kill(walls)
                            if kill_ind[1] == "right" or kill_ind[2] == "left" or kill_ind[5] == "right-down" or kill_ind[6] == "left-down":
                                Game.index_w = j
                                return True
                    else:
                        walls = self.check_walls()
                        if not(walls[1] == "right" and walls[2] == "left"):
                            kill_ind = self.posibility_to_kill(walls)
                            if kill_ind[1] == "right" or kill_ind[2] == "left":
                                Game.index_w = j
                                return True
            Game.index_w = j
            return False
        if Game.player == 2:
            j = Game.index_b
            for i in range(0, 8):
                if self.blacks[i].x != -100 and self.blacks[i].y != -100:
                    Game.index_b = i
                    if isinstance(self.blacks[i], Queen):
                        walls = self.check_walls()
                        if not(walls[1] == "right" and walls[2] == "left" and walls[5] == "right-down" and walls[6] == "left-down"):
                            kill_ind = self.posibility_to_kill(walls)
                            if kill_ind[1] == "right" or kill_ind[2] == "left" or kill_ind[5] == "right-down" or kill_ind[6] == "left-down":
                                Game.index_b = j
                                return True
                    else:
                        walls = self.check_walls()
                        if not(walls[1] == "right" and walls[2] == "left"):
                            kill_ind = self.posibility_to_kill(walls)
                            if kill_ind[1] == "right" or kill_ind[2] == "left":
                                Game.index_b = j
                                return True
            Game.index_b = j
            return False
        
    def check_walls(self):
        #walls [j, prawo, lewo, i-prawo, i-lewo] j-aktualnego, iobok prawo, i obok lewo, prawo-dol, lewo-dol, i-dol-prawo, i-dol-lewo
        if Game.player == 1:
            j = Game.index_w
            result = [j, "", "", "", "", "", "", "", ""]
            for i in range(0, 8):
                if self.blacks[i].x == (self.whites[j].x + self.field_width) and self.blacks[i].y == (self.whites[j].y + self.field_width):
                    if (self.whites[j].x + 2 * self.field_width) >= self.width or (self.whites[j].y + 2 * self.field_width) >= self.width:
                        result = [j, "right", "", i, "", "", "", "", ""]
                        break
                    for k in range(0, 8):
                        if self.blacks[k].x == (self.whites[j].x + 2 * self.field_width) and self.blacks[k].y == (self.whites[j].y + 2 * self.field_width):
                            result = [j, "right", "", i, "", "", "", "", ""]
                            break
                        elif self.whites[k].x == (self.whites[j].x + 2 * self.field_width) and self.whites[k].y == (self.whites[j].y + 2 * self.field_width):
                            result = [j, "right", "", i, "", "", "", "", ""]
                            break
            for i in range(0, 8):
                if self.blacks[i].x == (self.whites[j].x - self.field_width) and self.blacks[i].y == (self.whites[j].y + self.field_width):
                    if (self.whites[j].x - 2 * self.field_width) <= 0 or (self.whites[j].y + 2 * self.field_width) >= self.width:
                        result[2] = "left"
                        result[4] = i
                        break
                    for k in range(0, 8):
                        if self.blacks[k].x == (self.whites[j].x - 2 * self.field_width) and self.blacks[k].y == (self.whites[j].y + 2 * self.field_width):
                            result[2] = "left"
                            result[4] = i
                            break
                        elif self.whites[k].x == (self.whites[j].x - 2 * self.field_width) and self.whites[k].y == (self.whites[j].y + 2 * self.field_width):
                            result[2] = "left"
                            result[4] = i
                            break
            if (self.whites[j].x + self.field_width) >= self.width:
                result[1] = "right"
                result[3] = i
                result[5] = "right-down"
                result[7] = i
            if (self.whites[j].x - self.field_width) <= 0:
                result[2] = "left"
                result[4] = i
                result[6] = "left-down"
                result[8] = i
            if (self.whites[j].y + self.field_width) >= self.width:
                result[1] = "right"
                result[2] = "left"
                result[3] = i
            if isinstance(self.whites[j], Queen):
                for i in range(0, 8):
                    if self.blacks[i].x == (self.whites[j].x + self.field_width) and self.blacks[i].y == (self.whites[j].y - self.field_width):
                        if (self.whites[j].x + 2 * self.field_width) >= self.width or (self.whites[j].y - 2 * self.field_width) <= 0:
                            result[5] = "right-down"
                            result[7] = i
                            break
                        for k in range(0, 8):
                            if self.blacks[k].x == (self.whites[j].x + 2 * self.field_width) and self.blacks[k].y == (self.whites[j].y - 2 * self.field_width):
                                result[5] = "right-down"
                                result[7] = i
                                break
                            elif self.whites[k].x == (self.whites[j].x + 2 * self.field_width) and self.whites[k].y == (self.whites[j].y - 2 * self.field_width):
                                result[5] = "right-down"
                                result[7] = i
                                break
                for i in range(0, 8):
                    if self.blacks[i].x == (self.whites[j].x - self.field_width) and self.blacks[i].y == (self.whites[j].y - self.field_width):
                        if (self.whites[j].x - 2 * self.field_width) <= 0 or (self.whites[j].y - 2 * self.field_width) <= 0:
                            result[6] = "left-down"
                            result[8] = i
                            break
                        for k in range(0, 8):
                            if self.blacks[k].x == (self.whites[j].x - 2 * self.field_width) and self.blacks[k].y == (self.whites[j].y - 2 * self.field_width):
                                result[6] = "left-down"
                                result[8] = i
                                break
                            elif self.whites[k].x == (self.whites[j].x - 2 * self.field_width) and self.whites[k].y == (self.whites[j].y - 2 * self.field_width):
                                result[6] = "left-down"
                                result[8] = i
                                break
                if (self.whites[j].y - self.field_width) <= 0:
                    result[5] = "right-down"
                    result[6] = "left-down"
                    result[7] = i
            return result
        elif Game.player == 2:
            j = Game.index_b
            result = [j, "", "", "", "", "", "", "", ""]
            for i in range(0, 8):
                if self.whites[i].x == (self.blacks[j].x + self.field_width) and self.whites[i].y == (self.blacks[j].y - self.field_width):
                    if (self.blacks[j].x + 2 * self.field_width) >= self.width or (self.blacks[j].y - 2 * self.field_width) <= 0:
                        result = [j, "right", "", i, "", "", "", "", ""]
                        break
                    for k in range(0, 8):
                        if self.whites[k].x == (self.blacks[j].x + 2 * self.field_width) and self.whites[k].y == (self.blacks[j].y - 2 * self.field_width):
                            result = [j, "right", "", i, "", "", "", "", ""]
                            break
                        elif self.blacks[k].x == (self.blacks[j].x + 2 * self.field_width) and self.blacks[k].y == (self.blacks[j].y - 2 * self.field_width):
                            result = [j, "right", "", i, "", "", "", "", ""]
                            break
            for i in range(0, 8):
                if self.whites[i].x == (self.blacks[j].x - self.field_width) and self.whites[i].y == (self.blacks[j].y - self.field_width):
                    if (self.blacks[j].x - 2 * self.field_width) <= 0 or (self.blacks[j].y - 2 * self.field_width) <= 0:
                        result[2] = "left"
                        result[4] = i
                        break
                    for k in range(0, 8):
                        if self.whites[k].x == (self.blacks[j].x - 2 * self.field_width) and self.whites[k].y == (self.blacks[j].y - 2 * self.field_width):
                            result[2] = "left"
                            result[4] = i
                            break
                        elif self.blacks[k].x == (self.blacks[j].x - 2 * self.field_width) and self.blacks[k].y == (self.blacks[j].y - 2 * self.field_width):
                            result[2] = "left"
                            result[4] = i
                            break
            if (self.blacks[j].x + self.field_width) >= self.width:
                result[1] = "right"
                result[3] = i
                result[5] = "right-down"
                result[7] = i
            if (self.blacks[j].x - self.field_width) <= 0:
                result[2] = "left"
                result[4] = i
                result[6] = "left-down"
                result[8] = i
            if (self.blacks[j].y - self.field_width) <= 0:
                result[1] = "right"
                result[2] = "left"
                result[3] = "i"
            if isinstance(self.blacks[j], Queen):
                for i in range(0, 8):
                    if self.whites[i].x == (self.blacks[j].x + self.field_width) and self.whites[i].y == (self.blacks[j].y + self.field_width):
                        if (self.blacks[j].x + 2 * self.field_width) >= self.width or (self.blacks[j].y + 2 * self.field_width) >= self.width:
                            result[5] = "right-down"
                            result[7] = i
                            break
                        for k in range(0, 8):
                            if self.whites[k].x == (self.blacks[j].x + 2 * self.field_width) and self.whites[k].y == (self.blacks[j].y + 2 * self.field_width):
                                result[5] = "right-down"
                                result[7] = i
                                break
                            elif self.blacks[k].x == (self.blacks[j].x + 2 * self.field_width) and self.blacks[k].y == (self.blacks[j].y + 2 * self.field_width):
                                result[5] = "right-down"
                                result[7] = i
                                break
                for i in range(0, 8):
                    if self.whites[i].x == (self.blacks[j].x - self.field_width) and self.whites[i].y == (self.blacks[j].y + self.field_width):
                        if (self.blacks[j].x - 2 * self.field_width) <= 0 or (self.blacks[j].y + 2 * self.field_width) >= self.width:
                            result[6] = "left-down"
                            result[8] = i
                            break
                        for k in range(0, 8):
                            if self.whites[k].x == (self.blacks[j].x - 2 * self.field_width) and self.whites[k].y == (self.blacks[j].y + 2 * self.field_width):
                                result[6] = "left-down"
                                result[8] = i
                                break
                            elif self.blacks[k].x == (self.blacks[j].x - 2 * self.field_width) and self.blacks[k].y == (self.blacks[j].y + 2 * self.field_width):
                                result[6] = "left-down"
                                result[8] = i
                                break
                if (self.blacks[j].y + self.field_width) >= self.width:
                    result[5] = "right-down"
                    result[6] = "left-down"
                    result[7] = i  
            return result

    def move_posibility(self):
        if Game.player == 1:
            j = Game.index_w
            for i in range(0, 8):
                if self.whites[i].x != -100 and self.whites[i].y != -100:
                    Game.index_w = i
                    if isinstance(self.whites[i], Queen):
                        walls = self.check_walls()
                        if not(walls[1] == "right" and walls[2] == "left" and walls[5] == "right-down" and walls[6] == "left-down"):
                            Game.index_w = j
                            return True
                    else:
                        walls = self.check_walls()
                        if not(walls[1] == "right" and walls[2] == "left"):
                            Game.index_w = j
                            return True
            Game.index_w = j
            self.white_alives = 0
            return False
        if Game.player == 2:
            j = Game.index_b
            for i in range(0, 8):
                if self.blacks[i].x != -100 and self.blacks[i].y != -100:
                    Game.index_b = i
                    if isinstance(self.blacks[i], Queen):
                        walls = self.check_walls()
                        if not(walls[1] == "right" and walls[2] == "left" and walls[5] == "right-down" and walls[6] == "left-down"):
                            Game.index_b = j
                            return True
                    else:
                        walls = self.check_walls()
                        if not(walls[1] == "right" and walls[2] == "left"):
                            Game.index_b = j
                            return True
            Game.index_b = j
            self.black_alives = 0
            return False

    def is_queen(self, player):
        if player == 1:
            j = Game.index_w
            if isinstance(self.whites[j], Pawn):
                for i in range(1, 8, 2):
                    if self.whites[j].y == 750 and self.whites[j].x == i * self.field_width + 50:
                        self.whites[j] = Queen(self.whites[j].x, self.whites[j].y, self.whites[j].color)
                        Game.player = 2
                        break
        elif player == 2:
            j = Game.index_b
            if isinstance(self.blacks[j], Pawn):
                for i in range(0, 8, 2):
                    if self.blacks[j].y == 50 and self.blacks[j].x == i * self.field_width + 50:
                        self.blacks[j] = Queen(self.blacks[j].x, self.blacks[j].y, self.blacks[j].color)
                        Game.player = 1
                        break

    def reset_button(self, coord):
        if coord[0] >= 815 and coord[0] <= 890 and coord[1] >= 635 and coord[1] <= 660:
            return False
        else:
            return True

    def end_button(self, coord):
        if coord[0] >= 815 and coord[0] <= 890 and coord[1] >= 740 and coord[1] <= 770:
            return False
        else:
            return True

#podwojnie jest kill bo gdy raz zbiije to tylko na tym samym moze sie podwojne wywolac        
    def game_loop(self, coord, walls, kill_ind, screen, punch_sound, fatality_sound, fatalityImg, finish_him_sound):
        if Game.player == 1:
            j = kill_ind[0]
            try:
                self.white_must_kill = self.someone_can_kill()
                if self.white_must_kill == True:
                    raise Have_to_kill_exception
                else:
                    Game.have_to_kill_w = False
            except Have_to_kill_exception:
                Game.have_to_kill_w = True
            print("white_must_kill", self.white_must_kill)
            print("white_must_kill_second", self.white_must_kill_second)
            print("walls", walls)
            print("kill_ind", kill_ind)
            print("")
            if self.white_must_kill == False and self.move_posibility() == True:
                moved = self.whites[j].make_move(self.player, self.white_must_kill, coord, self.field_width, walls)
                if moved == True:
                    self.is_queen(1)
                    Game.index_w = -1
            elif self.white_must_kill_second == True and Game.index_w == self.kill_counter_w:
                killed = self.whites[j].kill(Game.player, coord, self.field_width, kill_ind, j)
                if Game.white_kill == True:
                    fatality_sound.play()
                    screen.blit(fatalityImg, (0, 0))
                    pygame.display.update()
                    time.sleep(1)
                    self.black_alives -= 1
                    self.is_queen(1)
                    self.blacks[killed].x = -100
                    self.blacks[killed].y = -100
                    self.kill_counter_w = j
                    walls = self.check_walls()
                    if not(walls[1] == "right" and walls[2] == "left") or (isinstance(self.whites[self.kill_counter_w], Queen) and not(walls[1] == "right" and walls[2] == "left" and walls[5] == "right-down" and walls[6] == "left-down")):
                        kill_ind = self.posibility_to_kill(walls)
                        if kill_ind[1] == "right" or kill_ind[2] == "left" or (isinstance(self.whites[self.kill_counter_w], Queen) and (kill_ind[5] == "right-down" or kill_ind[6] == "left-down")):
                            Game.index_w = self.kill_counter_w
                            self.white_must_kill_second = True
                            Game.white_kill = False
                        else:
                            Game.player = 2
                            self.white_must_kill = False
                            self.white_must_kill_second = False
                            Game.white_kill = False
                            Game.index_w = -1
                            Game.have_to_kill_w = False
                    else:
                        Game.player = 2
                        self.white_must_kill = False
                        self.white_must_kill_second = False
                        Game.white_kill = False
                        Game.index_w = -1
                        Game.have_to_kill_w = False
                elif kill_ind[1] == "right" or kill_ind[2] == "left" or (isinstance(self.whites[self.kill_counter_w], Queen) and (kill_ind[5] == "right-down" or kill_ind[6] == "left-down")):
                    finish_him_sound.play()
            elif self.white_must_kill == True and self.white_must_kill_second == False:
                killed = self.whites[j].kill(Game.player, coord, self.field_width, kill_ind, j)
                if Game.white_kill == True:
                    punch_sound.play(loops=0, maxtime=0, fade_ms=0)
                    self.black_alives -= 1
                    self.is_queen(1)
                    self.blacks[killed].x = -100
                    self.blacks[killed].y = -100
                    self.kill_counter_w = j
                    walls = self.check_walls()
                    if not(walls[1] == "right" and walls[2] == "left") or (isinstance(self.whites[self.kill_counter_w], Queen) and not(walls[1] == "right" and walls[2] == "left" and walls[5] == "right-down" and walls[6] == "left-down")):
                        kill_ind = self.posibility_to_kill(walls)
                        if kill_ind[1] == "right" or kill_ind[2] == "left" or (isinstance(self.whites[self.kill_counter_w], Queen) and (kill_ind[5] == "right-down" or kill_ind[6] == "left-down")):
                            Game.index_w = self.kill_counter_w
                            self.white_must_kill_second = True
                            Game.white_kill = False
                        else:
                            Game.player = 2
                            self.white_must_kill = False
                            self.white_must_kill_second = False
                            Game.white_kill = False
                            Game.index_w = -1
                            Game.have_to_kill_w = False
                    else:
                        Game.player = 2
                        self.white_must_kill = False
                        self.white_must_kill_second = False
                        Game.white_kill = False
                        Game.index_w = -1
                        Game.have_to_kill_w = False
                elif kill_ind[1] == "right" or kill_ind[2] == "left" or (isinstance(self.whites[self.kill_counter_w], Queen) and (kill_ind[5] == "right-down" or kill_ind[6] == "left-down")):
                    finish_him_sound.play()
        elif Game.player == 2:
            j = kill_ind[0]
            self.black_must_kill = self.someone_can_kill()
            try:
                self.black_must_kill = self.someone_can_kill()
                if self.black_must_kill == True:
                    raise Have_to_kill_exception
                else:
                    Game.have_to_kill_b = False
            except Have_to_kill_exception:
                Game.have_to_kill_b = True
            #Game.have_to_kill_b = self.black_must_kill
            print("black_must_kill", self.black_must_kill)
            print("black_must_kill_second", self.black_must_kill_second)
            print("walls", walls)
            print("kill_ind", kill_ind)
            print("")
            if self.black_must_kill == False and self.move_posibility() == True:
                moved = self.blacks[j].make_move(self.player, self.black_must_kill, coord, self.field_width, walls)
                if moved == True:
                    self.is_queen(2)
                    Game.index_b = -1
            elif self.black_must_kill_second == True and Game.index_b == self.kill_counter_b:
                killed = self.blacks[j].kill(Game.player, coord, self.field_width, kill_ind, j)
                if Game.black_kill == True:
                    fatality_sound.play()
                    screen.blit(fatalityImg, (0, 0))
                    pygame.display.update()
                    time.sleep(1)
                    self.white_alives -= 1
                    self.is_queen(2)
                    self.whites[killed].x = -100
                    self.whites[killed].y = -100
                    self.kill_counter_b = j
                    walls = self.check_walls()
                    if not(walls[1] == "right" and walls[2] == "left") or (isinstance(self.blacks[self.kill_counter_b], Queen) and not(walls[1] == "right" and walls[2] == "left" and walls[5] == "right-down" and walls[6] == "left-down")):
                        kill_ind = self.posibility_to_kill(walls)
                        if kill_ind[1] == "right" or kill_ind[2] == "left" or (isinstance(self.blacks[self.kill_counter_b], Queen) and (kill_ind[5] == "right-down" or kill_ind[6] == "left-down")):
                            Game.index_b = self.kill_counter_b
                            self.black_must_kill_second = True
                            Game.black_kill = False
                        else:
                            Game.player = 1
                            self.black_must_kill = False
                            self.black_must_kill_second = False
                            Game.black_kill = False
                            Game.index_b = -1
                            Game.have_to_kill_b = False
                    else:
                        Game.player = 1
                        self.black_must_kill = False
                        self.black_must_kill_second = False
                        Game.black_kill = False
                        Game.index_b = -1
                        Game.have_to_kill_b = False
                elif kill_ind[1] == "right" or kill_ind[2] == "left" or (isinstance(self.blacks[self.kill_counter_b], Queen) and (kill_ind[5] == "right-down" or kill_ind[6] == "left-down")):
                    finish_him_sound.play()
            elif self.black_must_kill == True and self.black_must_kill_second == False:
                killed = self.blacks[j].kill(Game.player, coord, self.field_width, kill_ind, j)
                if Game.black_kill == True:
                    punch_sound.play()
                    self.white_alives -= 1
                    self.is_queen(2)
                    self.whites[killed].x = -100
                    self.whites[killed].y = -100
                    self.kill_counter_b = j
                    walls = self.check_walls()
                    if not(walls[1] == "right" and walls[2] == "left") or (isinstance(self.blacks[self.kill_counter_b], Queen) and not(walls[1] == "right" and walls[2] == "left" and walls[5] == "right-down" and walls[6] == "left-down")):
                        kill_ind = self.posibility_to_kill(walls)
                        if kill_ind[1] == "right" or kill_ind[2] == "left" or (isinstance(self.blacks[self.kill_counter_b], Queen) and (kill_ind[5] == "right-down" or kill_ind[6] == "left-down")):
                            Game.index_b = self.kill_counter_b
                            self.black_must_kill_second = True
                            Game.black_kill = False
                        else:
                            Game.player = 1
                            self.black_must_kill = False
                            self.black_must_kill_second = False
                            Game.black_kill = False
                            Game.index_b = -1
                            Game.have_to_kill_b = False
                    else:
                        Game.player = 1
                        self.black_must_kill = False
                        self.black_must_kill_second = False
                        Game.black_kill = False
                        Game.index_b = -1
                        Game.have_to_kill_b = False
                elif kill_ind[1] == "right" or kill_ind[2] == "left" or (isinstance(self.blacks[self.kill_counter_b], Queen) and (kill_ind[5] == "right-down" or kill_ind[6] == "left-down")):
                    finish_him_sound.play()
        
    
#generator do przenoszenia pionkow zapisany w zakladce, bad move bedzie z generatora (funkcja bedzie zwracac true or false
#sprawdzic czemu reszta moze sie ruszac gdy jest mozliwosc bicia i jest sciana
#w killu nie zmieniac gracza

#someone_can_kill sprawdzic, ale raczej dobrze dziala
#!!! someone_can_kill to sprawdzic bo to chyba nawala
#bicie w dwóch kierunkach poparwic bo cos sie ryje
#krolowke posprawdzac na prawo
#krolowka biecie w prawo w tyl biala cos nie pyka
#czarny krolowka w prawo w tyl tez cos nie pyka


