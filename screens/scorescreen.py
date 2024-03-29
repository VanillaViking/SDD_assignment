import pygame, time
pygame.init()
from button import *
from dashboard import *
from score_history import *
pygame.display.set_caption("TENNIS SCOREKEEPER")

clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)
green = (0,255,0)

text_large = pygame.font.SysFont('Arial',50)
text_small = pygame.font.SysFont('Arial',20)
text_medium = pygame.font.SysFont('Arial',25)

        
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def msg(gameDisplay, text, font, colour, pos):
    text_surface = font.render(text, True, colour)
    gameDisplay.blit(text_surface, (pos[0] - (text_surface.get_width()/2), pos[1] - (text_surface.get_height()/2))) #position minus half of text size in order to center it. 



#----------------------------------------------------------------------------------MAIN LOOP------------------------------------------------------------------------

def start_loop(gameDisplay, p1_name, p2_name, p1_matches_won, p2_matches_won, p1_sets, p2_sets, num_sets, point_list):
    Exitgame = False
    
    score_list = ["Love", "15", "30", "40", "ADV", "win"]

    p1_win = False
    p2_win = False
    p1_score = 0 #these values correspond to the indexes in score_list. eg: 0 is "Love" and 3 is 40.
    p2_score = 0
    #BUTTONS
    
    p1_left_btn = button([255,255,255,100], [255,255, 255,190], (1*gameDisplay.get_width()/2) - 125, (1 * gameDisplay.get_height()/4) - 25, 50, 50, "-")
    p1_right_btn = button([255,255,255,100], [255,255, 255,190], (1*gameDisplay.get_width()/2) + 75, (1 * gameDisplay.get_height()/4) - 25, 50, 50, "+")
    p2_left_btn = button([255,255,255,100], [255,255, 255,190], (1*gameDisplay.get_width()/2) - 125, (1 * gameDisplay.get_height()* 2/4) - 25, 50, 50, "-")
    p2_right_btn = button([255,255,255,100], [255,255, 255,190], (1*gameDisplay.get_width()/2) + 75, (1 * gameDisplay.get_height()* 2/4) - 25, 50, 50, "+")

    back_btn = button([255,255,255,100], [255,255,255,190], 0, 0, 100, 37, "Back",(0,0,0,255)) #back

    #DASHBOARD
    dash = dashboard(gameDisplay, p1_name, p2_name, p1_matches_won, p2_matches_won, p1_sets, p2_sets)
    
    
    bg = pygame.transform.scale(pygame.image.load("pictures/tennnis.jpg"), (gameDisplay.get_width(),gameDisplay.get_height()))
    deuce = False   #True when score is 40-40
    while not Exitgame:
        #start_message(gameDisplay)
        #mouse = pygame.mouse.get_pos()
        #click = pygame.mouse.get_pressed() 
        pygame.display.update()
        gameDisplay.blit(bg, (0,0)) #Sets background img
       
        msg(gameDisplay, p1_name.upper(), text_medium, (190,190,190), (gameDisplay.get_width()/2, gameDisplay.get_height()/4 - 50))
        msg(gameDisplay, p2_name.upper(), text_medium, (190,190,190), (gameDisplay.get_width()/2, gameDisplay.get_height()* 2/4 - 50))
      

        #Drawing all the buttons: 
        p1_left_btn.draw(gameDisplay)     
        p1_right_btn.draw(gameDisplay)     
        p2_left_btn.draw(gameDisplay)        
        p2_right_btn.draw(gameDisplay)
        back_btn.draw(gameDisplay)

        #Draw dashboard
        dash.draw()

        #Draw score history
        draw_score_hist(gameDisplay, p1_name, p2_name, num_sets, point_list)

        msg(gameDisplay, score_list[p1_score], text_medium, (255,255,255), (gameDisplay.get_width()/2, gameDisplay.get_height()/4)) 
        msg(gameDisplay, score_list[p2_score], text_medium, (255,255,255), (gameDisplay.get_width()/2, gameDisplay.get_height()* 2/4)) 
        
        
         
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

        if back_btn.pressed:
            return "back"

        if p1_score >= 3 and p2_score >= 3 and p1_score == p2_score: #Checking for deuce
            msg(gameDisplay,"DEUCE", text_large, (68,252,243), (gameDisplay.get_width()/2, gameDisplay.get_height()* 11/12))
            deuce = True
            p1_score = 3
            p2_score = 3 
        else:
            deuce = False

        if p1_score == 3 or p2_score == 3: #Checking for match point
            if p1_score != 4 and p2_score != 4:
                if not deuce:
                    msg(gameDisplay,"MATCH POINT", text_large, (68,252,243), (gameDisplay.get_width()/2, gameDisplay.get_height() * 11/12))

        if p1_score == 5:
            #return [score_list[p1_score], score_list[p2_score]]
            p1_win = True
            return "p1"
            #p1_winner screen

        if p2_score == 5:
            #return [score_list[p1_score], score_list[p2_score]]
            p1_win = True
            return "p2"
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
            back_btn.update(event)            

       # clock.tick(30) ##sets frame rate
#start_loop() ##uncomment when adding to main program
#pygame.quit() #quit command
#quit() 
