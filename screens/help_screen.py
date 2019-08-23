import pygame
from button import *

"""Displays the user manual"""

def draw(DISPLAY):
    text = ''
    btn_text_y = 0 #for scrolling purposes.

    with open("screens/guide.txt") as f: #user manual is located in guide.txt
        text = f.read()   

    bg_image = pygame.transform.scale(pygame.image.load("pictures/tennnis.jpg"), (DISPLAY.get_width(),DISPLAY.get_height()))
    back_button = button((255,255,255,100), (255,255, 255,190), (9*DISPLAY.get_width() /10) - 100,     ((9 * DISPLAY.get_height())/10)-(37), 200, 75, "Back",(0,0,0,255)) #back

    while not back_button.pressed:
        pygame.display.update() 
        DISPLAY.blit(bg_image, (0,0)) 
        back_button.draw(DISPLAY)


        text_btn = button((255,255,255,0),(255,255,255,0), 0,btn_text_y,DISPLAY.get_width(),DISPLAY.get_height(), text, (255,255,255), 25, 64, False)
        
        text_btn.draw(DISPLAY)

        for event in pygame.event.get():
            back_button.update(event)
            
            if event.type == pygame.QUIT:
                quit()
                pygame.QUIT
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    if btn_text_y + 7 + (len(text_btn.text) * 30) > DISPLAY.get_height():
                        btn_text_y -= 10

                elif event.button == 4:
                    if btn_text_y < 0:
                        btn_text_y += 10