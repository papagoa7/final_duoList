#Sign-up, View all records, Search a record, Exit
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# File for data persistence
DATA_FILE = "data.json"

# Load existing records
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump([], file)

def load_records():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_records(records):
    with open(DATA_FILE, "w") as file:
        json.dump(records, file, indent=4)

def sign_up():
    def save():
        first_name = entry_first.get()
        middle_name = entry_middle.get()
        last_name = entry_last.get()
        birthday = entry_bday.get()
        gender = gender_var.get()
        
        if not all([first_name, last_name, birthday, gender]):
            messagebox.showerror("Error", "All fields except middle name are required!")
            return

        new_record = {
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "birthday": birthday,
            "gender": gender
        }
        
        records = load_records()
        records.append(new_record)
        save_records(records)
        messagebox.showinfo("Success", "Record saved successfully!")
        signup_window.destroy()
    
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("400x300")
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
    
    ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side=tk.LEFT)
    ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side=tk.LEFT)
    ttk.Radiobutton(gender_frame, text="Prefer not to say", variable=gender_var, value="Prefer not to say").pack(side=tk.LEFT)
    
    ttk.Button(frame, text="Save", command=save).grid(row=5, column=0, columnspan=2, pady=10)

def view_records():
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

def search_record():
    def search():
        query = entry_search.get().lower()
        records = load_records()
        results = [r for r in records if query in r['first_name'].lower() or query in r['last_name'].lower()]
        
        result_window = tk.Toplevel(search_window)
        result_window.title("Search Results")
        
        text_box = tk.Text(result_window, wrap=tk.WORD, height=10, width=50)
        text_box.pack()
        
        if not results:
            text_box.insert(tk.END, "No matching records found.\n")
        else:
            for record in results:
                text_box.insert(tk.END, f"{record['first_name']} {record['middle_name']} {record['last_name']} - {record['birthday']} - {record['gender']}\n")
    
    search_window = tk.Toplevel(root)
    search_window.title("Search Record")
    tk.Label(search_window, text="Enter First or Last Name:").pack()
    entry_search = ttk.Entry(search_window)
    entry_search.pack()
    ttk.Button(search_window, text="Search", command=search).pack()

root = tk.Tk()
root.title("User Records")
root.geometry("500x200")
root.configure(bg="#e6e6fa")

menu_frame = ttk.Frame(root, padding=20)
menu_frame.pack(pady=20)

ttk.Button(menu_frame, text="Sign Up", command=sign_up).grid(row=0, column=0, padx=10)
ttk.Button(menu_frame, text="View All Records", command=view_records).grid(row=0, column=1, padx=10)
ttk.Button(menu_frame, text="Search Record", command=search_record).grid(row=0, column=2, padx=10)
ttk.Button(menu_frame, text="Exit", command=root.quit).grid(row=0, column=3, padx=10)

root.mainloop()
