import pygame as pg
from game import Game

class Main:

    def __init__(self):

        pg.font.init()

        self.screen = pg.display.set_mode((350, 528))
        pg.display.set_caption('Queda Livre')

        self.game = Game()

        self.fps = pg.time.Clock()
        self.loop = True

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.loop = False

            self.game.events(event)
            if not self.game.reset:
                self.loop = False

    def draw(self):
        self.game.draw(self.screen)
        self.game.update()

    def update(self):

        while self.loop:
            self.events()
            self.draw()

            self.fps.tick(30)
            pg.display.update()


loop = True

while loop:
    Main().update()
