import pygame

class Window:
    def __init__(this, length, height):
        if not pygame.display.get_init():
            pygame.display.init()

        this._length = length
        this._height = height
        this._window = pygame.display.set_mode((length, height))
        this._items = list()

    def setCaption(this, caption):
        pygame.display.set_caption(caption)

    def display(this, surface, x, y):
        this._items.append((surface, x, y))

    def refresh(this):
        # Always start with a fresh window.
        this._window.fill((0, 0, 0))

        for item in this._items:
            surface, x, y = item
            this._window.blit(surface, (x, y))

        pygame.display.update()

        del this._items[:]
