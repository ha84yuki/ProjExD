import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm
import datetime

st=datetime.datetime.now()

def main():
    clock=pg.time.Clock()
    #練習１
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc=pg.display.set_mode((1600,900))  #画面用Surface
    screen_rct= screen_sfc.get_rect()           #画面用Rect
    bgimg_sfc=pg.image.load("fig/pg_bg.jpg")   #背景画像用のSurface
    bgimg_rct=bgimg_sfc.get_rect()               #背景画像用のRect
    screen_sfc.blit(bgimg_sfc,bgimg_rct)             #背景画像用Surfaceを画面用Surfaceに貼り付ける

    #練習３
    num= random.randint(0,9)
    kkimg_sfc=pg.image.load(f"fig/{num}.png")             #こうかとん画像用のSurface
    kkimg_sfc= pg.transform.rotozoom(kkimg_sfc,0,2.0)
    kkimg_rct=kkimg_sfc.get_rect()                   #こうかとん画像用のRect
    kkimg_rct.center=900,400                        #こうかとん画像の中心座標を設定する
    screen_sfc.blit(kkimg_sfc,kkimg_rct)                 #こうかとん画像用Surfaceを画面用Surfaceに貼り付ける

    #練習５
    bmimg_sfc = pg.Surface((20,20))   #Surface
    bmimg_sfc.set_colorkey((0,0,0,))#爆弾用のSurface
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10,10), 10)  #爆弾用のSurfaceに円を描く
    bmimg_rct=bmimg_sfc.get_rect()                       #爆弾用Rect
    bmimg_rct2=bmimg_sfc.get_rect()   
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    bmimg_rct2.centerx = random.randint(0, screen_rct.width)
    bmimg_rct2.centery = random.randint(0, screen_rct.height) 
    vx,vy= +1,+1
    vxx,vyy=+1,+1
    
    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)               #背景画像用Surfaceを画面用Surfaceに貼り付ける
        screen_sfc.blit(kkimg_sfc, kkimg_rct)
        #練習２
        for event in pg.event.get():
            if event.type==pg.QUIT: return
        
        #練習４
        key_states= pg.key.get_pressed()
        if key_states[pg.K_UP]==True: kkimg_rct.centery -= 1       #key上が押されているならばy方向に-1
        if key_states[pg.K_DOWN]==True: kkimg_rct.centery += 1     #key上が押されているならばy方向に+1
        if key_states[pg.K_LEFT]==True: kkimg_rct.centerx -= 1     #key上が押されているならばx方向に-1
        if key_states[pg.K_RIGHT]==True: kkimg_rct.centerx += 1    #key上が押されているならばx方向に+1
        if check_bound(kkimg_rct,screen_rct)!= (1,1):   #領域外なら
            if key_states[pg.K_UP]==True: kkimg_rct.centery += 1       #key上が押されているならばy方向に-1
            if key_states[pg.K_DOWN]==True: kkimg_rct.centery -= 1     #key上が押されているならばy方向に+1
            if key_states[pg.K_LEFT]==True: kkimg_rct.centerx += 1     #key上が押されているならばx方向に-1
            if key_states[pg.K_RIGHT]==True: kkimg_rct.centerx -= 1 
        screen_sfc.blit(kkimg_sfc,kkimg_rct)             #こうかとん画像の更新

        #練習６
        bmimg_rct.move_ip(vx,vy)
        bmimg_rct2.move_ip(vxx,vyy)
        screen_sfc.blit(bmimg_sfc,bmimg_rct)                     #爆弾用のSurfaceを画面用Surfaceに貼り付ける
        screen_sfc.blit(bmimg_sfc,bmimg_rct2)

        #練習５
        screen_sfc.blit(bmimg_sfc,bmimg_rct)

        #練習７
        x,y = check_bound(bmimg_rct,screen_rct)
        vx*=x
        vy*=y
        x,y = check_bound(bmimg_rct2,screen_rct)
        vxx*=x
        vyy*=y

        ed= datetime.datetime.now()
        tmr = (ed-st).seconds

        fonto = pg.font.Font(None,80)
        txt = fonto.render(str(tmr), True,(0,0,0))
        screen_sfc.blit(txt,(100,100))

        #練習８
        if kkimg_rct.colliderect(bmimg_rct) or kkimg_rct.colliderect(bmimg_rct2): 
            kkimg_sfc=pg.image.load("fig/bakuhatsu.png")
            screen_sfc.blit(kkimg_sfc, kkimg_rct)
            tkm.showinfo(root,f"Game over \n{tmr}秒生きました")
            return

        pg.display.update()                           #画面の更新
        clock.tick(1000)

#練習７
def check_bound(rct,scr_rct):#画面内：+1 / 画面外：-1
    x,y=+1,+1
    if scr_rct.left >rct.left or rct.right>scr_rct.right : x=-1
    if scr_rct.top >rct.top or rct.bottom>scr_rct.bottom : y=-1
    return x,y
    
if __name__=="__main__":
    root =tk.Tk()
    pg.init()
    main()
    pg.quit()
    sys.exit()