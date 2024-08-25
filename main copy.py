import pygame as pg
import settings
import sobaka
import xarakteristiki
import random
import knopka
import menu
from kartinki import*

pg.init()


class Game:
    def __init__(self):

        self.screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")
        self.fon = pg.image.load("images/background.png")
        self.fon = pg.transform.scale(self.fon, [settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
        self.soba4ka = sobaka.Sobaka(325, 170, self, 250, 250)
        self.happy = xarakteristiki.Xarakteristika(karttinkahappy, 100, 10, 10, self)
        self.health = xarakteristiki.Xarakteristika(karttinkahealth, 100, 10, 100, self)
        self.golod = xarakteristiki.Xarakteristika(kartinkagolod, 100, 10, 200, self)
        self.money = xarakteristiki.Xarakteristika(karttinkamoney, 0, 10, 300, self)
        self.xarakteristiki = [self.happy, self.golod, self.health, self.money]
        self.sobhelth = pg.USEREVENT
        self.sobhappy = pg.USEREVENT+1
        self.sobgolod = pg.USEREVENT+2
        pg.time.set_timer(self.sobhelth, random.randint(500, 3000))
        pg.time.set_timer(self.sobgolod, random.randint(500, 3000))
        pg.time.set_timer(self.sobhappy, random.randint(500, 3000))
        self.knopka1 = knopka.Knopka(700, 50, kartinkaknopka, "Еда", self, kartinkanachatai, self.funkeda)
        self.knopka2 = knopka.Knopka(700, 150, kartinkaknopka, "Одежда", self, kartinkanachatai, self.funkclothink)
        self.knopka3 = knopka.Knopka(700, 250, kartinkaknopka, "Игра", self, kartinkanachatai, self.funkigra)
        self.knopka4 = knopka.Knopka(700, 350, kartinkaknopka, "Улучшение", self, kartinkanachatai, self.funklevelup)
        self.knopki = []
        self.knopki.append(self.knopka1)
        self.knopki.append(self.knopka2)
        self.knopki.append(self.knopka3)
        self.knopki.append(self.knopka4)
        self.menueda = menu.Menueda(kartinkamenueda, self)
        self.menuigra = menu.Menuigra(kartinkamenuigra, self)
        self.menuclothink = menu.Menuclothink(kartinkamenueda, self)
        self.menu = None
        self.run()

    def run(self):
        while True:
            self.screen.blit(self.fon, [0, 0])
            if self.menu is None:
                self.update()
                self.draw()
                self.event()
            else:
                self.menu.update()
                self.menu.draw()
                self.menu.event()
            pg.display.flip()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for knopo4ka in self.knopki:
                    if knopo4ka.hitbox.collidepoint(event.pos):
                        knopo4ka.click()
                if self.soba4ka.hitbox.collidepoint(event.pos):
                    self.money.chislo = self.money.chislo + 1
            if event.type == self.sobgolod:
                self.golod.chislo = self.golod.chislo - random.randint(1, 4)
                pg.time.set_timer(self.sobgolod, random.randint(500, 3000))
            if event.type == self.sobhappy:
                self.happy.chislo = self.happy.chislo - random.randint(1, 4)
                pg.time.set_timer(self.sobhappy, random.randint(500, 3000))
            if event.type == self.sobhelth:
                self.health.chislo = self.health.chislo - random.randint(1, 4)
                pg.time.set_timer(self.sobhelth, random.randint(500, 3000))

    def update(self):
        for knopo4ka in self.knopki:
            knopo4ka.update()

    def draw(self):
        self.screen.blit(self.fon, [0, 0])
        for xarakteristika in self.xarakteristiki:
            xarakteristika.draw()
        self.knopka1.draw()
        self.knopka2.draw()
        self.knopka3.draw()
        self.knopka4.draw()
        self.soba4ka.draw()
        for clothing in self.menuclothink.clothesspis:
            if clothing.nadeto is True:
                clothing.draw()

    def funkeda(self):
        self.menu = self.menueda

    def funkigra(self):
        self.menu = self.menuigra

    def funkclothink(self):
        self.menu = self.menuclothink

    def funklevelup(self):
        pass

if __name__ == "__main__":
    Game()
