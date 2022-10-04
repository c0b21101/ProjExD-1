import tkinter as tk
import tkinter.messagebox as tkm



root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")
    
#ラベルのクラス
label = tk.Label(root, 
                 text="らべるを書いてみた件",
                 font=("Ricty Diminished", 30),
                 )
label.pack()

#入力のクラス
entry = tk.Entry(width=30)
entry.insert(tk.END, "fugapiyo")
entry.pack()

#ボタンのクラス
button = tk.Button(root, text="押すな",)
button.bind("<1>", button_click)
button.pack()

root.mainloop()