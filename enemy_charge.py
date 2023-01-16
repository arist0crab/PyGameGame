import pygame


def movement_calculation(start_pos, end_pos, bullet_speed):
    distance = ((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5
    time = distance / bullet_speed  # seconds charge need to get to the target
    return (end_pos[0] - start_pos[0]) / time, (end_pos[1] - start_pos[1]) / time


class Charge(pygame.sprite.Sprite):

    size = (40, 40)

    """Creating class of attacking charge."""
    def __init__(self, picture, damage, start_pos, end_pos, speed, *groups):
        super().__init__(*groups)

        self.image = pygame.transform.scale(pygame.image.load(picture), Charge.size)
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.mask = pygame.mask.from_surface(self.image)

        self.damage = damage
        self.speed_x, self.speed_y = movement_calculation(start_pos, end_pos, speed)
        self.cords = start_pos

    def move(self, target):
        if pygame.sprite.collide_mask(self, target):
            target.get_damage(self.damage)
            self.kill()
        else:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        # TODO: make living time for charge

    def update(self, *args):
        self.move(args[0])
