""" Main runfile of the game """

import pygame
from level_class import Level

# region variables, constants, and settings of the game
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
FPS = 30
running = True
# endregion

level_1 = Level()


"""Main cycle of the game"""
while running:
    clock.tick(FPS)

    """Handler signals to exit from keyboard"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                running = False

    screen.fill('black')
    level_1.draw(screen)

    pygame.display.update()
    pygame.display.flip()
