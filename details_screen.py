import pygame
from button import *
from text_input import *
from truefalse import *
arial = pygame.font.SysFont('Arial', 30)

#function called whenever screen needs to be drawn
def draw(DISPLAY):
    #for error msg
    count = 181
    clr_val = 0

    cont_button = button([200,200,200], (190,0, 230), (8*DISPLAY.get_width() /9) - 100, ((6 * DISPLAY.get_height())/7), 200, 75, "Continue") #continue
    doubles = tf(DISPLAY, 3*DISPLAY.get_width()/5, DISPLAY.get_height()/5, 10, "") #whether game is doubles
    
    #player name fields
    player1_name = text_input(DISPLAY, 3*DISPLAY.get_width()/5, DISPLAY.get_height()/5 + 100 - 37, 350, 75)
    player2_name = text_input(DISPLAY, 3*DISPLAY.get_width()/5, DISPLAY.get_height()/5 + 200-37, 350, 75)

    sets = text_input(DISPLAY, 3*DISPLAY.get_width()/5, DISPLAY.get_height()/5 + 300-37, 100, 75)

    #text
    doubles_text = arial.render("Doubles:", True, (0,0,0))

    player1_text = arial.render("Player 1:", True, (0,0,0))
    player2_text = arial.render("Player 2:", True, (0,0,0))

    team1_text = arial.render("Team 1:", True, (0,0,0))
    team2_text = arial.render("Team 2:", True, (0,0,0))

    sets_text = arial.render("No. of sets:", True, (0,0,0))
    while True:
        pygame.display.update()
        DISPLAY.fill((255,255,255))

        #drawing all of the objects on to the screen
        cont_button.draw(DISPLAY)
        doubles.draw(False)
        DISPLAY.blit(doubles_text, ((2 * DISPLAY.get_width()/5), DISPLAY.get_height()/5 - doubles_text.get_height()/2))
        player1_name.draw()
        player2_name.draw()
        sets.draw()

        if doubles.active: #display either "player" or "team" depending on if doubles is checked. 
            DISPLAY.blit(team1_text, ((2 * DISPLAY.get_width()/5), DISPLAY.get_height()/5 - team1_text.get_height()/2 + 100))
            DISPLAY.blit(team2_text, ((2 * DISPLAY.get_width()/5), DISPLAY.get_height()/5 - team2_text.get_height()/2 + 200))
        else:
            DISPLAY.blit(player1_text, ((2 * DISPLAY.get_width()/5), DISPLAY.get_height()/5 - player1_text.get_height()/2 + 100))
            DISPLAY.blit(player2_text, ((2 * DISPLAY.get_width()/5), DISPLAY.get_height()/5 - player2_text.get_height()/2 + 200))
        
        DISPLAY.blit(sets_text, ((2 * DISPLAY.get_width()/5), DISPLAY.get_height()/5 - sets_text.get_height()/2 + 300))

        for event in pygame.event.get():
            cont_button.update(event)
            doubles.activate(event)
            player1_name.activate(event)
            player2_name.activate(event)
            sets.activate(event)

            if event.type == pygame.QUIT:
                quit()
                pygame.QUIT
            
            if cont_button.pressed:
                    try:
                        int(sets.text)
                        return [player1_name.text, player2_name.text, sets.text]
                    except ValueError:
                        cont_button.pressed = False
                        count = 0
                        clr_val = 0
        #error msg fades away nicely.
        if count < 180:
            DISPLAY.blit(SFONT.render("Enter valid inputs", True, (255,clr_val,clr_val)),((1920/2) -(149/2), 750))
            if count > 60:
                clr_val += 2
                if clr_val > 255:
                    clr_val = 255

            count += 1

