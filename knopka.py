import pygame as pg
import pygame.freetype


pygame.init()
shrift = pygame.freetype.Font("shrift.otf", 25)


class Knopka:
    def __init__(self, x, y, kartinka, tekst, igra, nachatai, funk):
        self.funk = funk
        self.a = 0
        self.nenachatai = kartinka
        self.kartinka = kartinka
        self.nachatai = nachatai
        self.tekst = tekst
        self.hitbox = pg.Rect([x, y], [self.kartinka.get_width(), self.kartinka.get_height()])
        self.igra = igra

    def draw(self):
        self.igra.screen.blit(self.kartinka, self.hitbox)
        shrift.render_to(self.igra.screen, [self.hitbox.x+10, self.hitbox.y+20], self.tekst, [0, 0, 0])

    def click(self):
        self.kartinka = self.nachatai
        self.a = pg.time.get_ticks()
        self.funk()

    def update(self):
        self.v = pg.time.get_ticks()
        if self.v - self.a >= 500:
            self.kartinka = self.nenachatai
