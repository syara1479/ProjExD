import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
import random

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    global mx, my
    global life
    if key == "Up":
        if maze_list[my-1][mx] == 0: # 床なら
            my -= 1
        elif maze_list[my-1][mx] == 1: #壁なら
            life -= 1
    elif key == "Down":
        if maze_list[my+1][mx] == 0: # 床なら
            my += 1
        elif maze_list[my+1][mx] == 1:
            life -= 1
    elif key == "Left":
        if maze_list[my][mx-1] == 0: # 床なら
            mx -= 1
        elif maze_list[my][mx-1] == 1:
            life -= 1
    elif key == "Right":
        if maze_list[my][mx+1] == 0: # 床なら
            mx += 1
        elif maze_list[my][mx+1] == 1:
            life -=1

    cx, cy = mx*100+50, my*100+50
    canb.coords("tori", cx, cy)

    if mx == 13 and my == 7:
        tkm.showinfo("おめでとう", "ゴールだよ♡")
    elif life == 0:
        tkm.showinfo("脱出失敗", "残念！脱出失敗だよ♡")
    else:
        root.after(100, main_proc)

if __name__ == "__main__" :
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canb = tk.Canvas(root, width = 1500, height= 900, bg = "black")
    canb.pack()

    maze_list = mm.make_maze(15,9)
    mm.show_maze(canb,maze_list)

    tori1 = tk.PhotoImage(file="ex03/fig/1.png")
    tori2 = tk.PhotoImage(file="ex03/fig/2.png")
    tori3 = tk.PhotoImage(file="ex03/fig/3.png")
    tori4 = tk.PhotoImage(file="ex03/fig/4.png")
    tori5 = tk.PhotoImage(file="ex03/fig/5.png")
    tori6 = tk.PhotoImage(file="ex03/fig/6.png")
    
    mx, my =1, 1
    cx, cy = 300, 400

    a = random.randint(1,6)
    if a == 1:
        canb.create_image(cx, cy, image=tori1, tag="tori")
    elif a == 2: 
        canb.create_image(cx, cy, image=tori2, tag="tori")
    elif a == 3: 
        canb.create_image(cx, cy, image=tori3, tag="tori")
    elif a == 4: 
        canb.create_image(cx, cy, image=tori4, tag="tori")
    elif a == 5: 
        canb.create_image(cx, cy, image=tori5, tag="tori")
    elif a == 6: 
        canb.create_image(cx, cy, image=tori6, tag="tori")

    life = 5

    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()