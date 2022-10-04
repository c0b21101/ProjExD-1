import tkinter as tk

root = tk.Tk()
root.title("tk")
root.geometry("300x500")

tate = 0
yoko = 0

for n, i in enumerate(reversed(range(10)), 1):    
    btn = tk.Button(root, text=f"{i}", font=("Times New Roman", 30), width=4, height=2)
    btn.grid(row=tate, column=yoko)
    yoko += 1
    if n % 3 == 0:
        tate += 1
        yoko = 0
    
    
root.mainloop()