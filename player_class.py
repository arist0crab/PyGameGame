import pygame


class Player(pygame.sprite.Sprite):

    """Realizing player class."""

    def __init__(self, size, cords, speed, animations, *groups):

        super().__init__(*groups)

        """We're pretending on skins, so images of player we'll get by class arguments (check animations), 
        not constants. Pictures in animations are NOT pygame surface objects, so we're fixing it later.
        
        Here's animation structure: 
        animations = [ [going_right], [going_left], [stance_right], [stance_left] ]
        
        IMPORTANT: in each element of animation list must be the same number of pictures.
        """

        """Here we're changing size of player pictures (check size parameter)."""
        animations = [[pygame.transform.scale(pygame.image.load(pic), size) for pic in anim] for anim in animations]

        # region variables of animations only
        self.anim_right, self.anim_left, self.stance_right, self.stance_left = animations
        self.current_anim = self.stance_right  # TODO: should we make this parameter mutable?
        self.max_anim_count = 7
        self.anim_count = 0
        # endregion

        self.image = self.stance_right[0]
        self.rect = self.image.get_rect()
        self.rect.center = cords

        self.speed = speed
        self.cords = [0, 0]

        """This argument is for correct drawing sprites. Check 'level_class.py'."""
        self._layer = 1

    def keys(self):

        """Realizing movement of player."""

        keys = pygame.key.get_pressed()

        self.cords = [0, 0]

        if keys[pygame.K_d]:
            self.cords[0] += self.speed
            self.current_anim = self.anim_right
        if keys[pygame.K_a]:
            self.cords[0] -= self.speed
            self.current_anim = self.anim_left
        if keys[pygame.K_w]:
            self.cords[1] -= self.speed
        if keys[pygame.K_s]:
            self.cords[1] += self.speed
        elif not any([keys[pygame.K_d], keys[pygame.K_a]]):
            if self.current_anim == self.anim_left:
                self.current_anim = self.stance_left
            elif self.current_anim == self.anim_right:
                self.current_anim = self.stance_right

        self.anim_count += 1

        if self.anim_count >= self.max_anim_count * len(self.anim_right):
            self.anim_count = 0

        self.image = self.current_anim[self.anim_count // self.max_anim_count]
        self.rect = self.rect.move(self.cords)

    def update(self):
        self.keys()
