import pygame
import numpy as np
import random
from math import pi

pygame.init()

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)

screen = pygame.display.set_mode([600, 600])

pygame.display.set_caption("Snake")

done = False
clock = pygame.time.Clock()
grid = [[1] * 30 for i in range(30)]

screen.fill(WHITE)
lista = []
list_row_rect = []
zz = 0
x, y = 0, 0

# def xx(COLOR):
#     global x, y
#     return pygame.draw.rect(screen, COLOR, [x, y, 20, 20], 1)

for i in grid:
    for j in i:
        xx = lambda COLOR: lambda COLOR: pygame.draw.rect(screen, COLOR, [x, y, 20, 20], 1)
        list_row_rect.append(xx(RED))
        x = x + 20
    lista.append(list_row_rect)
    x = 0
    y = y + 20
# print()
x, y = 0, 0
step = 20

while 1:
    ok1 = 1

    # for event in pygame.event.get():  # User did something
    #     if event.type == pygame.QUIT:  # If user clicked close
    #         done = True  # Flag that we are done so we exit this loop

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    # if (event.type == pygame.K_TAB):
    #     pygame.draw.rect(screen, BLUE, [x, y, 20, 20])
    #     y += 20
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            x -= step
            # pygame.draw.rect(screen, BLUE, [x, y, 20, 20])
            lista[x][y](BLUE)
        if event.key == pygame.K_d:
            x += step
            lista[x][y](BLUE)
            # pygame.draw.rect(screen, BLUE, [x, y, 20, 20])
        if event.key == pygame.K_w:
            y -= step
            lista[x][y](BLUE)
            # pygame.draw.rect(screen, BLUE, [x, y, 20, 20])
        if event.key == pygame.K_s:
            y += step
            lista[x][y](BLUE)
            # pygame.draw.rect(screen, BLUE, [x, y, 20, 20])
    # pressed = pygame.key.get_pressed()d
    # if pressed[pygame.K_w] and ok1:
    #     print("w is pressed")
    #     pygame.draw.rect(screen, BLUE, [x, y, 20, 20])
    #     y += 20
    #     ok1 = 0
    #
    # if pressed[pygame.K_s]:
    #     print("s is pressed")

    pygame.display.flip()

# Be IDLE friendly
pygame.quit()

# if __name__ == '__main__':
#
