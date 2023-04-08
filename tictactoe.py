import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [' '] * 9
        self.current_player = 'X'
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.master, text=' ', font=('Roman', 20), width=12, height=3,
                                   command=lambda x=i, y=j: self.button_click(x, y))
                button.grid(row=i, column=j, sticky=tk.NSEW)
                row.append(button)
            self.buttons.append(row)

        self.reset_button = tk.Button(self.master, text='Reset', font=('Arial', 20), width=6, height=1,
                                      command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky=tk.NSEW)

        self.turn_label = tk.Label(self.master, text="Player X's turn", font=('Arial', 20))
        self.turn_label.grid(row=4, column=0, columnspan=3, sticky=tk.NSEW)

    def button_click(self, x, y):
        if self.board[x * 3 + y] == ' ':
            self.buttons[x][y].config(text=self.current_player)
            self.board[x * 3 + y] = self.current_player
            if self.check_win():
                self.disable_buttons()
                self.turn_label.config(text=f"Player {self.current_player} wins!")
            elif self.check_tie():
                self.disable_buttons()
                self.turn_label.config(text="It's a tie!")
            else:
                self.switch_player()
                self.turn_label.config(text=f"Player {self.current_player}'s turn")

    def reset(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', state=tk.NORMAL)
        self.turn_label.config(text="Player X's turn")

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_win(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def check_tie(self):
        return ' ' not in self.board

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk()
    tictactoe = TicTacToe(root)
    root.mainloop()
