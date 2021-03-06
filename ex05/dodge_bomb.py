import pygame as pg
import sys
import random

class Screen:
    def __init__(self,title,wh,image):
        pg.display.set_caption(title)
        self.sfc=pg.display.set_mode(wh)  #画面用Surface
        self.rct= self.sfc.get_rect()           #画面用Rect
        self.bgi_sfc=pg.image.load(image)   #背景画像用のSurface
        self.bgi_rct=self.bgi_sfc.get_rect()    #背景画像用のRect

    def blit(self):
        self.sfc.blit(self.bgi_sfc,self.bgi_rct)  #背景画像用Surfaceを画面用Surfaceに貼り付ける


class Bird:
    def __init__(self,image:str,size:float,xy):#こうかとん画像用のSurface
        self.sfc=pg.image.load(image)
        self.sfc= pg.transform.rotozoom(self.sfc,0,size)
        self.rct=self.sfc.get_rect()                   #こうかとん画像用のRect
        self.rct.center=xy                        #こうかとん画像の中心座標を設定する
        #screen_sfc.blit(kkimg_sfc,kkimg_rct)                 #こうかとん画像用Surfaceを画面用Surfaceに貼り付ける

    def blit(self,scr :Screen):
        scr.sfc.blit(self.sfc, self.rct)
        #screen_sfc.blit(kkimg_sfc,kkimg_rct)             #こうかとん画像の更新

    def update(self,scr:Screen):
        key_states= pg.key.get_pressed() #辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1    #key上が押されているならばy方向に-1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1    #key上が押されているならばy方向に+1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1    #key上が押されているならばx方向に-1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1    #key上が押されているならばx方向に+1
        #練習７
        if check_bound(self.rct,scr.rct) != (1,1):   #領域外なら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1    #key上が押されているならばy方向に+1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1    #key上が押されているならばy方向に-1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1    #key上が押されているならばx方向に+1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1    #key上が押されているならばx方向に-1
        self.blit(scr)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) #爆弾用のSurface
        pg.draw.circle(self.sfc, color, (size, size), size) #爆弾用のSurfaceに円を描く
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        # 練習5
        self.blit(scr)          


def main():
    global STATE,G_O
    clock = pg.time.Clock()
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd = Bomb((255,0,0), 10, (+1,+1), scr)

    while True:
        scr.blit()

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        kkt.update(scr)
        bkd.update(scr)
        if kkt.rct.colliderect(bkd.rct):
            return

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 #画面内：+1 / 画面外：-1
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()