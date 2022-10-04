import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right

root = tk.Tk()
root.title("tk")
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{txt}ボタンがクリックされました")

entry = tk.Entry(root, width=10, font=("Times New Roman", 40), justify="right")
entry.grid(row=0, column=0, columnspan=3)

tate = 1
yoko = 0

for n, i in enumerate(reversed(range(10)), 1):    
    btn = tk.Button(root, text=f"{i}", font=("Times New Roman", 30), width=4, height=2)
    btn.grid(row=tate, column=yoko)
    yoko += 1
    if n % 3 == 0:
        tate += 1
        yoko = 0
    btn.bind("<1>", button_click)
    
root.mainloop()