import pygame
from button import *

#FONTS
large_font = pygame.font.SysFont('Arial', 40)
medium_font = pygame.font.SysFont('Arial', 30)
small_font = pygame.font.SysFont('Arial', 20)
#--------------------------------------------------

def draw(DISPLAY):
    reslist = ["1280x720","1366x768","1920x1080"]

    #text surfaces.
    settings_text = large_font.render("SETTINGS ", True, (100,100,100))
    settings_restext = medium_font.render("Resolution:", True, (0,0,0))
    settings_changes_text = small_font.render("Changes take effect after restarting", True, (100,100,100))

    #check which resolution the display is currently set to:
    for c,n in enumerate(reslist):
        if (str(DISPLAY.get_width()) +"x"+str(DISPLAY.get_height())) == n:
            res_numbers = reslist[c]
            break   

    settings_res_numbers = small_font.render(res_numbers, True, (0,0,0) )

    #BUTTONS
    exit_btn = button([200,200,200], (190,0, 230), (8*DISPLAY.get_width()/9) - 100, (8 * DISPLAY.get_height()/9) - 85, 200, 75, "Save & Exit") #obj 0
    cancel_btn = button([200,200,200], (190,0, 230), (8*DISPLAY.get_width()/9) - 100, (8 * DISPLAY.get_height()/9) - 165, 200, 75, "Cancel")

    left_btn = button([200,200,200], (190,0, 230), (1*DISPLAY.get_width()/2) - 125, (1 * DISPLAY.get_height()/4) - 25, 50, 50, "<") 
    right_btn = button([200,200,200], (190,0, 230), (1*DISPLAY.get_width()/2) + 75, (1 * DISPLAY.get_height()/4) - 25, 50, 50, ">") 
    
    while not exit_btn.pressed and not cancel_btn.pressed:
        pygame.display.update()
        DISPLAY.fill((255,255,255))
        #draw all the buttons
        exit_btn.draw(DISPLAY)
        left_btn.draw(DISPLAY)
        right_btn.draw(DISPLAY)
        cancel_btn.draw(DISPLAY)

        #blit all the text surfaces onto the screen:
        DISPLAY.blit(settings_text, (int((DISPLAY.get_width()/2) - (settings_text.get_width()/2)), int((DISPLAY.get_height()*1/9) - (settings_text.get_height()/2))))
        DISPLAY.blit(settings_restext, (int((DISPLAY.get_width()/4) - (settings_restext.get_width()/2)), int((DISPLAY.get_height()*1/4) - (settings_restext.get_height()/2))))
        DISPLAY.blit(settings_changes_text, (int((DISPLAY.get_width()/2) - (settings_changes_text.get_width()/2)), int((DISPLAY.get_height()*3/4) - (settings_changes_text.get_height()/2))))
        DISPLAY.blit(settings_res_numbers, (int((DISPLAY.get_width()/2) - (settings_res_numbers.get_width()/2)), int((DISPLAY.get_height()*1/4) - (settings_res_numbers.get_height()/2))))
        for event in pygame.event.get():
            exit_btn.update(event)
            left_btn.update(event)
            right_btn.update(event)
            cancel_btn.update(event)
        
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()
        
        if left_btn.pressed: #resolution switcher
            if c-1 >= 0:
                res_numbers = reslist[c-1]
                c -=1
                settings_res_numbers = small_font.render(res_numbers, True, (0,0,0) )
                
                
            left_btn.pressed = False

        if right_btn.pressed: #resolution switcher
            if c+1 < len(reslist):
                res_numbers = reslist[c+1]
                c +=1
                settings_res_numbers = small_font.render(res_numbers, True, (0,0,0) )
                
                
            right_btn.pressed = False

    if cancel_btn.pressed:
        return "cancel"
    else:
        with open("settings.txt", "w") as f:
            f.write("resolution"+","+reslist[c].split("x")[0]+","+reslist[c].split("x")[1])
        return "exit"
    