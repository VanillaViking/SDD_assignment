import pygame
from button import *

"""Displays the user manual"""

def draw(DISPLAY):
    text = ''
    btn_text_y = 0 #for scrolling purposes.
    acc = 0
    
   
    for line in open("screens/guide.txt"):
        text += line   
    print(text)
    bg_image = pygame.transform.scale(pygame.image.load("pictures/tennnis.jpg"), (DISPLAY.get_width(),DISPLAY.get_height()))
    back_button = button([255,255,255,100], [255,255, 255,190], (9*DISPLAY.get_width() /10) - 100,     ((9 * DISPLAY.get_height())/10)-(37), 200, 75, "OK",(0,0,0,255)) #back
    
    while not back_button.pressed:
        pygame.display.update() 
        DISPLAY.blit(bg_image, (0,0)) 
        back_button.draw(DISPLAY)


        text_btn = button((255,255,255,0),(255,255,255,0), 0,btn_text_y,DISPLAY.get_width(),DISPLAY.get_height(), text, (255,255,255), 25, 64, False)
        #print(text_btn.wrapped)     
        text_btn.draw(DISPLAY)
        
        btn_text_y += acc

        # Smooth scrolling
        if acc > 0:
            acc -= (0.1 * abs(acc))
            if btn_text_y > 0:
                acc = 0
        elif acc < 0:
            acc += (0.1 * abs(acc))
            if btn_text_y + 7 + (len(text_btn.text) * 30) < DISPLAY.get_height():
                acc = 0 

        for event in pygame.event.get():
            back_button.update(event)
            
            if event.type == pygame.QUIT:
                quit()
                pygame.QUIT
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5: # SCROLL DOWN
                    if btn_text_y + 7 + (len(text_btn.text) * 30) > DISPLAY.get_height():
                        acc -= 3
                    else:
                        acc = 0
                elif event.button == 4: # SCROLL UP
                    if btn_text_y < 0:
                        acc += 3
                    else:
                        acc = 0
