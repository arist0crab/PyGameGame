""" Main runfile of the game """

import pygame
from level_class import Level
from enemy_charge import Charge

# region variables, constants, and settings of the game
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)  # making mouse invisible
# size = width, height = 500, 500
# screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 30
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
running = True
# endregion

hero_animations = [
    [
        'static/player_animations/player_anim_right_1.png',
        'static/player_animations/player_anim_right_2.png',
        'static/player_animations/player_anim_right_1.png',
        'static/player_animations/player_anim_right_2.png'
    ],
    [
        'static/player_animations/player_anim_left_1.png',
        'static/player_animations/player_anim_left_2.png',
        'static/player_animations/player_anim_left_1.png',
        'static/player_animations/player_anim_left_2.png'
    ],
    [
        'static/player_animations/player_standing_right_1.png',
        'static/player_animations/player_standing_right_1.png',
        'static/player_animations/player_standing_right_2.png',
        'static/player_animations/player_standing_right_2.png',
    ],
    [
        'static/player_animations/player_standing_left_1.png',
        'static/player_animations/player_standing_left_1.png',
        'static/player_animations/player_standing_left_2.png',
        'static/player_animations/player_standing_left_2.png',
    ]
]

level_1 = Level(screen, hero_animations, 10, FPS, clock)

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
    level_1.draw(screen, (WIDTH, HEIGHT))
    level_1.get_player().health_bar.render()
    level_1.get_player().stamina_bar.render()
    pygame.display.update()
    pygame.display.flip()
