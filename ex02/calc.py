#電卓のプログラム
import tkinter as tk
import tkinter.messagebox as tkm
import math
import numpy as np

#ボタンのクリックに関する関数
def button_click(event):
    btn =event.widget
    num =btn["text"]
    entry.insert(tk.END, num)

def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res) # 練習7

def click_cler(event):
    entry.delete(0, tk.END)


def click_sin(event):
     eqn = int(entry.get())
     rad = np.deg2rad(eqn)
     res = math.sin(rad)
     entry.delete(0, tk.END)
     entry.insert(tk.END, res)


root = tk.Tk()
root.geometry("600x700")

r, c = 0, 0 # r: 行を表す変数／c：列を表す変数

entry = tk.Entry(root, 
                 width=10, 
                 font=(", 40"), 
                 justify="right") # 練習4
#entry.insert(tk.END, "0")
entry.grid(row=0, 
           column=0, 
           columnspan=3)


r, c = 1, 0

numbers = list(range(9, -1, -1)) # 数字だけのリスト
operators = ["+","-", "*","/"] # 演算子だけのリスト
SP_operators = ["(", ")", "."]

for i, num in enumerate(numbers, 1):

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

r = 1
for j, num2 in enumerate(operators, 1):

    button = tk.Button(root,
                        text = f"{num2}",
                        font=("Times New Roman", 30),
                        bg="orange",
                        width=4,
                        height=2)
    button.bind("<1>",button_click)
    button.grid(row = r, column=3)
    r += 1

r = 1
for j, num2 in enumerate(SP_operators, 1):

    button = tk.Button(root,
                        text = f"{num2}",
                        font=("Times New Roman", 30),
                        bg="orange",
                        width=4,
                        height=2)
    button.bind("<1>",button_click)
    button.grid(row = r, column=4)
    r += 1
    

btn = tk.Button(root, text=f"=", font=("", 30), width=8, height=2)
btn.bind("<1>", click_equal)
btn.grid(row=r, column=c, columnspan=2)

btn = tk.Button(root, text=f"C", font=("", 30),bg="red", width=4, height=2)
btn.bind("<1>", click_cler)
btn.grid(row=4, column=4)

btn = tk.Button(root, text=f"sin", font=("", 30),bg="red", width=4, height=2)
btn.bind("<1>", click_sin)
btn.grid(row=4, column=5)


root.mainloop()