import pygame

text_large = pygame.font.SysFont('Arial',50)
text_small = pygame.font.SysFont('Arial',20)
text_medium = pygame.font.SysFont('Arial',25)


def msg(gameDisplay, text, font, colour, pos):
    text_surface = font.render(text, True, colour)
    gameDisplay.blit(text_surface, (pos[0] - (text_surface.get_width()/2), pos[1] - (text_surface.get_height()/2))) #position minus half of text size in order to center it.

def draw_score_hist(gameDisplay, p1_name, p2_name, sets, score_list): #Draws a history of the games won by each player
    p1 = text_small.render(p1_name, True, (255,255,255))
    p2 = text_small.render(p2_name, True, (255,255,255))

    x_increment = -25

    #These values are set separately since they need to be used later
    p1_x_val = gameDisplay.get_width()/2 - ((p1.get_width() + 85)/2)
    p1_y_val = gameDisplay.get_height()* 3/4 - 21

    p2_x_val = gameDisplay.get_width()/2 - (p2.get_width() + 85)/2
    p2_y_val = gameDisplay.get_height()* 3/4 + 2

    gameDisplay.blit(p1, ((p1_x_val), p1_y_val))
    gameDisplay.blit(p2, (p2_x_val,p2_y_val))

    if len(p1_name) >= len(p2_name):    #Checks whether p1's name is longer or p2's name is longer and accomodates space for the longer name.
        for n in range(sets+1):
            x_increment += 27
            pygame.draw.line(gameDisplay, (190,190,190), (p1_x_val + p1.get_width() + x_increment, p1_y_val), (p1_x_val + p1.get_width() + x_increment, p2_y_val + p2.get_height()), 2)
            if n <= len(score_list) - 1:
                msg(gameDisplay, str(score_list[n][0]), text_small, (255,255,255), (p1_x_val + p1.get_width() + x_increment + 13, p1_y_val + 10))
                msg(gameDisplay, str(score_list[n][1]), text_small, (255,255,255), (p1_x_val + p1.get_width() + x_increment + 13, p2_y_val + 12))

        pygame.draw.line(gameDisplay, (190,190,190), (p1_x_val, gameDisplay.get_height() * 3/4), (p1_x_val +p1.get_width() + x_increment, gameDisplay.get_height() * 3/4), 2) #horizontal line

    else:
        for n in range(sets+1):
            x_increment += 27
            pygame.draw.line(gameDisplay, (190,190,190), (p2_x_val + p2.get_width() + x_increment, p1_y_val), (p2_x_val + p2.get_width() + x_increment, p2_y_val + p2.get_height()), 2)
            if n <= len(score_list) - 1:
                msg(gameDisplay, str(score_list[n][0]), text_small, (255,255,255), (p2_x_val + p2.get_width() + x_increment + 13, p1_y_val + 10))
                msg(gameDisplay, str(score_list[n][1]), text_small, (255,255,255), (p2_x_val + p2.get_width() + x_increment + 13, p2_y_val + 12))

        pygame.draw.line(gameDisplay, (190,190,190), (p2_x_val, gameDisplay.get_height() * 3/4), (p2_x_val +p2.get_width() + x_increment, gameDisplay.get_height() * 3/4), 2) #horizontal line

