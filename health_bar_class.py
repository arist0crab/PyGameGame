import pygame


class HealthBar:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player

    def render(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.screen.get_size()[0] - 20 - self.player.health_bar_length, 20, self.player.health_bar_length, 25))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.screen.get_size()[0] - 20 - self.player.health_bar_length, 20, self.player.hp / self.player.health_ratio, 25))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen.get_size()[0] - 20 - self.player.health_bar_length, 20, self.player.health_bar_length, 25), 4)
