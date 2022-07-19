import pygame as pg
import sys
import random

def bgm():
    # 音楽ファイルの読み込み
    pg.mixer.music.load("./fig/Floor_Beast.mp3") 
    pg.mixer.music.play(loops=-1, start=0.0)#ロードした音楽の再生

class Screen:
    def __init__(self,title,wh,image):
        pg.display.set_caption(title)
        self.sfc=pg.display.set_mode(wh)  #画面用Surface
        self.rct= self.sfc.get_rect()           #画面用Rect
        self.bgi_sfc=pg.image.load(image)   #背景画像用のSurface
        self.bgi_rct=self.bgi_sfc.get_rect()    #背景画像用のRect

    def blit(self):
        self.sfc.blit(self.bgi_sfc,self.bgi_rct)  #背景画像用Surfaceを画面用Surfaceに貼り付ける


class Wall1:
    def __init__(self,image:str,size:float,xy):#ラケット画像用のSurface
        self.sfc=pg.image.load(image)
        self.sfc= pg.transform.rotozoom(self.sfc,0,size)
        self.rct=self.sfc.get_rect()                   #ラケット画像用のRect
        self.rct.center=xy                        #ラケット画像の中心座標を設定する

    def blit(self,scr :Screen):
        scr.sfc.blit(self.sfc, self.rct) #ラケット画像の更新

    def update(self,scr:Screen):
        key_states= pg.key.get_pressed() #辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1    #key上が押されているならばy方向に-1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1    #key上が押されているならばy方向に+1

        if check_bound(self.rct,scr.rct) != (1,1):   #領域外なら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1    #key上が押されているならばy方向に+1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1    #key上が押されているならばy方向に-1
        self.blit(scr)


class Wall2:
    def __init__(self,image:str,size:float,xy):#ラケット画像用のSurface
        self.sfc=pg.image.load(image)
        self.sfc= pg.transform.rotozoom(self.sfc,0,size)
        self.rct=self.sfc.get_rect()                   #ラケット画像用のRect
        self.rct.center=xy                        #ラケット画像の中心座標を設定する

    def blit(self,scr :Screen):
        scr.sfc.blit(self.sfc, self.rct) #ラケット画像の更新

    def update(self,scr:Screen):
        key_states= pg.key.get_pressed() #辞書
        if key_states[pg.K_w]: 
            self.rct.centery -= 1    #key上が押されているならばy方向に-1
        if key_states[pg.K_s]:
            self.rct.centery += 1    #key上が押されているならばy方向に+1

        if check_bound(self.rct,scr.rct) != (1,1):   #領域外なら
            if key_states[pg.K_w]: 
                self.rct.centery += 1    #key上が押されているならばy方向に+1
            if key_states[pg.K_s]:
                self.rct.centery -= 1    #key上が押されているならばy方向に-1
        self.blit(scr)


class Ball:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) #ボール用のSurface
        pg.draw.circle(self.sfc, color, (size, size), size) #ボール用のSurfaceに円を描く
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct) #更新

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        self.blit(scr)    


class Bar:
    def __init__(self,image:str,size:float,xy):#中央障害物画像用のSurface
        self.sfc=pg.image.load(image)
        self.sfc= pg.transform.rotozoom(self.sfc,0,size)
        self.rct=self.sfc.get_rect()                   #中央障害物画像用のRect
        self.rct.center=xy                        #中央障害物画像の中心座標を設定する

    def blit(self,scr :Screen):
        scr.sfc.blit(self.sfc, self.rct) #中央障害物画像の更新

    def update(self, scr: Screen): #更新
        self.blit(scr)


class Score:
    def __init__(self, score1, score2):
        self.fonto = pg.font.Font(None,100)#フォント設定
        self.txt = self.fonto.render(f"{score1}    -    {score2}",
        True,(255,255,255))#点数表示

    def blit(self,scr:Screen):
        scr.sfc.blit(self.txt,(675,200)) #表示場所指定

    def update(self,scr:Screen):
        self.blit(scr) #更新


def main():
    global STATE,G_O
    score1=0
    score2=0
    clock = pg.time.Clock()
    scr = Screen("エアホッケー", (1600, 900), "fig/black.jpg")
    bar = Bar("fig/line.jpg",0.225, (800, 450))
    w1 = Wall1("fig/line_chain_gold.png",0.15, (1550, 450))
    w2 = Wall2("fig/line_chain_silver.png",0.15, (50, 450))
    ball = Ball((255,0,0), 30, (+3,+2), scr)
    sb = Score(score1,score2)

    while True:
        scr.blit()
        sb.blit(scr)

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        if w1.rct.colliderect(ball.rct): #衝突処理
            ball.vx *=-1

        if w2.rct.colliderect(ball.rct): #衝突処理
            ball.vx *=-1
        
        if bar.rct.colliderect(ball.rct): #衝突処理
            ball.vx *=-1

        if ball.rct.left < scr.rct.left: #スコア増やす
            score1+=1
            sb = Score(score1,score2)
            
        if ball.rct.right > scr.rct.right: #スコア増やす
            score2+=1
            sb = Score(score1,score2)
        
        if score1==5 or score2 == 5:
            return

        w1.update(scr)
        w2.update(scr)
        ball.update(scr)
        bar.update(scr)
        pg.display.update()
        clock.tick(1000)
    
def check_bound(rct, scr_rct):
    yoko, tate = +1, +1 #画面内：+1 / 画面外：-1
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    bgm()
    main()
    pg.quit()
    sys.exit()