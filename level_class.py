import pygame

from converting_list_to_map_function import convert_list_to_level
from dungeon_procedural_generation_algorithm import dungeon_generation, grid
from camera_class import Camera
from random import choices


class Level:
    """
    Creating Level class.
    In __init__ we're initializing sprites tile_group and level_sprites_group.
    """

    def __init__(self, screen, player_animations, enemies_quantity, FPS, clock,
                 enemies_stats, potions_stats, lava_damage, the_best_score):

        """Creating sprite groups of tiles and entities."""
        self.tile_group = pygame.sprite.Group()
        self.level_sprites_group = pygame.sprite.Group()  # tiles aren't included in this group
        self.lava_group = pygame.sprite.Group()
        self.group_of_empty_tiles = pygame.sprite.Group()
        self.potion_group = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        """External variables for enemies, potions and lava stats."""
        self.enemies_stats = enemies_stats
        self.potions_stats = potions_stats
        self.lava_damage = lava_damage

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

        """Adding required quantity of enemies."""
        enemies = 0
        while enemies < enemies_quantity:
            for y, line in enumerate(self.array_map):
                for x, symbol in enumerate(line):
                    if symbol == 0 and enemies < enemies_quantity:
                        choice = choices([0, 2], k=1, weights=[90, 10])[0]
                        if choice == 2:
                            self.array_map[y][x] = 2
                            enemies += 1
                    elif enemies == enemies_quantity:
                        break

        """Player creating."""
        self.player = convert_list_to_level(screen, self.array_map, self.tile_group, self.level_sprites_group,
                                            self.player_animations, self.level_all_sprites_group, FPS, clock,
                                            self.lava_group, self.group_of_empty_tiles, self.potion_group, self.enemies,
                                            self.enemies_stats, self.potions_stats, self.lava_damage, the_best_score)

        """Adding all sprites we have in our main group of sprites."""
        for sprite in self.tile_group.sprites() + self.level_sprites_group.sprites():
            self.level_all_sprites_group.add(sprite)

    def draw(self, surface, screen_size):

        self.level_sprites_group.update(self.player)  # we aren't updating tiles, cuz it's not a must

        self.camera.update(self.player, screen_size)
        for sprite in self.level_all_sprites_group:
            self.camera.apply(sprite)

        self.level_all_sprites_group.draw(surface)

    def get_player(self):
        return self.player
