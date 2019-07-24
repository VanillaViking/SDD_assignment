import pygame
import details_screen
import tennis_startscreen
import options_screen

pygame.init()

#Get the default settings from the text file.
for line in open("settings.txt"):
    if "resolution" in line:
        line = line.strip().split(",")
        resolution = (int(line[1]),int(line[2]))

DISPLAY = pygame.display.set_mode(resolution)

#----------------------------------------------------

while True:
    if tennis_startscreen.start_loop(DISPLAY) == "start":
        player1_name, player2_name, sets = details_screen.draw(DISPLAY)
        break
    else:
        if options_screen.draw(DISPLAY) == "exit":
            pygame.QUIT
            quit()

