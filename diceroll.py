import tkinter as tk
from PIL import Image, ImageTk
import random
import subprocess

class DiceRollGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roll Game")
        self.center_window(400, 400)

        # Load dice images
        self.dice_images = [ImageTk.PhotoImage(Image.open(f"img/dice{i}.png").resize((100, 100))) for i in range(1, 7)]
        
        self.bg_image = Image.open("img/space.gif")
        self.bg_image = self.bg_image.resize((400, 400))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(relwidth=1, relheight=1)

        self.roll_button = tk.Button(self.root, text="Roll Dice", font=("Courier", 14), bg="green", fg="white", width=20, command=self.roll_dice)
        self.roll_button.pack(pady=20)

        self.dice_label = tk.Label(self.root)
        self.dice_label.pack(pady=20)

        self.result_label = tk.Label(self.root, text="Roll the dice!", font=("Courier", 20), bg="black", fg="white")
        self.result_label.pack(pady=20)

        self.back_button = tk.Button(self.root, text="Back", font=("Courier", 14), bg="red", fg="white", width=10, command=self.go_back)
        self.back_button.pack(pady=20)

    def roll_dice(self):
        dice_result = random.randint(1, 6)
        self.result_label.config(text=f"Rolled: {dice_result}")
        self.dice_label.config(image=self.dice_images[dice_result - 1])

    def go_back(self):
        self.root.destroy()
        subprocess.run(["python", "menu.py"])

    def center_window(self, width=400, height=400):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceRollGame(root)
    root.mainloop()
