import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os

USER_FILE = "users.json"
CURRENT_USER_FILE = "current_user.json"
RPS_SCORE_FILE = "rpsScore.json"

def center_window(root, width=900, height=500):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def load_scores():
    try:
        with open(RPS_SCORE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def load_users():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

def save_current_user(username):
    with open(CURRENT_USER_FILE, "w") as file:
        json.dump({"username": username}, file)

logged_in = False  # Track user authentication

def sign_up():
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
<<<<<<< HEAD

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

def sign_in():
    def check_credentials():
        username = entry_username.get().strip()
        password = entry_password.get().strip()

        users = load_users()
        if username in users and users[username]["password"] == password:
            save_current_user(username)
            messagebox.showinfo("Success", "Sign-in successful!")
            root.destroy()
            os.system("C:/Users/Nicole/AppData/Local/Programs/Python/Python313/python.exe menu.py")
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

def view_all_records():
    users = load_users()
    scores = load_scores()
    records_window = tk.Toplevel(root)
    records_window.title("All User Records")
    records_window.geometry("500x400")

    tk.Label(records_window, text="Registered Users:", font=("Courier", 12, "bold")).pack(pady=5)

    for username, details in users.items():
        user_score = scores.get(username, 0)
        user_info = f"Username: {username}\nFull Name: {details['first_name']} {details['last_name']}\nBirthday: {details['birthday']}\nGender: {details['gender']}\nRock Paper Scissors: {user_score}"
        tk.Label(records_window, text=user_info, justify="left", padx=10, pady=5, font="Courier").pack()

def search_record():
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

def exit_main():
    root.destroy()

=======
    signup_window.geometry("420x300")
    signup_window.configure(bg="#f0f0f0")
    
    frame = ttk.Frame(signup_window, padding=10)
    frame.pack(fill=tk.BOTH, expand=True)
    
    ttk.Label(frame, text="First Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_first = ttk.Entry(frame)
    entry_first.grid(row=0, column=1, padx=10, pady=5)
    
    ttk.Label(frame, text="Middle Name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_middle = ttk.Entry(frame)
    entry_middle.grid(row=1, column=1, padx=10, pady=5)
    
    ttk.Label(frame, text="Last Name:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_last = ttk.Entry(frame)
    entry_last.grid(row=2, column=1, padx=10, pady=5)
    
    ttk.Label(frame, text="Birthday (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_bday = ttk.Entry(frame)
    entry_bday.grid(row=3, column=1, padx=10, pady=5)
    
    ttk.Label(frame, text="Gender:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    gender_var = tk.StringVar()
    gender_frame = ttk.Frame(frame)
    gender_frame.grid(row=4, column=1, columnspan=2, pady=5)
    
    ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side=tk.LEFT, padx=5)
    ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side=tk.LEFT, padx=5)
    ttk.Radiobutton(gender_frame, text="Prefer not to say", variable=gender_var, value="Prefer not to say").pack(side=tk.LEFT, padx=5)
    
    ttk.Button(frame, text="Save", command=save).grid(row=5, column=0, columnspan=2, pady=10)

def sign_in():
    def authenticate():
        global logged_in
        first_name = entry_first.get()
        last_name = entry_last.get()
        birthday = entry_bday.get()
        records = load_records()
        
        for record in records:
            if (record['first_name'] == first_name and record['last_name'] == last_name and record['birthday'] == birthday):
                logged_in = True
                messagebox.showinfo("Success", "Sign-in successful! You can now view records.")
                sign_in_window.destroy()
                return
        messagebox.showerror("Error", "Record not found. Please try again.")
    
    sign_in_window = tk.Toplevel(root)
    sign_in_window.title("Sign In")
    sign_in_window.geometry("300x250")
    
    ttk.Label(sign_in_window, text="First Name:").pack(pady=5)
    entry_first = ttk.Entry(sign_in_window)
    entry_first.pack(pady=5)
    
    ttk.Label(sign_in_window, text="Last Name:").pack(pady=5)
    entry_last = ttk.Entry(sign_in_window)
    entry_last.pack(pady=5)
    
    ttk.Label(sign_in_window, text="Birthday (YYYY-MM-DD):").pack(pady=5)
    entry_bday = ttk.Entry(sign_in_window)
    entry_bday.pack(pady=5)
    
    ttk.Button(sign_in_window, text="Sign In", command=authenticate).pack(pady=10)

def view_records():
    if not logged_in:
        messagebox.showerror("Error", "You must sign in first to view records.")
        return
    records = load_records()
    view_window = tk.Toplevel(root)
    view_window.title("All Records")
    view_window.geometry("400x300")
    
    frame = ttk.Frame(view_window)
    frame.pack(fill=tk.BOTH, expand=True)
    
    text_box = tk.Text(frame, wrap=tk.WORD, height=15, width=50)
    text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar = ttk.Scrollbar(frame, command=text_box.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_box.config(yscrollcommand=scrollbar.set)
    
    if not records:
        text_box.insert(tk.END, "No records found.\n")
    else:
        for record in records:
            text_box.insert(tk.END, f"{record['first_name']} {record['middle_name']} {record['last_name']} - {record['birthday']} - {record['gender']}\n")

>>>>>>> 50b11d6dd100dc79a9c611deca236f76806eaa07
root = tk.Tk()
root.title("Main Menu")
center_window(root, 900, 500)
root.geometry("900x500")

bg_image = Image.open("img/space.gif")
bg_image = bg_image.resize((900, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

<<<<<<< HEAD
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)
=======
ttk.Button(menu_frame, text="Sign Up", command=sign_up).grid(row=0, column=0, padx=10)
ttk.Button(menu_frame, text="Sign In", command=sign_in).grid(row=0, column=1, padx=10)
ttk.Button(menu_frame, text="View All Records", command=view_records).grid(row=0, column=2, padx=10)
ttk.Button(menu_frame, text="Exit", command=root.quit).grid(row=0, column=3, padx=10)
>>>>>>> 50b11d6dd100dc79a9c611deca236f76806eaa07

title_label = tk.Label(root, text="Welcome to DuoList!", font=("Courier", 20), bg="black", fg="white").pack(pady=60)

tk.Button(root, text="Sign Up", command=sign_up, font="Courier", width=20, bg="black", fg="white").pack(pady=10)
tk.Button(root, text="Sign In", command=sign_in, font="Courier", width=20, bg="black", fg="white").pack(pady=10)
tk.Button(root, text="View All Records", command=view_all_records, font="Courier", width=20, bg="black", fg="white").pack(pady=10)
tk.Button(root, text="Search Record", command=search_record, font="Courier", width=20, bg="black", fg="white").pack(pady=10)
tk.Button(root, text="Exit", command=exit_main, font="Courier", width=20, bg="black", fg="white").pack(pady=10)

root.mainloop()