import pygame
from tile_class import Tile
from enemy_charge import EnemyCharge
from random import choice


def distance_between_enemy_and_target(first, second):
    return ((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) ** 0.5


class Enemy(pygame.sprite.Sprite):
    """Realizing Enemy class."""

    def __init__(self, size, cords, stance_anim, damage_pic, hp, vision, damage, main_level_sprite_group, *groups):
        super().__init__(*groups)

        flip = choice([True, False])
        self.current_anim = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(pic), size), flip, False)
                             for pic in stance_anim]
        self.damage_pic = pygame.transform.flip(pygame.transform.scale(pygame.image.load(damage_pic), (85, 85)),
                                                flip, False)
        self.max_anim_count = 15
        self.hp = hp
        self.vision = vision  # radius of zone where enemy can see player
        self.damage = damage
        self.attacking_period = 50
        self.attacking_counter = 0
        self.groups = groups
        self.mlsg = main_level_sprite_group

        # region start variables
        self.anim_count = 0
        self.image = self.current_anim[0]
        self.rect = self.image.get_rect()
        self.cords = cords
        self.rect.center = (cords[0] + Tile.size[0] // 2, cords[1] + Tile.size[1] // 2)
        self.attacking = False
        # endregion

    def is_alive(self):
        return self.hp > 0

    def movement(self, target):
        if distance_between_enemy_and_target(self.rect.center, target.rect.center) <= self.vision:
            self.attacking = True
        else:
            self.attacking = False

    def moving(self, target):
        self.movement(target)

        self.anim_count += 1
        if self.anim_count >= len(self.current_anim) * self.max_anim_count:
            self.anim_count = 0
        self.image = self.current_anim[self.anim_count // self.max_anim_count]

        if not self.attacking:
            pass
        else:
            if self.attacking_counter == 0:
                EnemyCharge('static/enemies/enemy_charge.png', 10, self.rect.center, target.rect.center, 10, self.groups[0], self.mlsg)
            self.attacking_counter += 1
            if self.attacking_counter > self.attacking_period:
                self.attacking_counter = 0

    def get_damage(self, damage, player):
        self.hp -= damage
        self.image = self.damage_pic
        if self.hp <= 0:
            self.kill()
            player.score += 0
            # TODO: improve it

    def update(self, *args):
        self.moving(args[0])
