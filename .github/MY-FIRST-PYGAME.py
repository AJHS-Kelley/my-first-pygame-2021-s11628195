200# My First PyGame, Amari Mayfield, 11/29/21 1:59, v0.4
import pygame, sys
from pygame.locals import *


# Start PyGame
pygame.init()

# Setup our Window. l
windowSurface = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Hello, world')

# Setup Colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FIREBROWN = (160, 82, 45)

# Setup font.

basicFont = pygame.font.SysFont(None, 48)
# Setup Text.
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centrerx = windowSurface.get_rect().centerx
textRect.centrerx = windowSurface.get_rect().centerx

# Fill in the background.
windowSurface.fill(FIREBROWN)

# Draw a polygon on the screen
pygame.draw.polygon(windowSurface, FIREBROWN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Draw line on the screen.
pygame.draw.polygon(windowSurface, RED, (60,60), (120, 60), 4)
pygame.draw.polygon(windowSurface, WHITE, (75, 60), (60,75),2)
pygame.draw.polygon(windowSurface, BLUE, (0, 150), (150, 0), 1)