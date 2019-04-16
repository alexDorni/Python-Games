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

for i in grid:
    for j in i:
        xx = pygame.draw.rect(screen, BLUE, [y, x, 20, 20], 1)
        list_row_rect.append(xx)
        y += 20
    list_row_rect = []
    lista.append(list_row_rect)
    x += 20
    y = 0

# TODO with functions

len_lista = lista.__len__() - 1
middle_screen = len_lista // 2

x, y = middle_screen, middle_screen
step = 1

while 1:
    ok1 = 1

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    if event.type == pygame.KEYDOWN:
        print(x, y)
        if (x == len_lista or y == len_lista) or (x < 0 or y < 0):
            print("sfarsit")
            # TODO rise exception

        if event.key == pygame.K_a:
            y -= step
            lista[x][y] = pygame.draw.rect(screen, RED, lista[x][y])
            print(x, y)
        if event.key == pygame.K_d:
            y += step
            lista[x][y] = pygame.draw.rect(screen, RED, lista[x][y])
        if event.key == pygame.K_w:
            x -= step
            lista[x][y] = pygame.draw.rect(screen, RED, lista[x][y])
        if event.key == pygame.K_s:
            x += step
            lista[x][y] = pygame.draw.rect(screen, RED, lista[x][y])

    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
