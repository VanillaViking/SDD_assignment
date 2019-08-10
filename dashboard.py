import pygame
from button import *
text_large = pygame.font.Font('freesansbold.ttf',50)
text_small = pygame.font.SysFont('Arial',20)
text_medium = pygame.font.SysFont('Arial',25)

def msg(DISPLAY, text, font, colour, pos):
    text_surface = font.render(text, True, colour)
    DISPLAY.blit(text_surface, (pos[0] - (text_surface.get_width()/2), pos[1])) #position minus half of text size in order to center it.




class dashboard():
    def __init__(self, DISPLAY,p1_name, p2_name, p1_matches_won, p2_matches_won, p1_sets_won, p2_sets_won):
        self.display = DISPLAY
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.p1_matches_won = p1_matches_won
        self.p2_matches_won = p2_matches_won

        self.p1_sets_won = p1_sets_won
        self.p2_sets_won = p2_sets_won
 
        self.bg = button((20,20,90,120), (20,20,90,120), 0, self.display.get_height()* 5/6, self.display.get_width(),self.display.get_height()/6, "")
        

    def draw(self):
        self.bg.draw(self.display)

        # PLAYER 1 STATS
        msg(self.display, self.p1_name.upper(), text_small, (200,200,200), (self.display.get_width()/4, self.display.get_height()* 15/18))
        msg(self.display, "Games won: " + str(self.p1_matches_won), text_small, (200,200,200), (self.display.get_width()/4, self.display.get_height()* 16/18))
        msg(self.display, "Sets won: " + str(self.p1_sets_won), text_small, (200,200,200), (self.display.get_width()/4, self.display.get_height()* 17/18))
        
        # PLAYER 2 STATS
        msg(self.display, self.p2_name.upper(), text_small, (200,200,200), (self.display.get_width()* 3/4, self.display.get_height()* 15/18))
        msg(self.display, "Games won: " + str(self.p2_matches_won), text_small, (200,200,200), (self.display.get_width()* 3/4, self.display.get_height()* 16/18))
        msg(self.display, "Sets won: " + str(self.p2_sets_won), text_small, (200,200,200), (self.display.get_width()* 3/4, self.display.get_height()* 17/18))
         
