import pygame


class HealPotion(pygame.sprite.Sprite):

    image = pygame.transform.scale(pygame.image.load('static/tiles/potion.png'), (30, 50))

    def __init__(self, cords, heal, *groups):
        super().__init__(*groups)
        self.image = HealPotion.image
        self.rect = self.image.get_rect()
        self.rect.center = cords
        self.mask = pygame.mask.from_surface(self.image)

        self.heal = heal
