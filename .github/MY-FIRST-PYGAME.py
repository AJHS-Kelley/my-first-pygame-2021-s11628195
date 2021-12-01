200# My First PyGame, Amari Mayfield, 11/29/21 1:59, v0.8
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
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Fill in the background.
windowSurface.fill(FIREBROWN)

# Draw a polygon on the screen
pygame.draw.polygon(windowSurface, WHITE, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Draw line on the screen.
pygame.draw.line(windowSurface, RED, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, WHITE, (75, 60), (60,75),2)
pygame.draw.line(windowSurface, BLUE, (0, 150), (150, 0), 1)

# Draw a cricle.
pygame.draw.circle(windowSurface, RED, (300, 50), 20,0)

# Draw an ellipse.
pygame.draw.ellipse(windowSurface, WHITE, (300, 250, 40, 80),1)

# Draw the text rectangle.
pygame.draw.rect(windowSurface, BLUE, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Create Pixel Array
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380]=BLUE
del pixArray

# Draw the text onto the surface.
windowSurface.blit(text, textRect)

# Update Pygame Dsipaly
pygame.display.update()

# Run game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()