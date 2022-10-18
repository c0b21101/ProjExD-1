import tkinter as tk

def key_down(event):
    global key
    key = event.keysys
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") # 練習1
    
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack() # 練習2
    
    tori = tk.PhotoImage(file="./fig/6.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori") # 練習3
    
    # 練習4
    key = "" #現在押されているキー
    
    root.bind("<KeyPress>", key_down) # 練習5
    
    root.mainloop()