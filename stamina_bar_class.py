import pygame


class StaminaBar:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player

    def render(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (self.screen.get_size()[0] - 20 - self.player.stamina_bar_length, 60,
                                                  self.player.stamina_bar_length, 25))
        pygame.draw.rect(self.screen, (0, 255, 0), (self.screen.get_size()[0] - 20 - self.player.stamina_bar_length,
                                                    60, self.player.stamina / self.player.stamina_ratio, 25))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen.get_size()[0] - 20 - self.player.stamina_bar_length,
                                                        60, self.player.stamina_bar_length, 25), 4)
