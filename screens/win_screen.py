import pygame, time
from button import *
from score_history import *

clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)
green = (0,255,0)

text_large = pygame.font.Font('freesansbold.ttf',50)
text_small = pygame.font.Font('freesansbold.ttf',20)
text_medium = pygame.font.SysFont('Arial',25)


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def msg(DISPLAY, text, font, colour, pos):
    text_surface = font.render(text, True, colour)
    DISPLAY.blit(text_surface, (pos[0] - (text_surface.get_width()/2), pos[1] - (text_surface.get_height()/2))) #position minus half of text size in order to center it. 


def win_loop(DISPLAY, winning_player, player1_name, player2_name, num_sets, score_list): #displays winning text
    bg = pygame.transform.scale(pygame.image.load("pictures/tennnis.jpg"), (DISPLAY.get_width(),DISPLAY.get_height()))
    exit_btn = button((255,255,255,100), (255,255, 255,190), (DISPLAY.get_width() /2) - 100, (DISPLAY.get_height()* 7/8)-(37), 200, 75, "Exit",(0,0,0,255))

    while not exit_btn.pressed:
        pygame.display.update()
        DISPLAY.blit(bg, (0,0))
        if winning_player == "p1": #checking which player won
            textSurf, textRect = text_objects(player1_name + " wins!", text_large, white)
            textRect.center = (DISPLAY.get_width()/2), ((DISPLAY.get_height()/2)-15)
            DISPLAY.blit(textSurf, textRect)
        else:
            textSurf, textRect = text_objects(player2_name + " wins!", text_large, white)
            textRect.center = (DISPLAY.get_width()/2), ((DISPLAY.get_height()/2)-15)
            DISPLAY.blit(textSurf, textRect)

        draw_score_hist(DISPLAY, player1_name, player2_name, num_sets, score_list)        # Draws the history of the points in each set
        exit_btn.draw(DISPLAY)
        for event in pygame.event.get(): #i don't know if this is needed here or not but i'm putting this here just in case
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()
                Exitgame = True
            exit_btn.update(event)
