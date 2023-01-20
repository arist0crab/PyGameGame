import pygame
from health_bar_class import HealthBar
from stamina_bar_class import StaminaBar
import math


class Player(pygame.sprite.Sprite):

    """Realizing player class."""

    def __init__(self, screen, size, cords, speed, hp, animations, level_tile_group, FPS, clock,
                 lava_tiles_group, empty_group, potion_group, enemies_group, main_sprites_group, *groups):

        super().__init__(*groups)

        self.screen = screen
        """We're pretending on skins, so images of player we'll get by class arguments (check animations), 
        not constants. Pictures in animations are NOT pygame surface objects, so we're fixing it later.
        
        Here's animation structure: 
        animations = [ [going_right], [going_left], [stance_right], [stance_left] ]
        
        IMPORTANT: in each element of animation list must be the same number of pictures.
        """

        """Here we're changing size of player pictures (check size parameter)."""
        animations = [[pygame.transform.scale(pygame.image.load(pic), size) for pic in anim] for anim in animations]
        # TODO: we can flip surfaces in pygame, so we should remove anim_left and stance left from animations
        # region variables of animations only
        self.anim_right, self.anim_left, self.stance_right, self.stance_left = animations
        self.current_anim = self.stance_right  # TODO: should we make this parameter mutable?
        self.max_anim_count = 7
        self.anim_count = 0
        # endregion

        self.screen = screen

        self.image = self.stance_right[0]
        self.rect = self.image.get_rect()
        self.rect.center = cords
        self.mask = pygame.mask.from_surface(self.image)

        self.hp = hp
        self.max_hp = 100
        self.screen_width, self.screen_height = screen.get_size()

        self.health_bar_length = self.screen_width / 3.5
        self.health_ratio = self.max_hp / self.health_bar_length
        self.health_bar = HealthBar(self.screen, self)

        self.enemy_group = enemies_group

        self.circular_attack_range = 500
        self.circular_attack_damage = 25
        self.circular_attack_stamina = 15

        self.last_stamina_recovery = pygame.time.get_ticks() / 1000
        self.stamina_recovery_speed = 0.5
        self.stamina = 100
        self.max_stamina = 100
        self.stamina_bar_length = self.screen_width / 3.5
        self.stamina_ratio = self.max_stamina / self.stamina_bar_length
        self.stamina_bar = StaminaBar(self.screen, self)

        self.speed = speed
        self.cords = [0, 0]
        self.tiles_in_level = level_tile_group

        self.rmb_locker = True

        """This argument is for correct drawing sprites. Check 'level_class.py'."""
        self._layer = 1

    def get_distance(self, target):
        return math.sqrt((self.rect.center[0] - target.rect.center[0]) ** 2 + (self.rect.center[1] - target.rect.center[1]) ** 2)

    def get_damage(self, damage):
        if self.hp > 0:
            self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.kill()
            # TODO: add the cutscene of dyeing process

    def circular_attack(self):
        for enemy in self.enemy_group:
            print(self.get_distance(enemy))
            if self.get_distance(enemy) <= self.circular_attack_range:
                print(enemy)
                enemy.get_damage(self.circular_attack_damage)


    def keys(self):

        """Realizing movement of player."""

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        self.cords = [0, 0]

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.cords[0] += self.speed
            self.current_anim = self.anim_right
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.cords[0] -= self.speed
            self.current_anim = self.anim_left
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.cords[1] -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.cords[1] += self.speed
        if mouse[0] and self.rmb_locker and self.stamina >= self.circular_attack_stamina:
            self.stamina -= self.circular_attack_stamina
            self.rmb_locker = False
            self.circular_attack()
        if not mouse[0]:
            self.rmb_locker = True
        elif not any([
            keys[pygame.K_d], keys[pygame.K_a], keys[pygame.K_w], keys[pygame.K_s],
            keys[pygame.K_RIGHT], keys[pygame.K_LEFT], keys[pygame.K_UP], keys[pygame.K_DOWN]
                      ]):
            if self.current_anim == self.anim_left:
                self.current_anim = self.stance_left
            elif self.current_anim == self.anim_right:
                self.current_anim = self.stance_right

        self.anim_count += 1

        if self.anim_count >= self.max_anim_count * len(self.anim_right):
            self.anim_count = 0

        self.image = self.current_anim[self.anim_count // self.max_anim_count]
        self.rect = self.rect.move(self.cords)

    def update(self, *args):
        if pygame.time.get_ticks() - self.last_stamina_recovery >= self.stamina_recovery_speed and self.stamina < self.max_stamina:
            self.last_stamina_recovery = pygame.time.get_ticks() / 1000
            self.stamina += 1
        self.keys()
