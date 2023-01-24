import pygame


class Tile(pygame.sprite.Sprite):

    """Creating Tile class."""

    size = (85, 85)
    images = {
        'grass_1': 'static/tiles/pink_grass_1.png',
        'grass_2': 'static/tiles/pink_grass_2.png',
        'grass_3': 'static/tiles/pink_grass_3.png',
        'floor': 'static/tiles/floor.png',
        'lava': 'static/tiles/laser.png',
        'empty': 'static/tiles/empty.png'
    }
    for image_name in images.keys():
        images[image_name] = pygame.transform.scale(pygame.image.load(images[image_name]), size)

    def __init__(self, tile_name, tile_position, *group):
        super().__init__(*group)
        self.image = Tile.images[tile_name]
        self.tile_name = tile_name
        self.rect = self.image.get_rect().move(tile_position[0], tile_position[1])
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args):
        pass
