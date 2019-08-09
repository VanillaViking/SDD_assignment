import pygame

class slider():
    def __init__(self, DISPLAY, colour, rect):
        self.display = DISPLAY
        self.colour = colour
        self.rect = pygame.Rect(rect)
        self.range = self.rect.width
        self.border_rect = pygame.Rect(self.rect.x - 1, self.rect.y - 1, self.rect.width + 1, self.rect.height + 1)        
        self.active = False
 
    def draw(self):
        pygame.draw.rect(self.display, self.colour, self.border_rect, 1) 
        pygame.draw.rect(self.display,self.colour, self.rect)
    def update(self, event, mouse_pos):
        if self.border_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.active = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.active = False
        if self.active:
            if mouse_pos[0] > self.border_rect.x:
                if mouse_pos[0] < (self.border_rect.x + self.border_rect.width):  
                    self.rect.width = mouse_pos[0] - self.rect.x
                else:
                    self.rect.width = self.range
            else:
                self.rect.width = 0
                

    def get_value(self):
        return int(self.rect.width * 100/self.range) / 100

    def set_value(self, value):
        self.rect.width = int(value*200) 
