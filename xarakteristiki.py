import pygame as pg
import pygame.freetype

pygame.init()
shrift = pygame.freetype.Font("shrift.otf", 45)

class Xarakteristika:
    def __init__(self, kartinka, chislo, x, y, igra):
        self.kartinka = kartinka
        self.chislo = chislo
        self.hitbox = pg.Rect([x, y], [self.kartinka.get_width(), self.kartinka.get_height()])
        self.igra = igra

    def draw(self):
        self.igra.screen.blit(self.kartinka, self.hitbox)
        shrift.render_to(self.igra.screen, [self.hitbox.x+130, self.hitbox.y+50], str(self.chislo), [0, 0, 0])