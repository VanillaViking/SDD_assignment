import pygame, time
pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("TENNIS SCOREKEEPER")

clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)
green = (0,255,0)

text_large = pygame.font.Font('freesansbold.ttf',50)
text_small = pygame.font.Font('freesansbold.ttf',20)


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_display(text, size, color): ###Instructions for displaying text. Trying to use Arial gave me an error
    #text_large = pygame.font.Font('freesansbold.ttf',50)
    #text_small = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, size, color)
    TextRect.center = ((display_width/2),(display_height/4))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def start_message():
    text_display("Tennis Scorekeeper", text_large, black)
def start_button_text():
    text_display("Start", text_small, white)
def options_text():
    text_display("Options", text_small, white)
def startcommand():
    #placeholder
def optionscommand():
    #placeholder

def start_loop():
    #startx =  (display_width * 0.45)
    #starty = (display_height * 0.8)
    Exitgame = False
    gameDisplay.fill(white) #Sets background color
    button_width = (display_width - 50)/2
    button_height = (display_height - 100)/2
    options_button_width = (display_width - 50)/2
    options_button_height = ((display_height - 100)/2+100)
    while not Exitgame:
        start_message()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if button_width+100 > mouse[0] > button_width and button_height+50 > mouse[1] > button_height:
            pygame.draw.rect(gameDisplay, gray,((display_width - 50)/2,(display_height - 100)/2,100,50))
            if click[0] == 1:
                startcommand() ###Defines what happen when the button is pressed
        ###Creates the start button
        else:
            pygame.draw.rect(gameDisplay, black,((display_width - 50)/2,(display_height - 100)/2,100,50))

        if options_button_width+100 > mouse[0] > options_button_width and options_button_height+50 > mouse[1] > options_button_height:
            pygame.draw.rect(gameDisplay, gray,((display_width - 50)/2,((display_height - 100)/2)+100,100,50))
            if click[0] == 1:
                optionscommand() ###Defines what happen when the button is pressed
        ###Creates the options button
        else:
            pygame.draw.rect(gameDisplay, black,((display_width - 50)/2,((display_height - 100)/2)+100,100,50))    
        textSurf, textRect = text_objects("Start", text_small, white)
        textRect.center = (button_width+(100/2)), (button_height+(50/2))
        gameDisplay.blit(textSurf, textRect) #Defines text for start button
        #start_button_text()#Work in progress, probably will create a button function later
        #options_text()
        textSurf, textRect = text_objects("Options", text_small, white)
        textRect.center = (options_button_width+(100/2)), (options_button_height+(50/2))
        gameDisplay.blit(textSurf, textRect) #Defines text for options button
        #smallText = pygame.font.Font("freesansbold.ttf",20)
        #starttextSurf, starttextRect = text_objects("Start", smallText)
        #textRect.center = ( (150+(100/2)), (450+(50/2)) )
        #gameDisplay.blit(textSurf, textRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exitgame = True
            #if event.type == pygame.KEYDOWN:
             #   if event.key == pygame.K_LEFT:
              #      start_b()
    
            #print(event)
        pygame.display.update()
        clock.tick(30) ##sets frame rate
start_loop()
pygame.quit() #quit command
quit()