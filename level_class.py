import pygame
from converting_list_to_map_function import convert_list_to_level
from dungeon_procedural_generation_algorithm import dungeon_generation, grid
from camera_class import Camera


class Level:

    """
    Creating Level class.
    In __init__ we're initializing sprites tile_group and level_sprites_group.
    """

    dungeon_generation()

    def __init__(self, player_animations):
        """Creating sprite groups of tiles and entities."""
        self.tile_group = pygame.sprite.Group()
        self.level_sprites_group = pygame.sprite.Group()  # tiles aren't included in this group

        """
        Here is special group of sprites. It makes player drawing over the tiles and, 
        all in all, any another sprite. Check self._layer = 1 in PLayer class.
        """
        self.level_all_sprites_group = pygame.sprite.LayeredUpdates()

        self.array_map = grid
        self.player_animations = player_animations

        """Creating the camera of the level."""
        self.camera = Camera()

        """Reformatting grid to make it more comfortable to draw tiles."""
        for row in range(len(self.array_map)):
            self.array_map[row] = [i if i < 0 else 0 for i in self.array_map[row]]

        # TODO: you must remove this row and replace it with automatically adding '1' in grid, so we can do player spawn
        self.array_map[10][30] = 1

        """Player creating."""
        self.player = convert_list_to_level(self.array_map, self.tile_group,
                                            self.level_sprites_group, self.player_animations)

        """Adding all sprites we have in our main group of sprites."""
        for sprite in self.tile_group.sprites() + self.level_sprites_group.sprites():
            self.level_all_sprites_group.add(sprite)

    def draw(self, surface, screen_size):
        self.level_sprites_group.update()  # we aren't updating tiles, cuz it's not a must

        self.camera.update(self.player, screen_size)
        for sprite in self.level_all_sprites_group:
            self.camera.apply(sprite)

        self.level_all_sprites_group.draw(surface)
