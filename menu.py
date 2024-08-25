import pygame as pg
import pygame.freetype
import knopka
from kartinki import*
import eda
import random
import clothes as cl
import sobaka
import toys 

pygame.init()
shrift = pygame.freetype.Font("shrift.otf", 25)

class Menu:
    def __init__(self, kartinka, igra):
        self.kartinka = kartinka
        self.igra = igra

    def draw(self):
        self.igra.screen.blit(self.kartinka, [0, 0])

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.igra.menu = None

    def update(self):
        pass


class Menueda:
    def __init__(self, kartinka, igra):
        self.kartinka = kartinka
        self.igra = igra
        self.knopka1 = knopka.Knopka(700, 50, kartinkaknopka, "Вперёд", self.igra, kartinkanachatai, self.vperiod)
        self.knopka2 = knopka.Knopka(700, 150, kartinkaknopka, "Назад", self.igra, kartinkanachatai, self.nazad)
        self.knopka3 = knopka.Knopka(700, 250, kartinkaknopka, "Съесть", self.igra, kartinkanachatai, self.kyshat)
        a = 0
        self.edaspis = []
        for foodpic in foods:
            food = eda.Eda(foodpic, 325, 170, random.randint(100, 500), self.igra, foodnames[a])
            self.edaspis.append(food)
            a = a + 1
        self.a = 0
        self.knopki = [self.knopka1, self.knopka2, self.knopka3]

    def draw(self):
        self.igra.screen.blit(self.kartinka, [0, 0])
        for knopka in self.knopki:
            knopka.draw()
        self.edaspis[self.a].draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.igra.menu = None
            if event.type == pg.MOUSEBUTTONDOWN:
                for knopo4ka in self.knopki:
                    if knopo4ka.hitbox.collidepoint(event.pos):
                        knopo4ka.click()

    def update(self):
        for knopka in self.knopki:
            knopka.update()

    def vperiod(self):
        if self.a < len(self.edaspis)-1:
            self.a = self.a+1
        else:
            self.a = 0

    def nazad(self):
        if self.a > 0:
            self.a = self.a-1
        else:
            self.a = len(self.edaspis)-1

    def kyshat(self):
        if self.igra.money.chislo >= self.edaspis[self.a].chena:
            if self.a != len(self.edaspis)-1:
                self.igra.money.chislo = self.igra.money.chislo - self.edaspis[self.a].chena
                self.igra.golod.chislo = self.igra.golod.chislo + random.randint(10, 30)
                if self.igra.golod.chislo >= 100:
                    self.igra.golod.chislo = 100
            else:
                self.igra.health.chislo = self.igra.health.chislo + 25
                if self.igra.health.chislo >= 100:
                    self.igra.health.chislo = 100


class Menuclothink:
    def __init__(self, kartinka, igra):
        self.kartinka = kartinka
        self.igra = igra
        self.knopka3 = knopka.Knopka(700, 50, kartinkaknopka, "Вперёд", self.igra, kartinkanachatai, self.vperiod)
        self.knopka4 = knopka.Knopka(700, 150, kartinkaknopka, "Назад", self.igra, kartinkanachatai, self.nazad)
        self.knopka1 = knopka.Knopka(700, 250, kartinkaknopka, "Надеть", self.igra, kartinkanachatai, self.nadet)
        self.knopka2 = knopka.Knopka(700, 350, kartinkaknopka, "Купить", self.igra, kartinkanachatai, self.kypit)
        self.knopki = [self.knopka1, self.knopka2, self.knopka3, self.knopka4]
        self.a = 0
        b = 0
        self.clothesspis = []
        for itempic in clothes:
            odeshda = self.igra.odeshda[b]
            item = cl.Clothes(odeshda["cost"], itempic, 325, 170, igra, clothesnames[b], odeshda["kypleno"], odeshda["nadeto"])
            self.clothesspis.append(item)
            b = b + 1

    def draw(self):
        self.igra.screen.blit(self.kartinka, [0, 0])
        for knopka in self.knopki:
            knopka.draw()
        self.clothesspis[self.a].draw()
        shrift.render_to(self.igra.screen, [self.clothesspis[self.a].hitbox.x+105, self.clothesspis[self.a].hitbox.y+200], str(self.clothesspis[self.a].cost), [0, 0, 0],)
        shrift.render_to(self.igra.screen, [self.clothesspis[self.a].hitbox.x+90, self.clothesspis[self.a].hitbox.y+230], str(self.clothesspis[self.a].nazvanie), [0, 0, 0])
        if self.clothesspis[self.a].kypleno is True:
            shrift.render_to(self.igra.screen, [390, 400], "Куплено", [0, 255, 0])
        else:
            shrift.render_to(self.igra.screen, [390, 400], "Не куплено", [255, 0, 0])
        if self.clothesspis[self.a].nadeto is True:
            shrift.render_to(self.igra.screen, [390, 430], "Надето", [0, 255, 0])
        else:
            shrift.render_to(self.igra.screen, [390, 430], "Не надето", [255, 0, 0])

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.igra.menu = None
            if event.type == pg.MOUSEBUTTONDOWN:
                for knopo4ka in self.knopki:
                    if knopo4ka.hitbox.collidepoint(event.pos):
                        knopo4ka.click()

    def update(self):
        for knopka in self.knopki:
            knopka.update()

    def nadet(self):
        if self.clothesspis[self.a].kypleno is True:
            self.clothesspis[self.a].nadeto = not self.clothesspis[self.a].nadeto


    def kypit(self):
        if self.igra.money.chislo >= self.clothesspis[self.a].cost:
            self.igra.money.chislo = self.igra.money.chislo - self.clothesspis[self.a].cost
            self.clothesspis[self.a].kypleno = True
            print("Купили")
        else:
            print("Не купили")

    def vperiod(self):
        if self.a < len(self.clothesspis)-1:
            self.a = self.a+1
        else:
            self.a = 0

    def nazad(self):
        if self.a > 0:
            self.a = self.a-1
        else:
            self.a = len(self.clothesspis)-1

    def slovar(self):
        c = []
        for a in self.clothesspis:
            b = a.getdict()
            c.append(b)
        return c


class Menuigra:
    def __init__(self, kartinka, igra):
        self.kartinka = kartinka
        self.soba4ka = sobaka.Sobaka(325, 250, igra, 250, 250)
        self.igra = igra
        self.sobitie = pg.USEREVENT+3
        self.b = 1
        pg.time.set_timer(self.sobitie, random.randint(500, 1000))
        self.toyslist = []
        self.a = 0

    def draw(self):
        self.igra.screen.blit(self.kartinka, [0, 0])
        self.soba4ka.draw()
        for toy1 in self.toyslist:
            toy1.draw()
        shrift.render_to(self.igra.screen, [150, 150], str(self.a), [0, 0, 0])

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.igra.menu = None
            if event.type == self.sobitie:
                toy = toys.Toys(random.choice(toysimages), random.randint(100, settings.SCREEN_WIDTH-100), 0, self.igra)
                self.toyslist.append(toy)

    def update(self):
        self.soba4ka.update()
        for toy2 in self.toyslist:
            toy2.dvishenie()
            if toy2.hitbox.colliderect(self.soba4ka.hitbox) is True:
                self.toyslist.remove(toy2)
                self.a = self.a+1
