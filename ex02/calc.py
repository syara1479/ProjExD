from ast import Num
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn =event.widget
    num =btn["text"]
    entry.insert(tk.END, num)

root = tk.Tk()
root.geometry("300x700")

r, c = 0, 0 # r: 行を表す変数／c：列を表す変数

entry = tk.Entry(root, width=10, font=(", 40"), justify="right") # 練習4
entry.grid(row=0, column=0, columnspan=3)


r, c = 1, 0

for i ,num in enumerate(range(9, -1, -1), 1):

    button = tk.Button(root,
                        text = f"{num}",
                        font=("Times New Roman", 30),
                        width=4,
                        height=2)
    button.bind("<1>",button_click)
    button.grid(row = r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

    


root.mainloop()