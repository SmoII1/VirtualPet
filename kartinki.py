import pygame as pg
import settings
import os

kartinkagolod = pg.image.load("images/satiety.png")
karttinkahealth = pg.image.load("images/health.png")
karttinkamoney = pg.image.load("images/money.png")
karttinkahappy = pg.image.load("images/happiness.png")
kartinkagolod = pg.transform.scale(kartinkagolod, [130, 130])
karttinkahealth = pg.transform.scale(karttinkahealth, [130, 130])
karttinkahappy = pg.transform.scale(karttinkahappy, [130, 130])
karttinkamoney = pg.transform.scale(karttinkamoney, [130, 130])
kartinkaknopka = pg.image.load("images/button.png")
kartinkaknopka = pg.transform.scale(kartinkaknopka, [150, 60])
kartinkanachatai = pg.image.load("images/button_clicked.png")
kartinkanachatai = pg.transform.scale(kartinkanachatai, [150, 60])
kartinkamenueda = pg.image.load("images/menu/menu_page.png")
kartinkamenueda = pg.transform.scale(kartinkamenueda, [settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
kartinkamenuigra = pg.image.load("images/game_background.png")
kartinkamenuigra = pg.transform.scale(kartinkamenuigra, [settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
foodnames = os.listdir("images/food")
foods = []
for eda in foodnames:
    food = pg.image.load("images/food/"+eda)
    food = pg.transform.scale(food, [250, 250])
    foods.append(food)
print(foods)
clothesnames = os.listdir("images/items")
clothes = []
for item in clothesnames:
    itempic = pg.image.load("images/items/"+item)
    itempic = pg.transform.scale(itempic, [250, 250])
    clothes.append(itempic)
toysnames = os.listdir("images/toys")
toysimages = []
for toy in toysnames:
    toyspic = pg.image.load("images/toys/"+toy)
    toyspic = pg.transform.scale(toyspic, [150, 150])
    toysimages.append(toyspic)
