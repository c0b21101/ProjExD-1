import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event): # 練習3
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num) # 練習5


def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res) # 練習7

def click_ac(event):
    entry.delete(0, tk.END)


root = tk.Tk() # 練習1
root.geometry("400x600")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right") # 練習4
entry.grid(row=0, column=0, columnspan=3)

tate, yoko = 2, 0 # r: 行を表す変数／c：列を表す変数
numbers = list(range(9, -1, -1))# 数字だけのリスト
operators = ["+", "-", "*", "/"] # 演算子だけのリスト
ac = ["%", "**"]
for i, num in enumerate(numbers, 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", click_number)
    btn.grid(row=tate, column=yoko)
    yoko += 1
    if i%3 == 0:
        tate += 1
        yoko = 0
        
tate_ac, yoko_ac = 1, 1
for i, num in enumerate(ac, 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2, bg="gray")
    btn.bind("<1>", click_number)
    btn.grid(row=tate_ac,column= yoko_ac)
    yoko_ac += 1  
         
tate_k, yoko_k = 1, 0
for i, num in enumerate(operators, 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2, bg="gray")
    btn.bind("<1>", click_number)
    btn.grid(row=tate_k, column=3 - yoko_k)
    tate_k += 1

keisan = ["00", "."]
for i, num in enumerate(keisan, 0):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", click_number)
    btn.grid(row=tate, column=yoko + i)
    
btn = tk.Button(root, text="=", font=("", 30), width=4, height=2, bg = "gray")
btn.bind("<1>", click_equal)
btn.grid(row=5, column=3)

btn = tk.Button(root, text="AC", font=("", 30), width=4, height=2, bg = "gray")
btn.bind("<1>", click_ac)
btn.grid(row=1, column=0)

root.mainloop()