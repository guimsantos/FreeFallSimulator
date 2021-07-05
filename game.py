import pygame as pg
from obj import Obj, Ball, Texto, Terreno
from random import randint


class Game:

    def __init__(self):

        self.all_sprites = pg.sprite.Group()
        self.plat_sprite = pg.sprite.Group()
        self.ball_sprite = pg.sprite.Group()
        self.buttom_sprite = pg.sprite.Group()

        self.altura = 10000  # <--- Mudar altura da queda aqui

        self.regua1 = Obj('assets/regua.png', 0, -64 , self.all_sprites)
        self.regua2 = Obj('assets/regua.png', 0, 464, self.all_sprites)
        self.grass = Terreno('assets/grassplatform.png', 0, 464 + self.altura, 464, self.all_sprites, self.plat_sprite)
        self.ball = Ball('assets/GreenBall.png', 145, 254, self.ball_sprite)

        self.resetbutttom = Obj('assets/reset.png', 128, 50, self.buttom_sprite)
        self.showbuttom = Obj('assets/show.png', 128, 100, self.buttom_sprite)

        self.tick = 1
        self.gravter = True

        self.reset = True
        self.show = False

        self.gravidade = -1
        self.vel = 0

        # Parâmetros
        self.time = 0
        self.res_altura = 0
        self.res_vel = 0

        # Textos dos parâmetros
        self.clock = Texto(str(round(self.time, 3)) + ' s', 30, 210, 50)
        self.show_altura = Texto(str(self.res_altura), 30, 210, 100)
        self.show_vel = Texto(str(self.res_vel), 30, 210, 150)


    def events(self, event):
        if event.type == pg.MOUSEBUTTONUP:
            if self.resetbutttom.rect.collidepoint(pg.mouse.get_pos()):
                self.reset = False
            if self.showbuttom.rect.collidepoint(pg.mouse.get_pos()):
                self.show = True


    def draw(self, window):

        pg.Surface.fill(window, (150, 230, 255))
        self.all_sprites.draw(window)
        self.ball_sprite.draw(window)
        self.clock.draw(window)
        if not self.ball.stop:
            self.buttom_sprite.draw(window)

        if self.show:
            self.show_altura.draw(window)
            self.show_vel.draw(window)

    def update(self):

        self.mov_regua()
        self.all_sprites.update()
        self.buttom_sprite.update()

        if not self.grass.grav:
            if self.gravter:
                self.ball.velocidade = self.grass.velocidade * - 1
                self.gravter = False
            self.ball.colision(self.plat_sprite)
            self.ball_sprite.update()

        if self.ball.stop:
            self.calc_var()

        self.clock.update(str(round(self.time, 3)) + ' s')
        self.show_altura.update(str(round(self.res_altura, 3)) + ' m')
        self.show_vel.update(str(round(self.res_vel, 3)) + ' m/s')

    def calc_var(self):
        # tempo
        self.time += 0.033

        # Altura
        self.res_altura = 0.5 * 9.81 * (round(self.time, 3) ** 2)

        # Velocidade Final
        self.res_vel = 9.81 * round(self.time, 3)


    def mov_regua(self):

        if self.grass.grav:
            self.vel += self.gravidade

            self.regua1.rect[1] += self.vel
            self.regua2.rect[1] += self.vel

            if self.regua1.rect[1] <= -592:
                self.regua1.rect[1] = -64
            if self.regua2.rect[1] <= -64:
                self.regua2.rect[1] = 464

        else:
            self.regua1.rect[1] = -64
            self.regua2.rect[1] = -64









