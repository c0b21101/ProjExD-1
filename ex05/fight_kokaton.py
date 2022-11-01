import pygame as pg
import sys
from random import randint


class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
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
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Bomb:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)
    
    #爆弾の加速の実装
    def speed(self, s, x_s, y_s):
        if s % 1000 == 0:
            self.vx *= x_s
            self.vy *= y_s
  
            
class Text:
    def __init__(self, size, txt, color, xy):
        self.font = pg.font.Font(None, size)
        self.txt = self.font.render(txt, True, color)
        self.x, self.y = xy
        
    def blit(self, scr:Screen):
        scr.sfc.blit(self.txt, (self.x, self.y))
  
        
class Music:
    def __init__(self,m_faile):
        pg.mixer.init(frequency = 44100)    # 初期設定
        pg.mixer.music.load(m_faile)     # 音楽ファイルの読み込み
        pg.mixer.music.play(1)              # 再生の終了
        for event in pg.event.get(): # 練習2
            if event.type == pg.K_SPACE:
                pg.mixer.music.stop()
                return 0

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

def main():
    # 練習1
    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # 練習3
    kkt = Bird("fig/6.png", 2.0, (900, 400))

    # 練習5
    bkd1 = Bomb((255, 0, 0), 10, (+1, +1), scr)
    
    #爆弾を増やす
    bkd2 = Bomb((0, 0, 255), 10, (+1, +1), scr)
    
    #音楽の実装
    Music("./fig/BGM.mp3")
    
    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        # 練習4
        kkt.update(scr)
        
        # 練習7
        bkd1.update(scr)
        
        #爆弾の数を増やす機能の実装
        bkd2.update(scr)
        
        #速度変化の実装
        s = pg.time.get_ticks()
        bkd1.speed(s, 1.1, 1.1)
        bkd2.speed(s, 1.05, 1.05)
        
        #タイムの実装
        time = Text(80, str(s/1000), "Black", (50, 50))
        time.blit(scr)
        
        # 練習8
        if kkt.rct.colliderect(bkd1.rct): # こうかとんrctが爆弾rctと重なったら
             return
        if kkt.rct.colliderect(bkd2.rct): # こうかとんrctが爆弾rctと重なったら
             return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()