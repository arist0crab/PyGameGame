""" Main runfile of the game """

import pygame
from level_class import Level
from start_screen_function import start_screen
from dungeon_procedural_generation_algorithm import dungeon_generation

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
the_best_score = 0
# endregion


"""Setting enemies, lava and potions stats to make it changeable later to regulate levels difficulty."""
# region start enemies, lava and potions quantity and stats
enemies_quantity = 3  # maximum 3
enemies_health = 10
enemies_damage = 7
enemies_vision = 225

potions_chance = enemies_quantity // 3  # in percents (%)
potions_heal = enemies_damage * 1.5

lava_damage = 0.1
# endregion

hero_animations = [
    [
        'static/player/player_going_right_1.png',
        'static/player/player_going_right_2.png',
        'static/player/player_going_right_1.png',
        'static/player/player_going_right_2.png'
    ],
    [
        'static/player/player_standing_right_1.png',
        'static/player/player_standing_right_1.png',
        'static/player/player_standing_right_2.png',
        'static/player/player_standing_right_2.png'
    ]
]

dungeon_generation()
current_level = Level(
    screen=screen, player_animations=hero_animations, enemies_quantity=enemies_quantity, FPS=FPS, clock=clock,
    enemies_stats={'quantity': enemies_quantity, 'health': enemies_health, 'damage': enemies_damage,
                   'vision': enemies_vision},
    potions_stats={'chance': potions_chance, 'heal': potions_heal}, lava_damage=lava_damage,
    the_best_score=the_best_score
)

"""Main cycle of the game"""
start_screen(screen, clock, FPS)
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
    current_level.draw(screen, (WIDTH, HEIGHT))
    if len(current_level.enemies) == 0:
        if current_level.player.score > the_best_score:
            the_best_score = current_level.player.score if current_level.player.score > 0 else the_best_score

        enemies_quantity = round(enemies_quantity * 1.5) if round(enemies_quantity * 1.5) <= 20 else 20
        enemies_damage = round(enemies_damage * 1.5)
        enemies_vision = round(enemies_vision * 1.15)
        enemies_health = round(enemies_health * 1.5)
        potions_heal = enemies_damage * 1.5 if enemies_damage * 1.5 <= 20 else 20
        potions_chance += 0.5 if potions_heal + 0.5 <= 5 else 5
        lava_damage *= 1.05

        # dungeon_generation()  # TODO: fix this with Alexey

        the_best_score = current_level.player.score if current_level.player.score > the_best_score else the_best_score

        current_level = Level(screen=screen, player_animations=hero_animations, enemies_quantity=enemies_quantity,
                              FPS=FPS, clock=clock,
                              enemies_stats={'quantity': enemies_quantity, 'health': enemies_health,
                                             'damage': enemies_damage, 'vision': enemies_vision},
                              potions_stats={'chance': potions_chance, 'heal': potions_heal},
                              lava_damage=lava_damage, the_best_score=the_best_score)

    current_level.draw(screen, (WIDTH, HEIGHT))
    current_level.get_player().health_bar.render()
    current_level.get_player().stamina_bar.render()
    pygame.display.update()
    pygame.display.flip()
