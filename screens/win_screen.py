import pygame, time
from button import *

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

def msg(gameDisplay, text, font, colour, pos):
    text_surface = font.render(text, True, colour)
    gameDisplay.blit(text_surface, (pos[0] - (text_surface.get_width()/2), pos[1] - (text_surface.get_height()/2))) #position minus half of text size in order to center it. 


def win_loop: #displays winning text
    if p1_win = True:
        textSurf, textRect = text_objects(player1_name + " wins", text_large, white)
        textRect.center = (DISPLAY.get_width()/2), ((DISPLAY.get_height()/2)-15)
        gameDisplay.blit(textSurf, textRect)
    if p2_win = True:
        textSurf, textRect = text_objects(player2_name + " wins", text_large, white)
        textRect.center = (DISPLAY.get_width()/2), ((DISPLAY.get_height()/2)-15)
        gameDisplay.blit(textSurf, textRect)
