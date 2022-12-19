import pygame


class Tile(pygame.sprite.Sprite):

    """Creating Tile class."""

    # TODO: now Tile class use "size" of tiles as constant, I think we need to fix it later,
    #  make it more dynamic, you know :)

    size = (50, 50)
    images = {
        'wood boards 1': 'static/tiles/wood boards 1.png',
        'wood boards 2': 'static/tiles/wood boards 2.png',
        'carpet': 'static/tiles/carpet.png',
        'stone floor': 'static/tiles/stone floor.png'
    }
    for image_name in images.keys():
        images[image_name] = pygame.transform.scale(pygame.image.load(images[image_name]), size)

    def __init__(self, tile_name, tile_position, *group):
        super().__init__(*group)
        self.image = Tile.images[tile_name]
        self.tile_name = tile_name
        self.rect = self.image.get_rect().move(tile_position[0], tile_position[1])


