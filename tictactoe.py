import tkinter as tk
from PIL import Image, ImageTk
import subprocess

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.center_window(900, 500)
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.buttons = []
        self.score_x = 0
        self.score_o = 0

        self.root.configure(bg="black")

        self.bg_image = Image.open("img/planet.jpg")
        self.bg_image = self.bg_image.resize((900, 500))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        self.back_button = tk.Button(self.root, text="Back", font=("Courier", 12), width=10, command=self.go_back, bg="black", fg="white")
        self.back_button.place(x=10, y=10)

        self.board_frame = tk.Frame(self.root, bg="black")
        self.board_frame.place(relx=0.5, rely=0.4, anchor="center")

        self.create_board()
        self.show_rules()
        
    def show_rules(self):
        popup = tk.Toplevel(self.root)
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
            text="Two players take turns marking X or O in an empty cell. The first player to get three in a row (horizontal, vertical, or diagonal) wins!",
            font=("Courier", 12),
            wraplength=500
        )
        label.pack(pady=30)

        go_button = tk.Button(popup, text="Got it!", command=popup.destroy, font=("Courier", 12), width=10, borderwidth=3)
        go_button.pack(pady=10)

        popup.transient(self.root)
        popup.grab_set()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.board_frame, text="", font=("Arial", 24), width=5, height=2, borderwidth=5, command=lambda i=i, j=j: self.make_move(i, j))
                btn.grid(row=i, column=j)
                self.buttons.append(btn)

        self.status_label = tk.Label(self.root, text="Player X's turn", font=("Courier", 14), bg="black", fg="white")
        self.status_label.place(relx=0.5, rely=0.80, anchor="center")

        self.score_label = tk.Label(self.root, text=f"Score - X: {self.score_x} | O: {self.score_o}", font=("Courier", 14), bg="black", fg="white")
        self.score_label.place(relx=0.5, rely=0.85, anchor="center")

        self.reset_button = tk.Button(self.root, text="Reset", font=("Courier", 14), bg="black", fg="white", command=self.reset_game)
        self.reset_button.place(relx=0.5, rely=0.90, anchor="center")

    def make_move(self, i, j):
        index = i * 3 + j
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                self.status_label.config(text=f"Player {self.current_player} wins!")
                self.update_score()
                self.disable_buttons()
            elif "" not in self.board:
                self.status_label.config(text="It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        winning_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "":
                return True
        return False

    def update_score(self):
        if self.current_player == "X":
            self.score_x += 1
        else:
            self.score_o += 1
        self.score_label.config(text=f"Score - X: {self.score_x} | O: {self.score_o}")

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def enable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.NORMAL)

    def reset_game(self):
        self.enable_buttons()
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        for button in self.buttons:
            button.config(text="")
        self.status_label.config(text="Player X's turn")

    def go_back(self):
        self.root.destroy()
        subprocess.run(["python", "menu.py"])

    def center_window(self, width=900, height=500):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
