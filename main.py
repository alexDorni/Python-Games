import pygame
import random


BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)

rect_obj_list = []
screen = None


def create_screen(color=WHITE):
    global rect_obj_list, screen
    screen = pygame.display.set_mode([400, 400])

    # Make the interface white
    screen.fill(WHITE)

    # Make a matrix with 20 x 20 of zeros
    grid = [[0] * 20 for _ in range(20)]

    rect_row_list = []

    x_coord_pixel, y_coord_pixel = 0, 0

    # Create a matrix with rect with dimension 20, 20 pixels
    for row in grid:
        for _ in row:
            rectang = pygame.draw.rect(screen,
                                       color,
                                       [y_coord_pixel, x_coord_pixel, 20, 20],
                                       )
            rect_row_list.append(rectang)

            # Increment with 20 pixels on the line
            y_coord_pixel += 20
        rect_row_list = []
        rect_obj_list.append(rect_row_list)

        # Increment with 20 pixels on column
        x_coord_pixel += 20

        y_coord_pixel = 0


def run_game():
    global rect_obj_list, screen, RED, BLUE, WHITE

    rect_len = len(rect_obj_list)
    middle_screen = rect_len // 2
    x_coord_rect, y_coord_rect = middle_screen, middle_screen

    snake_step = 1

    while 1:

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        if event.type == pygame.KEYDOWN:
            # TODO Collision with the margin equals END GAME

            if event.key == pygame.K_a:
                screen.fill(WHITE)
                y_coord_rect -= snake_step
                rect_obj_list[x_coord_rect][y_coord_rect] = pygame.draw.rect(screen,
                                                                             RED,
                                                                             rect_obj_list[x_coord_rect][y_coord_rect],
                                                                             )
            if event.key == pygame.K_d:
                screen.fill(WHITE)
                y_coord_rect += snake_step
                rect_obj_list[x_coord_rect][y_coord_rect] = pygame.draw.rect(screen,
                                                                             RED,
                                                                             rect_obj_list[x_coord_rect][y_coord_rect],
                                                                             )
            if event.key == pygame.K_w:
                screen.fill(WHITE)
                x_coord_rect -= snake_step
                rect_obj_list[x_coord_rect][y_coord_rect] = pygame.draw.rect(screen,
                                                                             RED,
                                                                             rect_obj_list[x_coord_rect][y_coord_rect],
                                                                             )
            if event.key == pygame.K_s:
                screen.fill(WHITE)
                x_coord_rect += snake_step
                rect_obj_list[x_coord_rect][y_coord_rect] = pygame.draw.rect(screen,
                                                                             RED,
                                                                             rect_obj_list[x_coord_rect][y_coord_rect],
                                                                             )

        pygame.display.flip()

    pygame.quit()


def main():
    # Initialize game engine
    pygame.init()
    pygame.display.set_caption("Snake Game")

    create_screen()

    run_game()


if __name__ == '__main__':
    main()
