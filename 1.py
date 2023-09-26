import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill((255,255,255))

circle(screen, (225, 255, 0), (300, 300), 170)
circle(screen, (0, 0, 0), (300, 300), 170,1)

rect(screen, (0, 0, 0), (200, 360, 190, 35))

circle(screen, (255, 0, 0), (220, 250), 27)
circle(screen, (0, 0, 0), (220, 250), 14)
circle(screen, (0, 0, 0), (220, 250), 27,1)

circle(screen, (255, 0, 0), (360, 250), 20)
circle(screen, (0, 0, 0), (360, 250), 9)
circle(screen, (0, 0, 0), (360, 250), 20,1)

line(screen, (0, 0, 0), [330, 240],[400, 200], 30)
line(screen, (0, 0, 0), [150, 170],[260, 240], 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
