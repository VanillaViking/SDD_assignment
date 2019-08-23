#!/usr/bin/env python 
import sys
import pygame

sys.path.append("screens/") #all of the different screens here
sys.path.append("interactables/") #Classes for buttons, sliders, text input etc here
import details_screen
import tennis_startscreen
import options_screen
import os
import scorescreen
import win_screen
import help_screen

resolution = None
pygame.init()
pygame.mixer.init()
def restart(): #restarts the entire program
    if sys.platform == "win32": #windows 
        os.execl(sys.executable, sys.executable, *sys.argv)
    else: #linux & macOS
        os.execv(__file__, sys.argv)

#Get the default settings from the text file.
for line in open("settings.txt"):
    if "resolution" in line:
        line = line.strip().split(",")
        try:
            resolution = (int(line[1]),int(line[2]))
        except:
            DISPLAY = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 

    if "volume" in line:
        line = line.strip().split(",")
        volume = float(line[1])



#MUSIC
bg_music = pygame.mixer.music.load("audio/bensound-inspire.mp3")
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play()
if resolution:
    DISPLAY = pygame.display.set_mode(resolution)

#----------------------------------------------------

#help_screen.draw(DISPLAY)

while True: #loops until player hits "start" in first screen or "save and exit" in options screen.
    start_screen_command = tennis_startscreen.start_loop(DISPLAY) 
    if start_screen_command == "start": #go to details screen
        details = details_screen.draw(DISPLAY)
        if details != "back":
            player1_name, player2_name, sets = details
            break
    elif start_screen_command == "opts": #go to options screen
        if options_screen.draw(DISPLAY, volume) == "exit":
            pygame.QUIT
            restart() #restart so that any changes come into effect
            quit()
    elif start_screen_command == "help": #bring up user manual
        help_screen.draw(DISPLAY)
        

def check_lead(p1_matches, p2_matches): #checking if a player is leading by to in order to win the set
    if p1_matches - p2_matches >= 2 or p2_matches - p1_matches >= 2:
        return True
    else:
        return False

p1_sets_won = 0
p2_sets_won = 0

score_list = []

for n in range(sets): #calculates the score
    
    p1_matches_won = 0
    p2_matches_won = 0
    while p1_matches_won < 6 and p2_matches_won < 6 or not check_lead(p1_matches_won, p2_matches_won):      #loops until one of the players have won over 6 matches AND have a 2 point lead. 
        if scorescreen.start_loop(DISPLAY, player1_name, player2_name, p1_matches_won, p2_matches_won, p1_sets_won, p2_sets_won, sets, score_list) == "p1":
            p1_matches_won += 1
        else:
            p2_matches_won += 1
    else:
        if p1_matches_won > p2_matches_won:
            p1_sets_won += 1
        else:
            p2_sets_won += 1
    score_list.append([p1_matches_won, p2_matches_won]) #adds the score to the total
    
#if scorescreen.start_loop(DISPLAY) == "end_game":

if p1_sets_won > p2_sets_won: #checks who the winner is
    win_screen.win_loop(DISPLAY, "p1", player1_name, player2_name, sets, score_list)
elif p2_sets_won > p1_sets_won:
    win_screen.win_loop(DISPLAY, "p2", player1_name, player2_name, sets, score_list)
    

