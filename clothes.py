import pygame as pg
import pygame.freetype


pygame.init()
shrift = pygame.freetype.Font("shrift.otf", 25)


class Clothes:
    def __init__(self, cost, kartinka, x, y, igra, nazvanie, kypleno, nadeto):
        a = nazvanie.find(".")
        self.nazvanie = nazvanie[0:a]
        self.kypleno = kypleno
        self.nadeto = nadeto
        self.kartinka = kartinka
        self.cost = cost
        self.igra = igra
        self.shrift = shrift
        self.hitbox = pg.Rect([x, y], [self.kartinka.get_width(), self.kartinka.get_height()])

    def draw(self):
        self.igra.screen.blit(self.kartinka, self.hitbox)

    def getdict(self):
        a = {"nadeto": self.nadeto, "kypleno": self.kypleno, "cost": self.cost, "nazvanie": self.nazvanie}
        return a