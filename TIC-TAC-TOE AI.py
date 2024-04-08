import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []

        # Define colors
        color_x = "red"
        color_o = "blue"
        background_color = "light gray"
        button_color = "white"

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", width=8, height=3, bg=button_color,
                                   font=('Helvetica', 24), command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

        self.root.configure(bg=background_color)
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart, bg=button_color,
                                        font=('Helvetica', 14))
        self.restart_button.grid(row=3, column=0, columnspan=3, sticky="WE", padx=10, pady=10)

    def on_button_click(self, i, j):
        index = 3 * i + j
        if self.board[index] == " ":
            self.board[index] = self.current_player
            if self.current_player == "X":
                self.buttons[index].config(text="X", fg='red')
            else:
                self.buttons[index].config(text="O", fg='blue')
                
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.restart()
            elif " " not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.restart()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.computer_move()

    def computer_move(self):
        empty_indices = [i for i in range(9) if self.board[i] == " "]
        if empty_indices:
            index = random.choice(empty_indices)
            self.board[index] = "O"
            self.buttons[index].config(text="O", fg='blue')
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", "Computer wins!")
                self.restart()
            elif " " not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.restart()
            else:
                self.current_player = "X"

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return True
            if self.board[3 * i] == self.board[3 * i + 1] == self.board[3 * i + 2] != " ":
                return True
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def restart(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ", fg='black')
        messagebox.showinfo("Tic Tac Toe", "Game has been restarted!")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
