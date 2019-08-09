import pygame, time
pygame.init()
from button import *

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

def msg(gameDisplay, text, font, colour, pos):
    text_surface = font.render(text, True, colour)
    gameDisplay.blit(text_surface, (pos[0] - (text_surface.get_width()/2), pos[1] - (text_surface.get_height()/2))) #position minus half of text size in order to center it. 


def start_loop(gameDisplay, p1_name, p2_name):
    Exitgame = False
    
    score_list = ["Love", "15", "30", "40", "adv", "win"]

    p1_win = False
    p2_win = False
    p1_score = 0 #these values correspond to the indexes in score_list. eg: 0 is "Love" and 3 is 40.
    p2_score = 0
    #BUTTONS
    p1_left_btn = button((255,255,255,100), (255,255, 255,190), (1*gameDisplay.get_width()/2) - 125, (1 * gameDisplay.get_height()/4) - 25, 50, 50, "<")
    p1_right_btn = button((255,255,255,100), (255,255, 255,190), (1*gameDisplay.get_width()/2) + 75, (1 * gameDisplay.get_height()/4) - 25, 50, 50, ">")
    p2_left_btn = button((255,255,255,100), (255,255, 255,190), (1*gameDisplay.get_width()/2) - 125, (1 * gameDisplay.get_height()* 3/4) - 25, 50, 50, "<")
    p2_right_btn = button((255,255,255,100), (255,255, 255,190), (1*gameDisplay.get_width()/2) + 75, (1 * gameDisplay.get_height()* 3/4) - 25, 50, 50, ">")

    bg = pygame.transform.scale(pygame.image.load("tennnis.jpg"), (gameDisplay.get_width(),gameDisplay.get_height()))
    deuce = False   #True when score is 40-40
    while not Exitgame:
        #start_message(gameDisplay)
        #mouse = pygame.mouse.get_pos()
        #click = pygame.mouse.get_pressed() 
        pygame.display.update()
        gameDisplay.blit(bg, (0,0)) #Sets background img
       
        textSurf, textRect = text_objects(p1_name, text_medium, white) #would be Player_1 + " Score" when put in main program
        textRect.center = ((gameDisplay.get_width()/2)/2), ((gameDisplay.get_height()/2)/2) #defines text for player 1 score
        gameDisplay.blit(textSurf, textRect)

        textSurf, textRect = text_objects(p2_name, text_medium, white) #would be Player_2 + " Score" when put in main program
        textRect.center = ((gameDisplay.get_width()/2)/2), (gameDisplay.get_height()/1.3333) #defines text for player 2 score
        gameDisplay.blit(textSurf, textRect)
      

        #Drawing all the buttons: 
        p1_left_btn.draw(gameDisplay)     
        p1_right_btn.draw(gameDisplay)     
        p2_left_btn.draw(gameDisplay)        
        p2_right_btn.draw(gameDisplay)

        msg(gameDisplay, score_list[p1_score], text_medium, (255,255,255), (gameDisplay.get_width()/2, gameDisplay.get_height()/4)) 
        msg(gameDisplay, score_list[p2_score], text_medium, (255,255,255), (gameDisplay.get_width()/2, gameDisplay.get_height()* 3/4)) 
         
        if p1_right_btn.pressed: #player 1 gets a point
            if p1_score == 3:
                if p2_score >= 3:
                    p1_score += 1
                else:
                    p1_score += 2        
            else:
               p1_score += 1
            p1_right_btn.pressed = False 

        if p2_right_btn.pressed:    #player 2 gets a point
            if p2_score == 3:
                if p1_score >= 3:
                    p2_score += 1
                else:
                    p2_score += 2        
            else:
               p2_score += 1 
            p2_right_btn.pressed = False 

        if p1_left_btn.pressed:     #player 1 loses a point
            if p1_score != 0:
                p1_score -= 1
            p1_left_btn.pressed = False

        if p2_left_btn.pressed:     #player 2 loses a point
            if p2_score != 0:
                p2_score -= 1  
            p2_left_btn.pressed = False
 
        if p1_score >= 3 and p2_score >= 3 and p1_score == p2_score: #Checking for deuce
            msg(gameDisplay,"DEUCE", text_medium, (255,255,255), (gameDisplay.get_width()/2, gameDisplay.get_height()/2))
            deuce = True
            p1_score = 3
            p2_score = 3 
        else:
            deuce = False

        if p1_score == 3 or p2_score == 3: #Checking for match point
            if p1_score != 4 and p2_score != 4:
                if not deuce:
                    msg(gameDisplay,"MATCH POINT", text_medium, (255,255,255), (gameDisplay.get_width()/2, gameDisplay.get_height()/2))

        if p1_score == 5:
            return [score_list[p1_score], score_list[p2_score]]
            p1_win = True
            #p1_winner screen

        if p2_score == 5:
            return [score_list[p1_score], score_list[p2_score]]
            p1_win = True
            #p2_winner screen

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
