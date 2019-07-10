import pygame
import textwrap
pygame.font.init()


class button():
  """class for simplifying the use of buttons"""
  def __init__(self, real_col, change_col, x, y, w, h, text, text_col=(0,0,0), font_size=(30), wrapping=0, center=True):
    arial = pygame.font.SysFont('Arial', font_size)
    self.real_col = real_col
    self.change_col = change_col
    self.colour = real_col
    self.rect = pygame.Rect(x,y,w,h)
    self.center = center
    self.plain_text = text
    self.pressed = False


    #text wrapping inside the button
    if wrapping:
      self.text = []
      wrapped = textwrap.wrap(text, wrapping)
      for n in wrapped:
          self.text.append(arial.render(n, True, text_col))
    else:
        self.text = [arial.render(text, True, text_col)]


  def draw(self, DISPLAY):
    btn = pygame.Surface((self.rect.width,self.rect.height), pygame.SRCALPHA)
    btn.fill(self.colour)
    DISPLAY.blit(btn, (self.rect.topleft))
    #pygame.draw.rect(DISPLAY, self.colour, self.rect)

    #centering the text in the middle of the button
    if self.center:
        ypos = self.rect.center[1] - (self.text[0].get_height()/2)
    else:
        ypos = self.rect.y + 15
    
    #printing the text in
    for line in self.text:
      DISPLAY.blit(line, (self.rect.center[0] - (line.get_width()/2), ypos))
      ypos += 20
  

  def isOver(self, mouse_pos):
    if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
      return True

    return False 
  

  def update(self, event):
    if event.type == pygame.MOUSEMOTION:
        if self.isOver(pygame.mouse.get_pos()):
            self.colour = self.change_col
        else:
            self.colour = self.real_col
    if event.type == pygame.MOUSEBUTTONDOWN:
        if self.isOver(pygame.mouse.get_pos()):
            self.pressed = True
    