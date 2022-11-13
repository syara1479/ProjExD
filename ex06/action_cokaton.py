import tkinter as tk
import pygame as pg
import sys
from random import randint
import tkinter.messagebox as tkm

check_over = False
check_clear = False
Ground = 360
canJump = True
vy = 0 # y方向の速度
gr = 0.2 # 重力加速度

class Gamefinish:
    def __init__(self, title, wh, goimg):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.go_sfc = pg.image.load(goimg)
        self.go_rct = self.go_sfc.get_rect()
        self.rct.center = 800, 450

    def blit(self):
        self.sfc.blit(self.go_sfc, self.go_rct)


def check_bound(obj_rct, scr_rct):
    yoko = +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right or (200 < obj_rct.right and obj_rct.bottom > 370) or (350 < obj_rct.right and obj_rct.bottom > 320) or (500 < obj_rct.right and obj_rct.bottom > 270): 
        yoko = -1
    return yoko

def janp():
    global canJump, vy
    if canJump:
        canJump = False
        vy = -10 # 初速を与える

def game_clear():
    game = Gamefinish("Gameclear", (700, 400),"ex06/game_clear.png")
    game.blit()
    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(0.2)

def game_over():
    game = Gamefinish("Gameovar", (700, 400),"ex06/fig/game_over.png")
    game.blit()
    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(0.2)


def main():
    global gr, vy, canJump, Ground, check_clear, check_over
    pg.display.set_caption("アクションこうかとん")
    scrn_sfc = pg.display.set_mode((800, 480))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("ex06/IMG_3412.PNG")
    bg_rct = bg_sfc.get_rect()
    tori_sfc = pg.image.load("ex06/fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.left = 0
    tori_rct.centery = Ground

    clock = pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        #ゴールポールの描画
        pg.draw.rect(scrn_sfc,(255,255,255),(750,100,5,320))
        pg.draw.rect(scrn_sfc,(116,80,48),(730,400,45,20))
        #障害物(階段)の描画
        pg.draw.rect(scrn_sfc,(116,80,48),(200,370,150,50))
        pg.draw.rect(scrn_sfc,(116,80,48),(350,320,150,100))
        pg.draw.rect(scrn_sfc,(116,80,48),(500,270,150,150))
        #スライムの描画
        sura_sfc = pg.image.load("figge/sura.png")
        sura_sfc = pg.transform.rotozoom(sura_sfc, 0, 2.0)
        sura_rct = sura_sfc.get_rect()
        sura_rct.center = 400, 400   

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_SPACE]: # space でジャンプ
            janp()
        if key_lst[pg.K_LEFT]:
            tori_rct.centerx -=1
        if key_lst[pg.K_RIGHT]:
            tori_rct.centerx +=1

        #update
        if canJump == False:
            vy += gr
            tori_rct.bottom += vy
            if 200 < tori_rct.centerx < 350:
                if tori_rct.bottom > 370: # 地面についたら
                    tori_rct.bottom = 370
                    vy = 0
                    canJump = True
            elif 350 < tori_rct.centerx < 500:
                if tori_rct.bottom > 320: # 地面についたら
                    tori_rct.bottom = 320
                    vy = 0
                    canJump = True
            elif  500 < tori_rct.centerx < 650:
                if tori_rct.bottom > 270: # 地面についたら
                    tori_rct.bottom = 270
                    vy = 0
                    canJump = True
            else:
                if tori_rct.centery > Ground: # 地面についたら
                    tori_rct.centery = Ground
                    vy = 0
                    canJump = True

        yoko = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_lst[pg.K_LEFT]: 
                tori_rct.centerx += 1
            if key_lst[pg.K_RIGHT]:
                tori_rct.centerx -= 1

        scrn_sfc.blit(tori_sfc, tori_rct)
        if tori_rct.right > 750 and tori_rct.bottom > 100:
            check_clear = True
            return
        
        if tori_rct.colliderect(sura_rct):
            check_over = True
            return
        
        pg.display.update()
        clock.tick(800)

        
        
if __name__ == "__main__" :
    pg.init()
    main()
    if check_clear:
        game_clear()
    elif check_over:
        game_over()
    pg.quit()
    sys.exit()