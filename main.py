import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import subprocess

USER_FILE = "users.json"
CURRENT_USER_FILE = "current_user.json"
RPS_SCORE_FILE = "rpsScore.json"
RTT_SCORE_FILE = "rttScore.json"

def center_window(root, width=900, height=500): #CENTER WINDOW FUNCTION
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def load_scores(): #FILE HANDLING (load from file)
    try:
        with open(RPS_SCORE_FILE, "r") as rps_file:
            rps_scores = json.load(rps_file)
    except (FileNotFoundError, json.JSONDecodeError):
        rps_scores = {}

    try:
        with open(RTT_SCORE_FILE, "r") as rtt_file:
            rtt_scores = json.load(rtt_file)
    except (FileNotFoundError, json.JSONDecodeError):
        rtt_scores = {}

    return rps_scores, rtt_scores

def load_users(): #FILE HANDLING (load from file)
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users): #FILE HANDLING (load from file)
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

def save_current_user(username): #FILE HANDLING (load from file)
    with open(CURRENT_USER_FILE, "w") as file:
        json.dump({"username": username}, file)

def sign_up(): #SIGN UP FUNCTION
    def register():
        username = entry_username.get().strip()
        password = entry_password.get().strip()
        first_name = entry_first_name.get().strip()
        last_name = entry_last_name.get().strip()
        birthday = entry_birthday.get().strip()
        gender = gender_var.get()

        if not username or not password or not first_name or not last_name or not birthday or not gender:
            messagebox.showerror("Error", "All fields are required!")
            return

        users = load_users()
        if username in users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            users[username] = {
                "password": password,
                "first_name": first_name,
                "last_name": last_name,
                "birthday": birthday,
                "gender": gender
            }
            save_users(users)
            messagebox.showinfo("Success", "Account created successfully!")
            signup_window.destroy()

    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")

    screen_width = signup_window.winfo_screenwidth()
    screen_height = signup_window.winfo_screenheight()
    signup_window_width = 700
    signup_window_height = 400
    x = (screen_width // 2) - (signup_window_width // 2)
    y = (screen_height // 2) - (signup_window_height // 2)
    signup_window.geometry(f"{signup_window_width}x{signup_window_height}+{x}+{y}")

    frame = tk.Frame(signup_window)
    frame.pack(pady=50)

    tk.Label(frame, text="Username:", font="Courier").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_username = tk.Entry(frame)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame, text="Password:", font="Courier").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_password = tk.Entry(frame, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame, text="First Name:", font="Courier").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_first_name = tk.Entry(frame)
    entry_first_name.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(frame, text="Last Name:", font="Courier").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_last_name = tk.Entry(frame)
    entry_last_name.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame, text="Birthday (YYYY-MM-DD):", font="Courier").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_birthday = tk.Entry(frame)
    entry_birthday.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(frame, text="Gender:", font="Courier").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    gender_var = tk.StringVar(value="None")
    gender_frame = tk.Frame(frame)
    gender_frame.grid(row=5, column=1, padx=10, pady=5)

    tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", font="Courier").grid(row=0, column=0)
    tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", font="Courier").grid(row=0, column=1)
    tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other", font="Courier").grid(row=0, column=2)

    tk.Button(signup_window, text="Sign Up", command=register, font="Courier").pack(pady=20)

def sign_in(): #SIGN IN FUNCTION
    def check_credentials():
        username = entry_username.get().strip()
        password = entry_password.get().strip()

        users = load_users()
        if username in users and users[username]["password"] == password:
            save_current_user(username)
            messagebox.showinfo("Success", "Sign-in successful!")
            root.destroy()
            subprocess.run(["python", "menu.py"])
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    signin_window = tk.Toplevel(root)
    signin_window.title("Sign In")
    signin_window.geometry("300x200")

    screen_width = signin_window.winfo_screenwidth()
    screen_height = signin_window.winfo_screenheight()
    signin_window_width = 600
    signin_window_height = 200
    x = (screen_width // 2) - (signin_window_width // 2)
    y = (screen_height // 2) - (signin_window_height // 2)
    signin_window.geometry(f"{signin_window_width}x{signin_window_height}+{x}+{y}")

    tk.Label(signin_window, text="Username:", font="Courier").pack(pady=5)
    entry_username = tk.Entry(signin_window)
    entry_username.pack(pady=5)

    tk.Label(signin_window, text="Password:", font="Courier").pack(pady=5)
    entry_password = tk.Entry(signin_window, show="*")
    entry_password.pack(pady=5)

    tk.Button(signin_window, text="Sign In", command=check_credentials, font="Courier").pack(pady=10)

def view_all_records(): #VIEW ALL RECORDS FUNCTION
    users = load_users()
    rps_scores, rtt_scores = load_scores()

    records_window = tk.Toplevel(root)
    records_window.title("All User Records")
    records_window.geometry("500x400")

    tk.Label(records_window, text="Registered Users:", font=("Courier", 12, "bold")).pack(pady=5)

    for username, details in users.items():
        rps_score = rps_scores.get(username, "N/A")
        rtt_score = rtt_scores.get(username, "N/A")

        user_info = (
            f"Username: {username}\n"
            f"Full Name: {details['first_name']} {details['last_name']}\n"
            f"Birthday: {details['birthday']}\n"
            f"Gender: {details['gender']}\n"
            f"Rock Paper Scissors Score: {rps_score}\n"
            f"Best Reaction Time: {rtt_score:.3f} seconds"
        )

        tk.Label(records_window, text=user_info, justify="left", padx=10, pady=5, font="Courier").pack()

def search_record(): ##SEARCH RECORD FUNCTION
    def search():
        username = entry_username.get().strip()
        users = load_users()

        if username in users:
            details = users[username]
            user_info = f"Username: {username}\nFull Name: {details['first_name']} {details['last_name']}\nBirthday: {details['birthday']}\nGender: {details['gender']}"
            result_label.config(text=user_info)
        else:
            result_label.config(text="User not found!", font="Courier")

    search_window = tk.Toplevel(root)
    search_window.title("Search User Record")

    screen_width = search_window.winfo_screenwidth()
    screen_height = search_window.winfo_screenheight()
    search_window_width = 700
    search_window_height = 400
    x = (screen_width // 2) - (search_window_width // 2)
    y = (screen_height // 2) - (search_window_height // 2)
    search_window.geometry(f"{search_window_width}x{search_window_height}+{x}+{y}")

    frame = tk.Frame(search_window)
    frame.pack(pady=20)

    tk.Label(frame, text="Enter Username to Search:", font="Courier").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_username = tk.Entry(frame)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(frame, text="Search", command=search, font="Courier").grid(row=1, column=0, columnspan=2, pady=10)

    result_label = tk.Label(frame, text="", font=("Courier", 12), justify="left")
    result_label.grid(row=2, column=0, columnspan=2, pady=10)

def delete_user(): #DELETE USER FUNCTION
    def confirm_delete():
        username = entry_username.get().strip()
        users = load_users()
        rps_scores, rtt_scores = load_scores()

        if username in users:
            del users[username]
            rps_scores.pop(username, None)
            rtt_scores.pop(username, None)

            save_users(users)
            with open(RPS_SCORE_FILE, "w") as rps_file:
                json.dump(rps_scores, rps_file, indent=4)
            with open(RTT_SCORE_FILE, "w") as rtt_file:
                json.dump(rtt_scores, rtt_file, indent=4)

            messagebox.showinfo("Success", f"User '{username}' deleted successfully!")
            delete_window.destroy()
        else:
            messagebox.showerror("Error", "User not found!")

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete User")
    delete_window.geometry("400x200")

    tk.Label(delete_window, text="Enter Username to Delete:", font="Courier").pack(pady=10)
    entry_username = tk.Entry(delete_window)
    entry_username.pack(pady=5)

    tk.Button(delete_window, text="Delete User", command=confirm_delete, font="Courier", bg="red", fg="white").pack(pady=20)

def exit_main():
    root.destroy()

root = tk.Tk()
root.title("Main Menu")
center_window(root, 900, 500)
root.geometry("900x500")

bg_image = Image.open("img/space.gif")
bg_image = bg_image.resize((900, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

title_label = tk.Label(root, text="Welcome to DuoList!", font=("Courier", 20), bg="black", fg="white").pack(pady=50)

tk.Button(root, text="Sign Up", command=sign_up, font="Courier", width=20, bg="orange", fg="white").pack(pady=10)
tk.Button(root, text="Sign In", command=sign_in, font="Courier", width=20, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="View All Records", command=view_all_records, font="Courier", width=20, bg="purple", fg="white").pack(pady=10)
tk.Button(root, text="Search Record", command=search_record, font="Courier", width=20, bg="blue", fg="white").pack(pady=10)
tk.Button(root, text="Delete User", command=delete_user, font="Courier", width=20, bg="red", fg="white").pack(pady=10)
tk.Button(root, text="Exit", command=exit_main, font="Courier", width=20, bg="gray", fg="white").pack(pady=10)

root.mainloop()