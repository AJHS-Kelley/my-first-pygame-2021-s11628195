Pygame Collision Detection Pactice, Aamri Mayfield, Jan 19, 2022, 6:32pm, v0.6

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

# Run the game loop
While True:
     # Clock for events
     for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
            if event.type == KEYDOWN
                # Change the keyboard variables
                if event.key == K_Left or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == k_Right or event.key == K_d:
                    moveRight = True 
                if event.key == K_UP or event.key ==K_w:
                    moveUP = False
                    moveDOWN = True
                if event.key
                if event.type == KEYUP
                    if event.key == K_ESCAPE:
                        pygame.quuit()
                        sys.exit()
                     # Check to see if the player has stopped moving.
                    if event.key == K_Left or event.key == K_a:
                         moveLeft = False
                    if event.key == K_RIGHT or event.key == K_d:
                         moveLight = False
                    if event.key == K_UP or event.key ==K_w:
                        moveUp = False
                    if event.key == K_DOWN or event.key == K_s:                    
        
