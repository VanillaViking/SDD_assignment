import pygame
from button import *
from text_input import *
from truefalse import *
arial = pygame.font.SysFont('Arial', 30)

#function called whenever screen needs to be drawn
def draw(DISPLAY):
    #for error msg
    count = 241

    cont_button = button((255,255,255,100), (255,255, 255,190), (4*DISPLAY.get_width() /5) - 100, ((4 * DISPLAY.get_height())/6)-(37), 200, 75, "Continue",(0,0,0,255)) #continue
    doubles = tf(DISPLAY, 3*DISPLAY.get_width()/5, DISPLAY.get_height()/5, 10, "", (255,255,255)) #whether game is doubles
    
    
    bg_image = pygame.transform.scale(pygame.image.load("tennnis.jpg"), (DISPLAY.get_width(),DISPLAY.get_height()))

    #player name fields
    player1_name = text_input(DISPLAY, 3*DISPLAY.get_width()/5, DISPLAY.get_height()/5 + 100 - 37, 350, 75,"",(255,255,255))
    player2_name = text_input(DISPLAY, 3*DISPLAY.get_width()/5, DISPLAY.get_height()/5 + 200-37, 350, 75,"",(255,255,255))

    sets = text_input(DISPLAY, 3*DISPLAY.get_width()/5, DISPLAY.get_height()/5 + 300-37, 100, 75,"",(255,255,255))

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
        if count < 200:
            DISPLAY.blit(SFONT.render("Sets should be a number!", True, (255,0,0)),((DISPLAY.get_width()/2) -(149/2), (DISPLAY.get_height() *2)/3))

            count += 1

