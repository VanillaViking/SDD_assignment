import pygame, time
pygame.init()
from button import *

#gameDisplay = 800  ##this is for testing the score screen individually. Comment when adding to main program
#gameDisplay.get_height() = 600
#gameDisplay = pygame.display.set_mode((gameDisplay,gameDisplay.get_height()))
#gameDisplay.get_width() = 1920
#gameDisplay.get_height() = 1080
#gameDisplay = pygame.display.set_mode((gameDisplay.get_width(),gameDisplay.get_height()))
pygame.display.set_caption("TENNIS SCOREKEEPER")

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

def text_display(gameDisplay, text, size, color): ###Instructions for displaying text. Trying to use Arial gave me an error
    #text_large = pygame.font.Font('freesansbold.ttf',50)
    #text_small = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, size, color)
    TextRect.center = ((gameDisplay.get_width()/2),(gameDisplay.get_height()/4))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def msg(gameDisplay, text, font, colour, pos):
    text_surface = font.render(text, True, colour)
    gameDisplay.blit(text_surface, (pos[0] - (text_surface.get_width()/2), pos[1] - (text_surface.get_height()/2))) #position minus half of text size in order to center it. 

def start_message(gameDisplay):
    text_display(gameDisplay, "Tennis Scorekeeper", text_large, white)
def start_button_text(gameDisplay):
    text_display(gameDisplay, "Start", text_small, white)
def options_text(gameDisplay):
    text_display(gameDisplay, "Options", text_small, white)
#def startcommand(gameDisplay):
#    pass
#    #placeholder
#def optionscommand():
#    pass
#    #placeholder

def start_loop(gameDisplay):
    #startx =  (gameDisplay.get_width() * 0.45)
    #starty = (gameDisplay.get_height() * 0.8)
    Exitgame = False

    #BUTTONS
    p1_left_btn = button((255,255,255,100), (255,255, 255,190), (1*gameDisplay.get_width()/2) - 125, (1 * gameDisplay.get_height()/4) - 25, 50, 50, "<")
    p1_right_btn = button((255,255,255,100), (255,255, 255,190), (1*gameDisplay.get_width()/2) + 75, (1 * gameDisplay.get_height()/4) - 25, 50, 50, ">")
    p2_left_btn = button((255,255,255,100), (255,255, 255,190), (1*gameDisplay.get_width()/2) - 125, (1 * gameDisplay.get_height()* 3/4) - 25, 50, 50, "<")
    p2_right_btn = button((255,255,255,100), (255,255, 255,190), (1*gameDisplay.get_width()/2) + 75, (1 * gameDisplay.get_height()* 3/4) - 25, 50, 50, ">")

    bg = pygame.transform.scale(pygame.image.load("tennnis.jpg"), (gameDisplay.get_width(),gameDisplay.get_height()))

    while not Exitgame:
        #start_message(gameDisplay)
        #mouse = pygame.mouse.get_pos()
        #click = pygame.mouse.get_pressed() 
        pygame.display.update()
        gameDisplay.blit(bg, (0,0)) #Sets background img
       
        textSurf, textRect = text_objects("Player 1 Score", text_medium, white) #would be Player_1 + " Score" when put in main program
        textRect.center = ((gameDisplay.get_width()/2)/2), ((gameDisplay.get_height()/2)/2) #defines text for player 1 score
        gameDisplay.blit(textSurf, textRect)

        textSurf, textRect = text_objects("Player 2 Score", text_medium, white) #would be Player_2 + " Score" when put in main program
        textRect.center = ((gameDisplay.get_width()/2)/2), (gameDisplay.get_height()/1.3333) #defines text for player 2 score
        gameDisplay.blit(textSurf, textRect)
      

        #Drawing all the buttons: 
        p1_left_btn.draw(gameDisplay)     
        p1_right_btn.draw(gameDisplay)     
        p2_left_btn.draw(gameDisplay)        
        p2_right_btn.draw(gameDisplay)      
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()
                Exitgame = True
            
            p1_left_btn.update(event)           
            p1_right_btn.update(event)
            p2_left_btn.update(event)
            p2_right_btn.update(event)            
 
       # clock.tick(30) ##sets frame rate
#start_loop() ##uncomment when adding to main program
#pygame.quit() #quit command
#quit() 
