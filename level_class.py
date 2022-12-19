import pygame
from converting_list_to_map_function import convert_list_to_level
from dungeon_procedural_generation_algorithm import dungeon_generation, grid


class Level:

    """
    Creating Level class.
    In __init__ we're initializing sprites tile_group and player_group.
    """

    # TODO: I think it'll be much better to replace player_group with level_sprites_group, but it's later

    dungeon_generation()

    def __init__(self):
        self.tile_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.array_map = grid
        for row in range(len(self.array_map)):
            self.array_map[row] = [i if i < 0 else 0 for i in self.array_map[row]]

        convert_list_to_level(self.array_map, self.tile_group, self.player_group)

    def draw(self, surface):
        self.tile_group.draw(surface)
        self.player_group.draw(surface)

