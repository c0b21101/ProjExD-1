from ast import Delete
import tkinter as tk
import tkinter.messagebox as tkm
from turtle import right

root = tk.Tk()
root.title("tk")
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(num, f"{num}ボタンがクリックされました")
    entry.insert(tk.END, num)
    
def button_equal(event):
    eql = entry.get()
    res = eval(eql)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

entry = tk.Entry(root, width=10, font=(" ", 40), justify="right")
entry.grid(row=0, column=0, columnspan=3)

tate , yoko =1, 0
number = list(reversed(range(10)))
kigou = ["+"]

for n, i in enumerate(number + kigou , 1):    
    btn = tk.Button(root, text=f"{i}", font=(" ", 30), width=4, height=2)
    btn.grid(row=tate, column=yoko)
    yoko += 1
    if n % 3 == 0:
        tate += 1
        yoko = 0
    btn.bind("<1>", button_click)
btn = tk.Button(root, text=f"=", font=(" ", 30), width=4, height=2)
btn.grid(row=tate, column=yoko)
btn.bind("<1>", button_equal)

root.mainloop()