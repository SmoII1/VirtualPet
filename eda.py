import pygame as pg
import pygame.freetype


pygame.init()
shrift = pygame.freetype.Font("shrift.otf", 25)


class Eda:
    def __init__(self, kartinka, x, y, chena, igra, nazvanie):
        a = nazvanie.find(".")
        self.nazvanie = nazvanie[0:a]
        self.kartinka = kartinka
        self.chena = chena
        self.igra = igra
        self.shrift = shrift
        self.hitbox = pg.Rect([x, y], [self.kartinka.get_width(), self.kartinka.get_height()])

    def draw(self):
        self.igra.screen.blit(self.kartinka, self.hitbox)
        shrift.render_to(self.igra.screen, [self.hitbox.x+105, self.hitbox.y+200], str(self.chena), [0, 0, 0])
        shrift.render_to(self.igra.screen, [self.hitbox.x+90, self.hitbox.y+230], str(self.nazvanie), [0, 0, 0])
