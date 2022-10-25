import pygame as pg
import sys
from random import randint

check_game = 0

def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

def game_over():
    pg.display.set_caption("Game Over")
    scrn_sfc = pg.display.set_mode((1600, 900))
    #画像
    go_sfc = pg.image.load("ex04/fig/game_over.png")
    go_rct = go_sfc.get_rect()
    go_rct.center = 800, 450
    scrn_sfc.blit(go_sfc, go_rct)
    #時間
    pg.display.update()
    clock = pg.time.Clock()
    clock.tick(0.2)

def main():
    check = -1 #keyかカーソルか判定するための変数
    global check_game#gameoverしたか判定するグローバル変数
    
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("ex04/fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    #練習3
    tori_sfc = pg.image.load("ex04/fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    #練習5
    bomb_sfc = pg.Surface((20,20)) #空のサーフェイス
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, ( 255, 0, 0), (10,10), 10)#円を描く
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx, bomb_rct.centery = randint(0, scrn_rct.width), randint(0, scrn_rct.height)

    #練習6
    vx, vy = 1, 1

    #練習2
    clock = pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_LSHIFT]:
            check = -1
        if key_lst[pg.K_RSHIFT]:
            check = 1
        #練習4
        if check == 1: 
            if key_lst[pg.K_UP]:
                tori_rct.centery -=1
            if key_lst[pg.K_DOWN]:
                tori_rct.centery +=1
            if key_lst[pg.K_LEFT]:
                tori_rct.centerx -=1
            if key_lst[pg.K_RIGHT]:
                tori_rct.centerx +=1
        if check == -1:
            tori_rct.centerx, tori_rct.centery = pg.mouse.get_pos()

        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_lst[pg.K_LEFT]: 
                tori_rct.centerx += 1
            if key_lst[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_lst[pg.K_UP]: 
                tori_rct.centery += 1
            if key_lst[pg.K_DOWN]:
                tori_rct.centery -= 1       
        scrn_sfc.blit(tori_sfc, tori_rct)#練習3
        yoko, tate = check_bound(bomb_rct, bg_rct)
        vx *= yoko
        vy *= tate
        #加速機構
        if vx < 0:
            vx -= 0.0005
        elif vx > 0:
            vx += 0.0005
        if vy < 0:
            vy -= 0.0005
        elif vy > 0:
            vy += 0.0005
        #練習6
        bomb_rct.move_ip(vx, vy)
        #練習5         
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        # 練習8
        if tori_rct.colliderect(bomb_rct): # こうかとんrctが爆弾rctと重なったら
            check_game = 1
            return
        pg.display.update()
        clock.tick(1000)

if __name__ =="__main__":
    pg.init()
    main()
    if check_game == 1: 
        game_over()
    pg.quit()
    sys.exit()