import pygame, time
pygame.init()

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

def start_message(gameDisplay):
    text_display(gameDisplay, "Tennis Scorekeeper", text_large, white)
def start_button_text(gameDisplay):
    text_display(gameDisplay, "Start", text_small, white)
def options_text(gameDisplay):
    text_display(gameDisplay, "Options", text_small, white)
def startcommand(gameDisplay):
    pass
    #placeholder
def optionscommand():
    pass
    #placeholder

def start_loop(gameDisplay):
    #startx =  (gameDisplay.get_width() * 0.45)
    #starty = (gameDisplay.get_height() * 0.8)
    Exitgame = False
    gameDisplay.blit(pygame.transform.scale(pygame.image.load("pictures/tennnis.jpg"), (gameDisplay.get_width(),gameDisplay.get_height())), (0,0)) #Sets background img
    button_width = (gameDisplay.get_width() - 50)/2
    button_height = (gameDisplay.get_height() - 100)/2
    options_button_width = (gameDisplay.get_width() - 50)/2
    options_button_height = ((gameDisplay.get_height() - 100)/2+100)
    while not Exitgame:
        start_message(gameDisplay)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if button_width+100 > mouse[0] > button_width and button_height+50 > mouse[1] > button_height:
            pygame.draw.rect(gameDisplay, gray,((gameDisplay.get_width() - 50)/2,(gameDisplay.get_height() - 100)/2,100,50))
            if click[0] == 1:
                startcommand(gameDisplay) ###Defines what happen when the button is pressed
                return "start"
        ###Creates the start button
        else:
            pygame.draw.rect(gameDisplay, black,((gameDisplay.get_width() - 50)/2,(gameDisplay.get_height() - 100)/2,100,50))

        if options_button_width+100 > mouse[0] > options_button_width and options_button_height+50 > mouse[1] > options_button_height:
            pygame.draw.rect(gameDisplay, gray,((gameDisplay.get_width() - 50)/2,((gameDisplay.get_height() - 100)/2)+100,100,50))
            if click[0] == 1:
                optionscommand() ###Defines what happen when the button is pressed
                return "opts"
        ###Creates the options button
        else:
            pygame.draw.rect(gameDisplay, black,((gameDisplay.get_width() - 50)/2,((gameDisplay.get_height() - 100)/2)+100,100,50))    
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
                pygame.QUIT
                quit()
                Exitgame = True
            #if event.type == pygame.KEYDOWN:
             #   if event.key == pygame.K_LEFT:
              #      start_b()
    
            #print(event)
        pygame.display.update()
        clock.tick(30) ##sets frame rate
#start_loop()
#pygame.quit() #quit command
#quit()
