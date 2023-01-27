""" Main runfile of the game """

import pygame
from menu_class import Menu
from level_class import Level
from dungeon_procedural_generation_algorithm import dungeon_generation

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

FPS = 30
WIDTH, HEIGHT = pygame.display.get_surface().get_size()

TEXT_COLOR = (255, 255, 255)
arialblack_font = pygame.font.SysFont("arialblack", 40)

running = True
current_scene = "MenuScreen"

the_best_score = 0

enemies_quantity = 3
enemies_health = 10
enemies_damage = 7
enemies_vision = 225

potions_chance = enemies_quantity // 3
potions_heal = enemies_damage * 1.5

lava_damage = 0.1

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

main_menu = Menu(screen)

current_level = Level(
    screen=screen, player_animations=hero_animations, enemies_quantity=enemies_quantity, FPS=FPS, clock=clock,
    enemies_stats={'quantity': enemies_quantity, 'health': enemies_health, 'damage': enemies_damage,
                   'vision': enemies_vision},
    potions_stats={'chance': potions_chance, 'heal': potions_heal}, lava_damage=lava_damage,
    the_best_score=the_best_score
)


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


def developers_page():
    draw_text("Это Лёша. Он фуллстекер", arialblack_font, TEXT_COLOR, 25, 25)
    zhabyich = pygame.image.load('static/zhabyich.png')
    screen.blit(zhabyich, (25, 100))
    draw_text("Это Варя. Она тоже фуллстекер", arialblack_font, TEXT_COLOR, 775, 25)
    zhabka = pygame.image.load('static/zhabka.png')
    screen.blit(zhabka, (900, 100))


def about_page():
    draw_text("Добро пожаловать в Самую долбанутую игру в мире!", arialblack_font, TEXT_COLOR, 25, 50)
    draw_text("В нашей игре есть ряд правил. Пожалуйста, соблюдайте их:", arialblack_font, TEXT_COLOR, 25, 100)
    draw_text("1. Попробуйте остаться в живых до самого конца и убить", arialblack_font, TEXT_COLOR, 40, 200)
    draw_text("как можно больше противников", arialblack_font, TEXT_COLOR, 50, 250)
    draw_text("2. Если вы нашли баг, то вас обманывают глаза (честно)", arialblack_font, TEXT_COLOR, 40, 300)
    draw_text("3. Я вас обманул, правил нет. Удачи!)", arialblack_font, TEXT_COLOR, 40, 350)
    player = pygame.transform.scale(pygame.image.load('static/player/player_standing_right_1.png'), (244, 175))
    mushroom = pygame.transform.scale(pygame.image.load('static/enemies/mushroom_1.png'), (134, 127))
    screen.blit(mushroom, ((screen.get_size()[0] - 134) // 2, screen.get_size()[1] - 300))
    screen.blit(mushroom, ((screen.get_size()[0] - 134) // 2 + 100, screen.get_size()[1] - 300))
    screen.blit(mushroom, ((screen.get_size()[0] - 134) // 2 + 200, screen.get_size()[1] - 300))
    screen.blit(mushroom, ((screen.get_size()[0] - 134) // 2 - 100, screen.get_size()[1] - 300))
    screen.blit(mushroom, ((screen.get_size()[0] - 134) // 2 - 200, screen.get_size()[1] - 300))
    screen.blit(player, ((screen.get_size()[0] - 244) // 2, screen.get_size()[1] - 200))
    draw_text("мама...", arialblack_font, TEXT_COLOR, (screen.get_size()[0] + 244) // 2 + 10, screen.get_size()[1] - 75)


def play_cycle():
    global current_level
    global enemies_quantity
    global enemies_health
    global enemies_damage
    global enemies_vision
    global potions_chance
    global potions_heal
    global the_best_score
    global lava_damage

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

        dungeon_generation()

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


def main_cycle():
    global running
    global current_scene

    while running:
        clock.tick(FPS)
        """Handler signals to exit from keyboard"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    if current_scene == "MenuScreen":
                        running = False
                    else:
                        current_scene = "MenuScreen"
        screen.fill('black')
        if current_scene == "MenuScreen":
            menu_context = main_menu.render()
            if menu_context["Start"]:
                current_scene = "GameScreen"
            if menu_context["Developers"]:
                current_scene = "DevelopersScreen"
            if menu_context["About"]:
                current_scene = "AboutScreen"
        elif current_scene == "GameScreen":
            play_cycle()
        elif current_scene == "DevelopersScreen":
            developers_page()
        elif current_scene == "AboutScreen":
            about_page()
        pygame.display.flip()


if __name__ == "__main__":
    main_cycle()
