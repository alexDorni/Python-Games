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
    screen = pygame.display.set_mode([400, 500])

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


def spawn_food():
    return random.randint(0, 19), random.randint(0, 19)


def draw_text(surf, text, size, x, y):
    global BLACK
    font = pygame.font.Font(pygame.font.match_font("arial"), size)
    text_surface = font.render(text,
                               True,
                               BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def run_game():
    global rect_obj_list, screen, RED, GREEN

    rect_len = len(rect_obj_list)
    middle_screen = rect_len // 2
    x_coord_rect, y_coord_rect = middle_screen, middle_screen

    snake_step = 1

    # Spawn the first food
    x_coord_food, y_coord_food = spawn_food()

    score = 0

    while 1:
        # TODO Collision with the margin equals END GAME

        # Draw on the screen the food
        rect_obj_list[x_coord_food][y_coord_food] = pygame.draw.rect(screen,
                                                                     GREEN,
                                                                     rect_obj_list[x_coord_food][y_coord_food])

        draw_text(screen, "Score: 0 si atat daca nu faceti ceva", 20, 200, 450)
        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            break

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                screen.fill(WHITE)
                y_coord_rect -= snake_step

                # TODO Check if snake eats food and increment the score
                rect_obj_list[x_coord_rect][y_coord_rect] = pygame.draw.rect(screen,
                                                                             RED,
                                                                             rect_obj_list[x_coord_rect][y_coord_rect],
                                                                             )
            if event.key == pygame.K_d:
                screen.fill(WHITE)
                y_coord_rect += snake_step

                # TODO Check if snake eats food and increment the score
                rect_obj_list[x_coord_rect][y_coord_rect] = pygame.draw.rect(screen,
                                                                             RED,
                                                                             rect_obj_list[x_coord_rect][y_coord_rect],
                                                                             )
            if event.key == pygame.K_w:
                screen.fill(WHITE)
                x_coord_rect -= snake_step

                # TODO Check if snake eats food and increment the score
                rect_obj_list[x_coord_rect][y_coord_rect] = pygame.draw.rect(screen,
                                                                             RED,
                                                                             rect_obj_list[x_coord_rect][y_coord_rect],
                                                                             )
            if event.key == pygame.K_s:
                screen.fill(WHITE)
                x_coord_rect += snake_step

                # TODO Check if snake eats food and increment the score
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
