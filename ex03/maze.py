import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy
    global mx, my
    if key == "Up":
        my -= 1
    elif key == "Down":
        my += 1
    elif key == "Left":
        mx -= 1
    elif key == "Right":
        mx += 1

    cx, cy = mx*100+50, my*100+50

    if maze_list[my][mx] == 0: # 床なら
        cx, cy = mx*100+50, my*100+50
    else: # 壁なら
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1    

    canb.coords("tori", cx, cy)

    root.after(100, main_proc)




if __name__ == "__main__" :
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canb = tk.Canvas(root, width = 1500, height= 900, bg = "black")
    canb.pack()

    maze_list = mm.make_maze(15,9)
    mm.show_maze(canb,maze_list)

    tori = tk.PhotoImage(file="ex03/fig/5.png")
    mx, my =1, 1
    cx, cy = 300, 400
    canb.create_image(cx, cy, image=tori, tag="tori")

    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()


    

    root.mainloop()