# My First PyGame, Amari Mayfield, 11/29/21 1:59, v0.3

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

# Setup font.
basicFont = pygame.font.SysFont(None, 48)

# Setup Text.
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centrerx = windowSurface.get_rect().centerx
textRect.centrerx = windowSurface.get_rect().centerx