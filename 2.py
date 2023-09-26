import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 500))

#sky
rect(screen, (100, 255, 255), (0, 0, 700, 500))

#ground
rect(screen, (50, 204, 50), (0, 250, 700, 250))

#house
def plot_house(X,Y,scale):
    rect(screen, (204, 153, 0), (X-90*scale, Y-70*scale, 180*scale, 140*scale))
    rect(screen, (0, 0, 0), (X-90*scale, Y-70*scale, 180*scale, 140*scale),2)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()