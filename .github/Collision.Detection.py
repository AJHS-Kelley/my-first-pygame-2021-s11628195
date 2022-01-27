Pygame Collision Detection Pactice, Aamri Mayfield, Jan 19, 2022, 2:32pm, v0.5

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

# Setup colors.
BLACK - (0, 0, 0)
GREEN - (0, 255, 0)
WHITE - (255, 255, 255)

# Setup the player and food data structures.
foodcounter = 0
NEWFOOD = 40
FOOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods[]

for i in range(20):\
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOOODSIZE), FOOODSIZE, FOOODSIZE))

# Movement Variables
moveleft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6