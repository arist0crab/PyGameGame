import pygame
import sys


def terminate():
    pygame.quit()
    sys.exit()


def start_screen(screen, clock, FPS):
    intro_text = ["Welcome to our game.",
                  "",
                  "Here is our rules:",
                  "#1. Try to stay alive and kill as many enemies, as possible.",
                  "#2. It is not a bug, it is feature.",
                  "#3. No rules, good luck. Just try to guess how to play."
                  ]

    fon = pygame.transform.scale(pygame.image.load('static/fon_for_start_screen.jpg'), screen.get_size())
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 80
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color((255, 0, 0)))
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    terminate()
                else:
                    return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)
