from tkinter import *
from PIL import ImageTk, Image


path = "MonaLisa.png"
path2 = "best_output.bmp"
path3 = "test.png"

root = Tk()

img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def callback(e):
    img2 = ImageTk.PhotoImage(Image.open(path2))
    panel.configure(image=img2)
    panel.image = img2


root.bind("<Return>", callback)
root.mainloop()