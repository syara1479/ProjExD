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
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20

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
    cx, cy = 300, 400
    canb.create_image(cx, cy, image=tori, tag="tori")

    key = ""

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()


    

    root.mainloop()