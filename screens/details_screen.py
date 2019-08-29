import pygame
from button import *
from text_input import *
from truefalse import *
arial = pygame.font.SysFont('Arial', 30)


#function called whenever screen needs to be drawn
def draw(DISPLAY):
    #for error msg
    count = 241
    
    num_sets = None
    cont_button = button([255,255,255,100], [255,255,255,190], (4*DISPLAY.get_width() /5) - 100, ((4 * DISPLAY.get_height())/6)-(37), 200, 75, "Continue",(0,0,0,255)) #continue
    back_button = button([255,255,255,100], [255,255,255,190], (1*DISPLAY.get_width() /5) - 100, ((4 * DISPLAY.get_height())/6)-(37), 200, 75, "Back",(0,0,0,255)) #back
    doubles = tf(DISPLAY, 3*DISPLAY.get_width()/5, DISPLAY.get_height()/5, 10, "", (255,255,255)) #whether game is doubles
    
    
    bg_image = pygame.transform.scale(pygame.image.load("pictures/tennnis.jpg"), (DISPLAY.get_width(),DISPLAY.get_height()))

    #player name fields
    player1_name = text_input(DISPLAY, 3*DISPLAY.get_width()/5, DISPLAY.get_height()/5 + 100 - 37, 350, 75,"",(255,255,255))
    player2_name = text_input(DISPLAY, 3*DISPLAY.get_width()/5, DISPLAY.get_height()/5 + 200-37, 350, 75,"",(255,255,255))

    sets = text_input(DISPLAY, 3*DISPLAY.get_width()/5, DISPLAY.get_height()/5 + 300, 100, 75,"",(255,255,255))
    sets_1 = tf(DISPLAY, DISPLAY.get_width() * 8/10, DISPLAY.get_height()/5 + 300, 10, "1", (255,255,255))
    sets_3 = tf(DISPLAY, DISPLAY.get_width() * 6/10, DISPLAY.get_height()/5 + 300, 10, "3", (255,255,255))
    sets_5 = tf(DISPLAY, DISPLAY.get_width() * 7/10, DISPLAY.get_height()/5+ 300, 10, "5", (255,255,255))
    
    #text
    doubles_text = arial.render("Doubles:", True, (255,255,255))

    player1_text = arial.render("Player 1:", True, (255,255,255))
    player2_text = arial.render("Player 2:", True, (255,255,255))

    team1_text = arial.render("Team 1:", True, (255,255,255))
    team2_text = arial.render("Team 2:", True, (255,255,255))

    sets_text = arial.render("No. of sets:", True, (255,255,255))
    while True:
        pygame.display.update()
        DISPLAY.fill((255,255,255))

        #drawing all of the objects on to the screen
        DISPLAY.blit(bg_image, (0,0))
        cont_button.draw(DISPLAY)
        back_button.draw(DISPLAY)
        doubles.draw(True)
        DISPLAY.blit(doubles_text, ((2 * DISPLAY.get_width()/5), DISPLAY.get_height()/5 - doubles_text.get_height()/2))
        player1_name.draw()
        player2_name.draw()
        sets_1.draw(True)
        sets_3.draw(True)
        sets_5.draw(True)

        if doubles.active: #display either "player" or "team" depending on if doubles is checked. 
            DISPLAY.blit(team1_text, ((2 * DISPLAY.get_width()/5), DISPLAY.get_height()/5 - team1_text.get_height()/2 + 100))
            DISPLAY.blit(team2_text, ((2 * DISPLAY.get_width()/5), DISPLAY.get_height()/5 - team2_text.get_height()/2 + 200))
        else:
            DISPLAY.blit(player1_text, ((2 * DISPLAY.get_width()/5), DISPLAY.get_height()/5 - player1_text.get_height()/2 + 100))
            DISPLAY.blit(player2_text, ((2 * DISPLAY.get_width()/5), DISPLAY.get_height()/5 - player2_text.get_height()/2 + 200))
        
        DISPLAY.blit(sets_text, ((2 * DISPLAY.get_width()/5), DISPLAY.get_height()/5 - sets_text.get_height()/2 + 300))


        for event in pygame.event.get():
            #Activating or updating the objects 
            cont_button.update(event)
            back_button.update(event)
            doubles.activate(event)
            player1_name.activate(event)
            player2_name.activate(event)
            sets_3.activate(event)            
            sets_5.activate(event)            

            if event.type == pygame.QUIT: #command for quitting the program
                quit()
                pygame.QUIT
            
            if cont_button.pressed:
                    if sets_3.active:
                        num_sets = 3
                    elif sets_5.active:
                        num_sets = 5
                    elif sets_1.active:
                        num_sets = 1
                    try:
                        return [player1_name.text, player2_name.text, int(num_sets)]
                    except TypeError:
                        cont_button.pressed = False
                        count = 0
                        clr_val = 0
            
            if back_button.pressed:
                return "back"
        #error msg fades away nicely.
        if count < 200:
            DISPLAY.blit(SFONT.render("Sets should be a number!", True, (255,0,0)),((DISPLAY.get_width()/2) -(149/2), (DISPLAY.get_height() *2)/3))

            count += 1
        

        if sets_3.clicked: #Deactivates other set options when a set number is selected
            sets_5.active = False
            sets_1.active = False
        if sets_5.clicked:
            sets_3.active = False
            sets_1.active = False

