import pygame


class Button:
    def __init__(self, x, y, width, height, animation_images, scale):
        self.animation_images = [pygame.transform.scale(i, (int(width * scale), int(height * scale))) for i in
                                 animation_images]
        self.i = 0
        self.rect = self.animation_images[-1].get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        current_image = self.animation_images[-1]
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 0:
                self.i = self.i + 1 if self.i < len(self.animation_images) - 1 else 0
                current_image = self.animation_images[self.i]
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            self.i = 0
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(current_image, (self.rect.x, self.rect.y))
        return action
