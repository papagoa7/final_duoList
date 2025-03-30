import tkinter as tk
import time
import random
import os
import json
from PIL import Image, ImageTk

RTT_SCORE_FILE = "rttScore.json"
CURRENT_USER_FILE = "current_user.json"

def load_current_user():
    try:
        with open(CURRENT_USER_FILE, "r") as file:
            data = json.load(file)
            return data.get("username")
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_current_user(username):
    with open(CURRENT_USER_FILE, "w") as file:
        json.dump({"username": username}, file)

def load_score():
    global current_user
    if current_user is None:
        return None
    try:
        with open(RTT_SCORE_FILE, "r") as file:
            data = json.load(file)
            return data.get(current_user, None)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_score():
    global current_user, best_time
    if current_user is None or best_time is None:
        return
    try:
        with open(RTT_SCORE_FILE, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data[current_user] = best_time

    with open(RTT_SCORE_FILE, "w") as file:
        json.dump(data, file)

current_user = load_current_user()
if current_user is None:
    current_user = "Guest"
    save_current_user(current_user)
best_time = load_score()

def start_test():
    start_button.config(state=tk.DISABLED)
    result_label.config(text="Wait for it...")
    root.after(random.randint(2000, 5000), show_button)

def show_button():
    global start_time
    test_button.config(bg="green", state=tk.NORMAL)
    result_label.config(text="Click now!")
    start_time = time.time()

def check_reaction():
    global best_time
    reaction_time = time.time() - start_time
    test_button.config(bg="gray", state=tk.DISABLED)
    start_button.config(state=tk.NORMAL)

    if best_time is None or reaction_time < best_time:
        best_time = reaction_time
        best_label.config(text=f"Best Time: {best_time:.3f} seconds")
        save_score()

    result_label.config(text=f"Reaction time: {reaction_time:.3f} seconds")

def center_window(root, width=900, height=500):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def go_back():
    root.destroy()
    os.system("C:/Users/Nicole/AppData/Local/Programs/Python/Python313/python.exe menu.py")

root = tk.Tk()
root.title("Reaction Time Test")
center_window(root, 900, 500)

bg_image = Image.open("img/moon.png")
bg_image = bg_image.resize((900, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

back_button = tk.Button(root, text="Back", font=("Courier", 12), width=10, command=go_back, bg="black", fg="white")
back_button.place(x=10, y=10)

start_button = tk.Button(root, text="Start", font=("Courier", 12), bg="black", fg="white", width=10, borderwidth=5, command=start_test)
start_button.pack(pady=50)

test_button = tk.Button(root, text="Click me!", font=("Courier", 18), bg="gray", state=tk.DISABLED, width=30, height=3, borderwidth=10, command=check_reaction)
test_button.pack(pady=40)

result_label = tk.Label(root, text="Press 'Start' to begin", font=("Courier", 14), bg="black", fg="white")
result_label.pack(pady=20)

best_label = tk.Label(root, text=f"Best Time: {best_time:.3f} seconds" if best_time else "Best Time: N/A", font=("Courier", 14), bg="black", fg="white")
best_label.pack()

root.mainloop()
