import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.player_labels = {}
        self.create_player_display()
        self.create_board()
        self.update_player_display()

    def create_player_display(self):
        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0, columnspan=3, pady=10)
        self.player_labels["X"] = tk.Label(frame, text="Player X", font=('Arial', 18), fg="blue", padx=20, pady=5)
        self.player_labels["O"] = tk.Label(frame, text="Player O", font=('Arial', 18), fg="red", padx=20, pady=5)
        self.player_labels["X"].pack(side=tk.LEFT, padx=10)
        self.player_labels["O"].pack(side=tk.LEFT, padx=10)

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=('Arial', 40), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_click(i, j), bg="white", activebackground="#e0e0e0")
                button.grid(row=i+1, column=j)  # shift down by 1 row for player display
                self.buttons[i][j] = button

    def on_click(self, i, j):
        if self.buttons[i][j]["text"] == "" and not self.check_winner():
            self.buttons[i][j]["text"] = self.current_player
            # Set color for each player
            if self.current_player == "X":
                self.buttons[i][j]["fg"] = "blue"
            else:
                self.buttons[i][j]["fg"] = "red"
            if self.check_winner():
                self.update_player_display()
                self.animate_winner(self.current_player)
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_draw():
                self.update_player_display()
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_player_display()
    def update_player_display(self):
        # Animate/highlight the current player
        for player, label in self.player_labels.items():
            if player == self.current_player:
                label.config(bg="#ffff99", font=('Arial', 20, 'bold'))  # highlight
            else:
                label.config(bg=self.root.cget('bg'), font=('Arial', 18))

    def animate_winner(self, winner):
        # Simple flash animation for winner label
        label = self.player_labels[winner]
        def flash(count=6):
            if count > 0:
                current_bg = label.cget("bg")
                label.config(bg="#ffcccb" if current_bg != "#ffcccb" else "#ffff99")
                self.root.after(200, flash, count-1)
            else:
                label.config(bg="#ffff99")
        flash()

    def check_winner(self):
        board = [[self.buttons[i][j]["text"] for j in range(3)] for i in range(3)]
        # Check rows, columns, and diagonals
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return True
            if board[0][i] == board[1][i] == board[2][i] != "":
                return True
        if board[0][0] == board[1][1] == board[2][2] != "":
            return True
        if board[0][2] == board[1][1] == board[2][0] != "":
            return True
        return False

    def is_draw(self):
        return all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["fg"] = "black"
        self.current_player = "X"
        self.update_player_display()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()