from tile_class import Tile
from random import choices
from player_class import Player
from enemy_class import Enemy
from heal_potion_class import HealPotion
import pygame


def convert_list_to_level(screen, map_array, tile_group, level_sprites_group, player_animations,
                          main_level_sprite_group, FPS, clock, lava_group, empty_group, potion_group,
                          enemies_group, enemies_stats, potions_stats, lava_damage):
    """
    parameters of function:
    :param lava_damage: lava damage on current level
    :param potions_stats: setting of potions on current level
    :param enemies_stats: settings of enemies on current level
    :param enemies_group: group of enemies
    :param potion_group: group of potions sprites
    :param empty_group: group of 'empty' tiles which will be limit player movement
    :param lava_group: group of lava tiles
    :param clock: game clock
    :param FPS: game FPS
    :param main_level_sprite_group: all sprites group
    :param screen: screen
    :param player_animations: the matrix with pictures of the player
    :param level_sprites_group: group of all level sprites, which is not tiles
    :param tile_group: level tiles group of sprites
    :param map_array: array from whom we get tiles locations
    :return: hero of level and draw level map on screen

    This function take list of numbers and create tiles basing on this list.

    symbols meanings:
    -2 - floor
    -1 - empty
    0 - grass
    2 - enemy
    """

    hero = None  # if we have no player
    for y, line in enumerate(map_array):
        for x, symbol in enumerate(line):
            if symbol == -2:
                if not hero:
                    Tile('floor', (x * Tile.size[0], y * Tile.size[1]), tile_group)

                    hero = Player(
                        screen,
                        (x * Tile.size[0] + Tile.size[0] / 2 - 5.5, y * Tile.size[1] + Tile.size[1] / 2),
                        10, 100, player_animations, tile_group, FPS, clock, lava_group, empty_group, potion_group,
                        enemies_group, lava_damage, main_level_sprite_group,
                        level_sprites_group
                    )
                else:
                    if choices([1, 0], weights=[potions_stats['chance'], 100 - potions_stats['chance']])[0]:
                        Tile('floor', (x * Tile.size[0], y * Tile.size[1]), tile_group)

                        """Args for potion class:
                        cords, heal, *groups"""
                        HealPotion((x * Tile.size[0] + Tile.size[0] // 2, y * Tile.size[1] + Tile.size[1] // 2),
                                   potions_stats['heal'], level_sprites_group, potion_group)
                    else:
                        Tile('floor', (x * Tile.size[0], y * Tile.size[1]), tile_group)
            elif symbol == 0:
                tile = choices(['grass_1', 'grass_2', 'grass_3', 'lava'], k=1, weights=[30, 30, 30, 10])[0]
                if tile == 'lava':
                    Tile(tile, (x * Tile.size[0], y * Tile.size[1]), tile_group, lava_group)
                else:
                    Tile(tile, (x * Tile.size[0], y * Tile.size[1]), tile_group)
            elif symbol == 2:
                Tile(choices(['grass_1', 'grass_2', 'grass_3'], k=1, weights=[30, 30, 30])[0],
                     (x * Tile.size[0], y * Tile.size[1]), tile_group)

                """Args for enemy class: 
                size, cords, stance_anim, damage_pic, hp, vision, damage, main_level_sprite_group, *groups"""
                Enemy((85, 85), (x * Tile.size[0], y * Tile.size[1]),
                      ['static/enemies/mushroom_1.png', 'static/enemies/mushroom_2.png'],
                      'static/enemies/mushroom_angry.png',
                      enemies_stats['health'], enemies_stats['vision'], enemies_stats['damage'],
                      main_level_sprite_group, level_sprites_group, enemies_group)

            # region creating lava tiles
            '''Checking if it is any need to create lava tile.'''
            if symbol == -1 and x > 0 and (line[x - 1] in [-2, 0, 2]):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group, lava_group)
                continue
            if symbol == -1 and x < len(line) - 1 and (line[x + 1] in [-2, 0, 2]):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group, lava_group)
                continue
            if symbol == -1 and y > 0 and (map_array[y - 1][x] in [-2, 0, 2]):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group, lava_group)
                continue
            if symbol == -1 and y < len(map_array) - 1 and (map_array[y + 1][x] in [-2, 0, 2]):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group, lava_group)
                continue
            if symbol == -1 and (x > 0 and y > 0) and (map_array[y - 1][x - 1] in [-2, 0, 2]):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group, lava_group)
                continue
            if symbol == -1 and (x < len(line) - 1 and y > 0) and (map_array[y - 1][x + 1] in [-2, 0, 2]):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group, lava_group)
                continue
            if symbol == -1 and (x > 0 and y < len(map_array) - 1) and (map_array[y + 1][x - 1] in [-2, 0, 2]):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group, lava_group)
                continue
            if symbol == -1 and (x < len(line) - 1 and y < len(map_array) - 1) and \
                    (map_array[y + 1][x + 1] in [-2, 0, 2]):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group, lava_group)
                continue
            elif symbol == -1:
                Tile('empty', (x * Tile.size[0], y * Tile.size[1]), tile_group, empty_group)
            # endregion

    return hero