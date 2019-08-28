import pygame
import time

pygame.font.init()
FONT = pygame.font.SysFont('Arial', 32)

class tf():
    '''class for true/false buttons'''
    def __init__(self, DISPLAY, x, y, radius, text, col):
        self.x = x
        self.y = y
        self.display = DISPLAY
        self.active = False
        self.col = col
        self.real_col = self.col
        self.change_col = (190,0, 230)
        self.text = text = FONT.render(text, True, (255,255,255))
        self.radius = radius
        self.temp_radius = 0
        self.coloured = False
        self.clicked = False

    def draw(self, anim_check):
        self.display.blit(self.text, (self.x - self.text.get_width()-30, self.y - (self.radius * 2)))
        if self.active:
            if anim_check:
                if not self.coloured:
                    #for f in range(self.radius + 1):
                    if self.temp_radius < self.radius:
                        pygame.draw.circle(self.display, (self.col), (int(self.x),int(self.y)), self.radius, 1)
                        pygame.draw.circle(self.display, (190,0,230), (int(self.x),int(self.y)), int(self.temp_radius))
                        self.temp_radius += 0.9
                    else:
                        self.coloured = True
                        pygame.draw.circle(self.display, (190,0,230), (int(self.x),int(self.y)), int(self.radius))
                else:
                    pygame.draw.circle(self.display, (190,0,230), (int(self.x),int(self.y)), int(self.temp_radius))
            else:
                pygame.draw.circle(self.display, (190,0,230), (int(self.x),int(self.y)), int(self.radius))
                
        else:
            if anim_check:
                if self.coloured:
                    #for f in range(self.radius + 1,0,-1):
                    if self.temp_radius > 0:
                        pygame.draw.circle(self.display, (190,0, 230), (int(self.x),int(self.y)), int(self.temp_radius))
                        self.temp_radius -= 0.9
                    else:
                        self.coloured = False
                    
            pygame.draw.circle(self.display, (self.col), (int(self.x),int(self.y)), self.radius, 1)
  
    def activate(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (int(event.pos[0] - self.x))**2 + (int(event.pos[1] - self.y))**2 <= self.radius**2: # check if mouse is within the area of the button
                self.active = not self.active
                self.clicked = True
            else:
                self.clicked = False

        
