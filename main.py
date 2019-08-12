#!/usr/bin/env python

import sys
import pygame

sys.path.append("screens/")
sys.path.append("interactables/")
import details_screen
import tennis_startscreen
import options_screen
import os
import scorescreen
#import win_screen

pygame.init()
pygame.mixer.init()
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
    if "volume" in line:
        line = line.strip().split(",")
        volume = float(line[1])


#MUSIC
bg_music = pygame.mixer.music.load("audio/bensound-inspire.mp3")
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play()

DISPLAY = pygame.display.set_mode(resolution)

#----------------------------------------------------

while True: #loops until player hits "start" in first screen or "save and exit" in options screen.
    if tennis_startscreen.start_loop(DISPLAY) == "start": #go to details screen
        details = details_screen.draw(DISPLAY)
        if details != "back":
            player1_name, player2_name, sets = details
            break
    else: #go to options screen
        if options_screen.draw(DISPLAY, volume) == "exit":
            pygame.QUIT
            restart() #restart so that any changes come into effect
            quit()
#while True: #displays results after game is won.            
 #   if scorescreen.start_loop(DISPLAY) == "end_game":
  #      results = winscreen.win_loop

def check_lead(p1_matches, p2_matches):
    if p1_matches - p2_matches >= 2 or p2_matches - p1_matches >= 2:
        return True
    else:
        return False

p1_sets_won = 0
p2_sets_won = 0

score_list = []

for n in range(sets):
    
    p1_matches_won = 0
    p2_matches_won = 0
    while p1_matches_won < 6 and p2_matches_won < 6 or not check_lead(p1_matches_won, p2_matches_won):      #loops until one of the players have won over 6 matches AND have a 2 point lead. 
        if scorescreen.start_loop(DISPLAY, player1_name, player2_name, p1_matches_won, p2_matches_won, p1_sets_won, p2_sets_won, sets) == "p1":
            p1_matches_won += 1
        else:
            p2_matches_won += 1
    else:
        if p1_matches_won > p2_matches_won:
            p1_sets_won += 1
        else:
            p2_sets_won += 1
    score_list.append([p1_matches_won, p2_matches_won])

print(score_list)
