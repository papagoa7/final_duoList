import tkinter as tk
import random
import time
import os
from PIL import Image, ImageTk

def show_rules():
    popup = tk.Toplevel(root)
    popup.title("Rules")
    popup.geometry("600x200")

    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    popup_width = 600
    popup_height = 200
    x = (screen_width // 2) - (popup_width // 2)
    y = (screen_height // 2) - (popup_height // 2)
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    label = tk.Label(
        popup,
        text="You'll be playing against a Computer! Once the countdown says to shoot, choose Rock, Paper, or Scissors!",
        font=("Courier", 12),
        wraplength=500)

    label.pack(pady=30)

    button_frame = tk.Frame(popup)
    button_frame.pack(pady=10)

    go_button = tk.Button(button_frame, text="Got it!", command=popup.destroy, font=("Courier", 12), width=10, borderwidth=3)
    go_button.pack(side=tk.LEFT, padx=10)

    popup.transient(root)
    popup.grab_set()

def start_game():
    disable_buttons()
    countdown_phrases = ["Rock...", "Paper...", "Scissors..."]
    for phrase in countdown_phrases:
        result_label.config(text=phrase, bg="black", fg="white")
        root.update()
        time.sleep(1)
    result_label.config(text="Shoot!", bg="black", fg="white")
    enable_buttons()

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}", bg="black", fg="white")
    disable_buttons()

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def center_window(root, width=900, height=500):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def enable_buttons():
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)

def disable_buttons():
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)

def go_back():
    root.destroy()
    os.system("py menu.py")

root = tk.Tk()
root.title("Rock Paper Scissors")
center_window(root, 900, 500)
root.configure(bg="black")
show_rules()

bg_image = Image.open("img/mars.jpg")
bg_image = bg_image.resize((900, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

back_button = tk.Button(root, text="Back", font=("Courier", 12), width=10, command=go_back, bg="black", fg="white")
back_button.place(x=10, y=10)

start_button = tk.Button(root, text="Start", font=("Courier", 12), width=10, command=start_game, bg="black", fg="white")
start_button.pack(pady=50)

button_frame = tk.Frame(root, bg="white")
button_frame.pack()

rock_img = Image.open("img/rock.png").resize((200, 200))
paper_img = Image.open("img/paper.png").resize((200, 200))
scissors_img = Image.open("img/scissor.png").resize((200, 200))

rock_photo = ImageTk.PhotoImage(rock_img)
paper_photo = ImageTk.PhotoImage(paper_img)
scissors_photo = ImageTk.PhotoImage(scissors_img)

rock_button = tk.Button(button_frame, image=rock_photo, command=lambda: play("Rock"), bg="orange", activebackground="black", borderwidth=10, )
paper_button = tk.Button(button_frame, image=paper_photo, command=lambda: play("Paper"), bg="orange", activebackground="black", borderwidth=10)
scissors_button = tk.Button(button_frame, image=scissors_photo, command=lambda: play("Scissors"), bg="orange", activebackground="black", borderwidth=10)

rock_button.grid(row=0, column=0, padx=0, pady=0)
paper_button.grid(row=0, column=1, padx=0, pady=0)
scissors_button.grid(row=0, column=2, padx=0, pady=0)

disable_buttons()

result_label = tk.Label(root, text="", font=("Courier", 18), bg="black", fg="white")
result_label.pack(pady=30)

root.mainloop()
