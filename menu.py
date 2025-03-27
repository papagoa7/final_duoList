import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def reset():
    root.destroy()
    os.system("py main.py")

def tictactoe_game():
    root.destroy()
    os.system("py tictactoe.py")

def show_custom_message():
    popup = tk.Toplevel(root)
    popup.title("Warning!")
    popup.geometry("600x200")

    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    popup_width = 600
    popup_height = 200
    x = (screen_width // 2) - (popup_width // 2)
    y = (screen_height // 2) - (popup_height // 2)
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    label = tk.Label(popup, text="This is a two player game! Do you still want to continue?", font=("Courier", 12), wraplength=500)
    label.pack(pady=30)

    button_frame = tk.Frame(popup)
    button_frame.pack(pady=10)

    yes_button = tk.Button(button_frame, text="Yes", command=tictactoe_game, font=("Courier", 12), width=10, borderwidth=3)
    yes_button.pack(side=tk.LEFT, padx=10)

    no_button = tk.Button(button_frame, text="No", command=popup.destroy, font=("Courier", 12), width=10, borderwidth=3)
    no_button.pack(side=tk.LEFT, padx=10)

    popup.transient(root)
    popup.grab_set()

def rockpaperscissors_game():
    root.destroy()
    os.system("py rockpaperscissors.py")

def center_window(root, width=900, height=500):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def create_menu():
    global root

    title_label = tk.Label(root, text="Game Menu", font=("Courier", 18), bg="black", fg="white")
    title_label.pack(pady=50)

    tictactoe_button = tk.Button(root, text="Tic-Tac-Toe", font=("Courier", 14), width=30, borderwidth=5, command=show_custom_message)
    tictactoe_button.pack(pady=10)

    rockpaperscissors_button = tk.Button(root, text="Rock, Paper, Scissors", font=("Courier", 14), width=30, borderwidth=5, command=rockpaperscissors_game)
    rockpaperscissors_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", font=("Courier", 14), width=30, borderwidth=5, command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()

root = tk.Tk()
root.title("Game Menu")
center_window(root, 900, 500)
root.configure(bg="black")

bg_image = Image.open("img/space.gif")
bg_image = bg_image.resize((900, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

if __name__ == "__main__":
    create_menu()