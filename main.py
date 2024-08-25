import pygame as pg
import settings
import sobaka
import xarakteristiki
import random
import knopka
import menu
import json
from kartinki import*
import pygame.freetype

pg.init()
shrift = pygame.freetype.Font("shrift.otf", 25)


class Game:
    def __init__(self):

        self.screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")
        self.fon = pg.image.load("images/background.png")
        self.fon = pg.transform.scale(self.fon, [settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
        self.soba4ka = sobaka.Sobaka(325, 170, self, 250, 250)
        file = open("data.json", "r", encoding="UTF-8")
        self.data = json.load(file)
        self.happy = xarakteristiki.Xarakteristika(karttinkahappy, self.data["happy"], 10, 10, self)
        self.health = xarakteristiki.Xarakteristika(karttinkahealth, self.data["health"], 10, 100, self)
        self.golod = xarakteristiki.Xarakteristika(kartinkagolod, self.data["golod"], 10, 200, self)
        self.money = xarakteristiki.Xarakteristika(karttinkamoney, self.data["moneta"], 10, 300, self)
        self.odeshda = self.data["odehda"]
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
        self.m = 1
        self.levelup = {500: False, 1500: False, 4000: False, 10000: False, 40000: False}
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
                data = {"moneta": self.money.chislo, "health": self.health.chislo, "happy": self.happy.chislo, "golod": self.golod.chislo, "odehda": self.menuclothink.slovar()}
                file = open("data.json", "w", encoding="UTF-8")
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.close()
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for knopo4ka in self.knopki:
                    if knopo4ka.hitbox.collidepoint(event.pos):
                        knopo4ka.click()
                if self.soba4ka.hitbox.collidepoint(event.pos):
                    self.money.chislo = self.money.chislo + self.m
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
        for klych in self.levelup:
            if self.levelup[klych] is False:
                shrift.render_to(self.screen, [0, 0], str(klych), [0, 0, 0])
                break

    def funkeda(self):
        self.menu = self.menueda

    def funkigra(self):
        self.menu = self.menuigra

    def funkclothink(self):
        self.menu = self.menuclothink

    def funklevelup(self):
        for klych in self.levelup:
            if self.levelup[klych] is False and self.money.chislo >= klych:
                self.m = self.m + 1
                self.levelup[klych] = True
                self.money.chislo = self.money.chislo - klych
                break

if __name__ == "__main__":
    Game()
