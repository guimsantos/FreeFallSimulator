import pygame as pg


class Obj(pg.sprite.Sprite):

    def __init__(self,img, x, y, *groups):
        super().__init__(*groups)
        self.image = pg.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y


class Ball(Obj):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)

        self.velocidade = 0
        self.grav = True
        self.stop = True
        self.quique = 0
        self.gravidade = 1

    def fall(self):
        if self.grav:
            self.velocidade += self.gravidade
            self.rect[1] += self.velocidade
        if self.rect[1] >= 431:
            self.rect[1] = 431

    def colision(self, group):

        col = pg.sprite.spritecollide(self, group, False)

        if col:
            self.stop = False


        if col:

            self.rect.bottom = col[0].rect.top
            self.quique += 1
            if self.quique <= 4:
                self.velocidade *= -0.35
            else:
                self.grav = False

    def update(self, *args):
        self.fall()


class Terreno(Obj):

    def __init__(self, img, x, y, limite, *groups):
        super().__init__(img, x, y, *groups)

        self.velocidade = 0
        self.gravidade = -1
        self.limite = limite
        self.grav = True

    def move(self):
        if self.grav:

            if self.rect[1] <= self.limite + 100:
                self.rect[1] = self.limite
                self.grav = False

            elif self.rect[1] >= self.limite + 100:
                self.velocidade += self.gravidade
                self.rect[1] += self.velocidade

    def update(self, *args):
        self.move()


class Regua(Obj):

    def __init__(self, img, x, y, limite, *groups):
        super().__init__(img, x, y, *groups)

        self.velocidade = 0
        self.gravidade = -1
        self.limite = limite
        self.grav = True


class Texto:

    def __init__(self, txt, size, x, y):

        self.font = pg.font.SysFont('arial', size)
        self.render = self.font.render(txt, True, (255,255,255))
        self.x = x
        self.y = y

    def draw(self, window):
        window.blit(self.render, (self.x, self.y))

    def update(self, txt):
        self.render = self.font.render(txt, True, (255, 255, 255))
