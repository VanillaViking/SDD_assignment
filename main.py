import pygame
import details_screen
import tennis_startscreen

pygame.init()

DISPLAY = pygame.display.set_mode((1920,1080))


#for game settings...
if tennis_startscreen.start_loop() == "start":
    player1_name, player2_name, sets = details_screen.draw(DISPLAY)
else:
    pass