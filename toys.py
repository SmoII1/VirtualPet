import pygame as pg


class Toys:
    def __init__(self, kartinka, x, y, igra):
        self.kartinka = kartinka
        self.igra = igra
        self.hitbox = pg.Rect([x, y], self.kartinka.get_size())

    def draw(self):
        self.igra.screen.blit(self.kartinka, self.hitbox)

    def dvishenie(self):
        self.hitbox.y = self.hitbox.y+2
