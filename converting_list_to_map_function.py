from tile_class import Tile
from random import choices
from player_class import Player
# from entitys_classes.base_enemy_class import BaseEnemy
from enemy_class import Enemy


def convert_list_to_level(screen, map_array, tile_group, level_sprites_group, player_animations,
                          main_level_sprite_group):
    """
    parameters of function:
    :param main_level_sprite_group: all sprites group
    :param screen: screen
    :param player_animations:
    :param level_sprites_group: group of all level sprites, which is not tiles
    :param tile_group: level tiles group of sprites
    :param map_array: array from whom we get tiles locations
    :return: hero of level and draw level map on screen

    This function take list of numbers and create tiles basing on this list.

    symbols meanings:
    -2 - floor
    -1 - empty
    0 - grass
    1 - player
    2 - enemy
    """

    hero = None  # if we have no player
    for y, line in enumerate(map_array):
        for x, symbol in enumerate(line):
            if symbol == -2:
                Tile('floor', (x * Tile.size[0], y * Tile.size[1]), tile_group)
            elif symbol == 0:
                Tile(choices(['grass', 'lava'], k=1, weights=[90, 10])[0],
                     (x * Tile.size[0], y * Tile.size[1]), tile_group)
                # TODO: add more tiles and random choice of them
            elif symbol == 1:
                hero = Player(screen, (50, 70), (x * Tile.size[0], y * Tile.size[1]), 10, 100,
                              player_animations, tile_group, level_sprites_group)
                Tile('grass', (x * Tile.size[0], y * Tile.size[1]), tile_group)
            elif symbol == 2:
                Tile('grass', (x * Tile.size[0], y * Tile.size[1]), tile_group)
                Enemy((85, 85), (x * Tile.size[0], y * Tile.size[1]), ['static/enemy_1.png', 'static/enemy_2.png'],
                      100, 300, 20, main_level_sprite_group, level_sprites_group)

            # region creating lava tiles
            '''Checking if it is any need to create lava tile.'''
            if symbol == -1 and x > 0 and (line[x - 1] == -2 or line[x - 1] == 0):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group)
                continue
            if symbol == -1 and x < len(line) - 1 and (line[x + 1] == -2 or line[x + 1] == 0):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group)
                continue
            if symbol == -1 and y > 0 and (map_array[y - 1][x] == -2 or map_array[y - 1][x] == 0):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group)
                continue
            if symbol == -1 and y < len(map_array) - 1 and (map_array[y + 1][x] == -2 or map_array[y + 1][x] == 0):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group)
                continue
            if symbol == -1 and (x > 0 and y > 0) and (map_array[y - 1][x - 1] == -2 or map_array[y - 1][x - 1] == 0):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group)
                continue
            if symbol == -1 and (x < len(line) - 1 and y > 0) and \
                    (map_array[y - 1][x + 1] == -2 or map_array[y - 1][x + 1] == 0):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group)
                continue
            if symbol == -1 and (x > 0 and y < len(map_array) - 1) and \
                    (map_array[y + 1][x - 1] == -2 or map_array[y + 1][x - 1] == 0):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group)
                continue
            if symbol == -1 and (x < len(line) - 1 and y < len(map_array) - 1) and \
                    (map_array[y + 1][x + 1] == -2 or map_array[y + 1][x + 1] == 0):
                Tile('lava', (x * Tile.size[0], y * Tile.size[1]), tile_group)
                continue
            # endregion

    return hero
