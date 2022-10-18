import tkinter as tk




if __name__ == "__main__" :
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canb = tk.Canvas(root, width = 1500, height= 900, bg = "black")

    tori = tk.PhotoImage(file="ex03/fig/5.png")
    cx, cy = 300, 400
    canb.create_image(cx, cy, image=tori, tag="tori")

    key = ""

    canb.pack()
    root.mainloop()