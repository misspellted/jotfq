import pygame

from window import Window
from clearing import Clearing

CLOCK_TICKS = 60
CLEARING_X = 10
CLEARING_Y = 10

class Game:
    def __init__(this):
        pygame.init()

        this._clock = pygame.time.Clock()

    def play(this):
        window = Window(1280, 720)
        window.setCaption("Journey of the Faerie Queen")

        clearing = Clearing()

        playing = True

        while playing:
            this._clock.tick(CLOCK_TICKS)

            playing = not pygame.event.peek(pygame.QUIT)

            if playing:
                keys = pygame.key.get_pressed()

                playing = not keys[pygame.K_ESCAPE]

                if playing:
                    window.display(clearing.render(), CLEARING_X, CLEARING_Y)
                    window.refresh()

            if not playing:
                window.setCaption("Exiting...")

        pygame.quit()
