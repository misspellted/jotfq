import pygame

from window import Window

class Game:
    def __init__(this):
        pygame.init()

        this._clock = pygame.time.Clock()

    def play(this):
        window = Window(1280, 720)
        window.setCaption("Journey of the Faerie Queen")

        playing = True

        while playing:
            this._clock.tick(60)

            playing = not pygame.event.peek(pygame.QUIT)

            if playing:
                keys = pygame.key.get_pressed()

                playing = not keys[pygame.K_ESCAPE]

                if playing:
                    window.refresh()

            if not playing:
                window.setCaption("Exiting...")

        pygame.quit()
