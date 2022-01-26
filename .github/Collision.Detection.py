Pygame Collision Detection Pactice, Aamri Mayfield, Jan 19, 2022, 7:46pm, v0.2

import pygame, sys, random
from pygame.locals import *

# Setup Pygame
pygame.init()
mainClock = pygame.time.Clock ()

# Setup the Pygame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), 0,32)
pygame.display.set_caption('Collision Detection 2022')