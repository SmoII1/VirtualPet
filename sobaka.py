import pygame as pg
import settings


class Sobaka:
    def __init__(self, x, y, igra, shirina, visota):
        self.kartinka = pg.image.load("images/dog.png")
        self.kartinka = pg.transform.scale(self.kartinka, [shirina, visota])
        self.hitbox = pg.Rect([x, y], [shirina, visota])
        self.igra = igra

    def draw(self):
        self.igra.screen.blit(self.kartinka, self.hitbox)

    def update(self):
        self.a = pg.key.get_pressed()
        if self.a[pg.K_a] is True and self.hitbox.x > 100:
            self.hitbox.x = self.hitbox.x - 2
        if self.a[pg.K_d] is True and self.hitbox.right < settings.SCREEN_WIDTH-100:
            self.hitbox.x = self.hitbox.x + 2
