import pygame


class PlayerCharge(pygame.sprite.Sprite):

    size = (45, 35)

    """Creating class of player attacking charge."""

    def __init__(self, start_pos, delta_cords, enemies_group, player, *groups):
        super().__init__(*groups)

        self.image = pygame.transform.scale(pygame.image.load('static/player_charge.png'), PlayerCharge.size)
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.mask = pygame.mask.from_surface(self.image)

        self.delta_cords = delta_cords
        self.enemies_group = enemies_group

        self.counter = round(3 / 0.033)

        self.player = player

    def move(self):
        for enemy in self.enemies_group:
            if pygame.sprite.collide_mask(self, enemy):
                enemy.get_damage(10, self.player)
                self.kill()
                break
        self.rect.x += self.delta_cords[0]
        self.rect.y += self.delta_cords[1]

    def update(self, *args):
        self.counter -= 1
        if self.counter <= 0:
            self.kill()
        self.move()
