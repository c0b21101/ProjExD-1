import tkinter as tk
import maze_maker as mm # 練習8
import random

# 練習5
def key_down(event):
    global key
    key = event.keysym

# 練習6    
def key_up(event):
    global key
    key = " "
    
# 練習7
def main_proc():
    global mx, my
    global cx, cy
    global tori, i
    if key == "Up":
        my -= 1
        i += 1
    if key == "Down":
        my += 1
        i += 1
    if key == "Left":
        mx -= 1
        i += 1
    if key == "Right":
        mx += 1
        i += 1
    if maze_lst[my][mx] == 0:
        cx, cy = mx * 100 + 50, my * 100 + 50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
            i += 1
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)
    tori = tk.PhotoImage(file=f"./fig/{koukaton[i]}")
    canv.create_image(cx, cy, image=tori, tag="tori")
    if i == 9:
            i = 0
 
 #敵の動き           
def teki_proc():
     global tx, ty
     global mmx, mmy
     mmx = random.randint(1, 14)
     mmy = random.randint(1, 14)
     if maze_lst[my][mx] == 0:
        tx, ty = mmx * 100 + 50, mmy * 100 + 50
        if maze_lst[my][mx] == 1:
            tx, ty = 100 + 50,  100 + 50
     canv.coords("teki", tx, ty)
     root.after(500, teki_proc)
     
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") # 練習1
    
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack() # 練習2
    
    # 練習9
    maze_lst = mm.make_maze(15, 9)

    # 練習10
    mm.show_maze(canv, maze_lst)
    
    #動かすたびにこうかとんが変わるプログラム
    koukaton = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png"]
    
    # 練習3
    i = 0
    tori = tk.PhotoImage(file=f"./fig/0.png")
    mx, my = 1, 1 #練習11
    cx, cy = mx * 100 + 50, my * 100 + 50
    canv.create_image(cx, cy, image=tori, tag="tori") 
    
    #敵の追加
    teki= tk.PhotoImage(file="./fig/hito.png")
    mmx, mmy = 1, 1
    tx, ty = mmx * 100 + 50, mmy * 1300 + 50
    canv.create_image(cx, cy, image=teki, tag="teki")
    
    # 練習4
    key = " " #現在押されているキー
    
    root.bind("<KeyPress>", key_down) # 練習5
    root.bind("<KeyRelease>", key_up) # 練習6
    
    # 練習7
    root.after(1000,main_proc())
    root.after(1000,teki_proc())
    
    root.mainloop()