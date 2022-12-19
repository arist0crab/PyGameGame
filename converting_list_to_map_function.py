from tile_class import Tile
from random import choice


def convert_list_to_level(map_array, tile_group, player_group):
    """
    :param player_group: level payer group of sprites
    :param tile_group: level tiles group of sprites
    :param map_array: array from whom we get tiles locations
    :return: draw level map on screen

    This function take list of numbers and create tiles basing on this list.

    symbols meanings:
    -2 - stone floor (corridor)
    -1 - empty
    0 - wood boards
    2 - carpet
    3 - stone floor
    """

    for y, line in enumerate(map_array):
        for x, symbol in enumerate(line):
            if symbol == -2:
                Tile('stone floor', (x * Tile.size[0], y * Tile.size[1]), tile_group)
            elif symbol == 0:
                Tile(choice(['wood boards 1', 'wood boards 2']),
                     (x * Tile.size[0] - x * 2, y * Tile.size[1] - y * 18), tile_group)
            # TODO: add more tiles and random choice of them
