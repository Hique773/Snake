from email.iterators import body_line_iterator
from turtle import Screen
from webbrowser import get
import pygame
from pygame.locals import *

WINDOW_SIZE = (600, 600)
PIXEL_SIZE = 10


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('snake')

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill((255, 255, 255))

apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_surface.fill((255, 0, 0))

for pos in snake_pos:
    screen.blit(snake_surface, pos)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()


    



