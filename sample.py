import tkinter as tk
from PIL import Image, ImageTk

def create_window():
    root = tk.Tk()
    root.title("Tkinter Background Image")
    root.geometry("800x500")

    bg_image = Image.open("img/space.gif")
    bg_image = bg_image.resize((800, 500))
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    root.mainloop()

create_window()
