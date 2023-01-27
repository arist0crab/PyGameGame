import pygame
from spritesheet import SpriteSheet
from button_class import Button


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.center_point_y = screen.get_size()[0] // 2

        self.start_button_spritesheet = SpriteSheet("static/Buttons_Spritesheet/Start_Button.png")
        self.start_button_images = self.start_button_spritesheet.images_at([(i*56, 0, 56, 32) for i in range(0, 10)], colorkey=(0, 0, 0))
        self.start_button_position = screen.get_size()[1] // 4
        self.start_button = Button(self.center_point_y - 28 * 5, self.start_button_position, 56, 32, self.start_button_images, scale=5)

        self.developers_button_spritesheet = SpriteSheet("static/Buttons_Spritesheet/Developers_Button.png")
        self.developers_button_images = self.developers_button_spritesheet.images_at([(i*126, 0, 126, 32) for i in range(0, 10)], colorkey=(0, 0, 0))
        self.developers_button_position = (screen.get_size()[1] // 4) * 2
        self.developers_button = Button(self.center_point_y - 63 * 5, self.developers_button_position, 126, 32, self.developers_button_images, scale=5)

        self.about_button_spritesheet = SpriteSheet("static/Buttons_Spritesheet/About_Button.png")
        self.about_button_images = self.about_button_spritesheet.images_at([(i*70, 0, 70, 32) for i in range(0, 10)], colorkey=(0, 0, 0))
        self.about_button_position = (screen.get_size()[1] // 4) * 3
        self.about_button = Button(self.center_point_y - 35 * 5, self.about_button_position, 70, 32, self.about_button_images, scale=5)

    def render(self):
        context = {"Start": False, "Developers": False, "About": False}
        background = pygame.image.load('static/space_background.jpg')
        self.screen.blit(background, background.get_rect())
        if self.start_button.draw(self.screen):
            context["Start"] = True
        if self.developers_button.draw(self.screen):
            context["Developers"] = True
        if self.about_button.draw(self.screen):
            context["About"] = True
        return context
