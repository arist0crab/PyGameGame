import pygame
import sys

GLOBAL_PLAYER_SCORE = 0


def terminate():
    pygame.quit()
    sys.exit()


def end_screen(screen, clock, FPS):
    intro_text = ["Congratulations.",
                  "You are dead.",
                  f"Your score in this session: {GLOBAL_PLAYER_SCORE}",
                  "Guess how to escape. See ya."
                  ]

    fon = pygame.transform.scale(pygame.image.load('static/fon_for_end_screen.png'), screen.get_size())
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 170
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
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)
