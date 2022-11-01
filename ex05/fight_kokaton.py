import pygame as pg
import sys
from random import randint

check_game = 0

class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)#(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg)#"ex05/fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img)#"ex05/fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)#2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy#900, 400

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) # 練習3

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                # 練習7
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr)#= scr.sfc.blit(self.sfc, self.rct)


class Enemy:
    def __init__(self, img, zoom, vxy, scr:Screen):
        sfc = pg.image.load(img)#"ex05/fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)#2.0
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6
    
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) 
    
    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        if self.vx < 0:
            self.vx -= 0.0005
        elif self.vx > 0:
            self.vx += 0.0005
        if self.vy < 0:
            self.vy -= 0.0005
        elif self.vy > 0:
            self.vy += 0.0005
         # 練習6
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct) # 練習5


class Gameover:
    def __init__(self, title, wh, goimg):
        pg.display.set_caption(title)#"Game Over"
        self.sfc = pg.display.set_mode(wh)#(1600, 900)
        self.rct = self.sfc.get_rect()
        self.go_sfc = pg.image.load(goimg)#"ex04/fig/game_over.png"
        self.go_rct = self.go_sfc.get_rect()
        self.rct.center = 800, 450

    def blit(self):
        self.sfc.blit(self.go_sfc, self.go_rct)


class shot:
    speed = -10
    def __init__(self, color, radius, koka_rect:Bird):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = koka_rect.reft
        self.rct.centery = koka_rect.up

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()


def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

def game_over():
    game = Gameover("Gameover", (1600, 900),"ex05/fig/game_over.png")
    game.blit()
    #時間
    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(0.2)

def main():
    global check_game
    # 練習1
    scr = Screen("負けるな！こうかとん", (1600, 900),"ex05/fig/pg_bg.jpg")
    # 練習3
    kkt = Bird("ex05/fig/6.png", 2.0, (900, 400))
    # 練習5
    bkd = Enemy("ex05/fig/bird_aoitori_bluebird.png", 0.1, (+1, +1), scr)

    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() # 練習2
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return
        kkt.update(scr)
        # 練習7
        bkd.update(scr)
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_LSHIFT]:
            ban = ((255, 0, 0), 10, (+1, +1), scr)
            ban.update()
        # 練習8
        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重なったら
            check_game = 1
            return
        #練習2
        pg.display.update() 
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    if check_game == 1: 
        game_over()
    pg.quit() # 初期化の解除
    sys.exit()
