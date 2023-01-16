import pygame


class Tile(pygame.sprite.Sprite):

    """Creating Tile class."""

    size = (85, 85)
    images = {
        'grass': 'static/tiles/grass.png',
        'floor': 'static/tiles/floor.png',
        'lava': 'static/tiles/lava.png'
    }
    for image_name in images.keys():
        images[image_name] = pygame.transform.scale(pygame.image.load(images[image_name]), size)

    def __init__(self, tile_name, tile_position, *group):
        super().__init__(*group)
        self.image = Tile.images[tile_name]
        self.tile_name = tile_name
        self.rect = self.image.get_rect().move(tile_position[0], tile_position[1])

    def update(self, *args):
        pass
