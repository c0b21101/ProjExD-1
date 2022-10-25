import pygame as pg
import sys

def main():
    #練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    bg_sfc = pg.image.load("./fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    
    while True: #無限ループの処理
        scrn_sfc.blit(bg_sfc, bg_rct) #練習1
        pg.display.update() #練習1
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        #2秒間表示する
        clock = pg.time.Clock()
        clock.tick(0.2)
    

    
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()