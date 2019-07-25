#!/usr/bin/env python

import pygame
import details_screen
import tennis_startscreen
import options_screen
import os
import sys

pygame.init()

def restart():
    if sys.platform == "win32": #windows 
        os.execl(sys.executable, sys.executable, *sys.argv)
    else: #linux & macOS
        os.execv(__file__, sys.argv)

#Get the default settings from the text file.
for line in open("settings.txt"):
    if "resolution" in line:
        line = line.strip().split(",")
        resolution = (int(line[1]),int(line[2]))

DISPLAY = pygame.display.set_mode(resolution)

#----------------------------------------------------

while True: #loops until player hits "start" in first screen or "save and exit" in options screen.
    if tennis_startscreen.start_loop(DISPLAY) == "start":
        player1_name, player2_name, sets = details_screen.draw(DISPLAY)
        break
    else:
        if options_screen.draw(DISPLAY) == "exit":
            pygame.QUIT
            restart() #restart so that any changes come into effect
            quit()

