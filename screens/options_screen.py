import pygame
from button import *
from slider import *
from truefalse import *

#FONTS
large_font = pygame.font.SysFont('Arial', 40)
medium_font = pygame.font.SysFont('Arial', 30)
small_font = pygame.font.SysFont('Arial', 20)
#--------------------------------------------------

def msg(gameDisplay, text, font, colour, pos):
    text_surface = font.render(text, True, colour)
    gameDisplay.blit(text_surface, (pos[0] - (text_surface.get_width()/2), pos[1] - (text_surface.get_height()/2))) #position minus half of text size in order to center it.



def draw(DISPLAY, volume):
    reslist = ["1280x720","1366x768","Fullscreen"]
    #background
    bg_image = pygame.transform.scale(pygame.image.load("pictures/tennnis.jpg"), (DISPLAY.get_width(),DISPLAY.get_height()))


    #text surfaces.
    settings_text = large_font.render("SETTINGS ", True, (200,200,200))
    settings_restext = medium_font.render("Resolution:", True, (255,255,255))
    settings_changes_text = small_font.render("Changes take effect after restarting", True, (200,200,200))
    volume_text = medium_font.render("Volume:", True, (255,255,255))

    #check which resolution the display is currently set to:
    for c,n in enumerate(reslist):
        if (str(DISPLAY.get_width()) +"x"+str(DISPLAY.get_height())) == n:
            res_numbers = reslist[c]
            break   
        else:
            res_numbers = reslist[-1]

    settings_res_numbers = small_font.render(res_numbers, True, (255,255,255) )

    #BUTTONS
    exit_btn = button([255,255,255,100], [255,255, 255,190], (8*DISPLAY.get_width()/9) - 100, (8 * DISPLAY.get_height()/9) - 85, 200, 75, "Save & Restart", (0,0,0), 25) #obj 0
    cancel_btn = button([255,255,255,100], [255,255, 255,190], (8*DISPLAY.get_width()/9) - 100, (8 * DISPLAY.get_height()/9) - 165, 200, 75, "Cancel")

    left_btn = button([255,255,255,100], [255,255, 255,190], (1*DISPLAY.get_width()/2) - 125, (1 * DISPLAY.get_height()/4) - 25, 50, 50, "<") 
    right_btn = button([255,255,255,100], [255,255, 255,190], (1*DISPLAY.get_width()/2) + 75, (1 * DISPLAY.get_height()/4) - 25, 50, 50, ">") 

    #SLIDER
    volume_slider = slider(DISPLAY, (255,255,255), (DISPLAY.get_width()/2 - 125, DISPLAY.get_height()/2 - 10, 200, 20)) 
    volume_slider.set_value(volume)    

    #RADIO
    help_yesno = tf(DISPLAY, DISPLAY.get_width()* 3/4, DISPLAY.get_height() * 3/4, 5, "", (255,255,255)) 

    while not exit_btn.pressed and not cancel_btn.pressed:
        pygame.display.update()
        DISPLAY.blit(bg_image, (0,0))
        #draw all the buttons
        exit_btn.draw(DISPLAY)
        left_btn.draw(DISPLAY)
        right_btn.draw(DISPLAY)
        cancel_btn.draw(DISPLAY)
        volume_slider.draw()

        #blit all the text surfaces onto the screen:
        DISPLAY.blit(settings_text, (int((DISPLAY.get_width()/2) - (settings_text.get_width()/2)), int((DISPLAY.get_height()*1/9) - (settings_text.get_height()/2))))
        DISPLAY.blit(settings_restext, (int((DISPLAY.get_width()/4) - (settings_restext.get_width()/2)), int((DISPLAY.get_height()*1/4) - (settings_restext.get_height()/2))))
        DISPLAY.blit(settings_changes_text, (int((DISPLAY.get_width()/2) - (settings_changes_text.get_width()/2)), int((DISPLAY.get_height()*3/4) - (settings_changes_text.get_height()/2))))
        DISPLAY.blit(settings_res_numbers, (int((DISPLAY.get_width()/2) - (settings_res_numbers.get_width()/2)), int((DISPLAY.get_height()*1/4) - (settings_res_numbers.get_height()/2))))
        DISPLAY.blit(volume_text, (int((DISPLAY.get_width()/4) - (volume_text.get_width()/2)), int((DISPLAY.get_height()*1/2) - (volume_text.get_height()/2))))
        msg(DISPLAY, str(int(volume_slider.get_value() * 100)) + "%", medium_font, (255,255,255), (DISPLAY.get_width()/2 + 125, DISPLAY.get_height()/2))

        for event in pygame.event.get():
            #Updating all objects
            exit_btn.update(event)
            left_btn.update(event)
            right_btn.update(event)
            cancel_btn.update(event)
            volume_slider.update(event, pygame.mouse.get_pos())    
            pygame.mixer.music.set_volume(volume_slider.get_value())            
 
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()
        
        if left_btn.pressed: #resolution switcher
            if c-1 >= 0:
                res_numbers = reslist[c-1]
                c -=1
                settings_res_numbers = small_font.render(res_numbers, True, (255,255,255) )
                
                
            left_btn.pressed = False

        if right_btn.pressed: #resolution switcher
            if c+1 < len(reslist):
                res_numbers = reslist[c+1]
                c +=1
                settings_res_numbers = small_font.render(res_numbers, True, (255,255,255) )
                
                
            right_btn.pressed = False

    if cancel_btn.pressed:
        return "cancel"
    else: #Writes to a txt file so that the changes are not lost after each restart.
        with open("settings.txt", "w") as f:
            try:
                f.write("resolution"+","+reslist[c].split("x")[0]+","+reslist[c].split("x")[1])
                f.close()
            except:
                f.write("resolution,fullscreen")
                f.close()
        with open("settings.txt", "a") as f:
            f.write("\nvolume,"+str(volume_slider.get_value()))
            f.close()
        return "exit"
    
