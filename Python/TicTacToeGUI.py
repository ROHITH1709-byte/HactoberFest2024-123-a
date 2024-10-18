import tkinter

def set_title(row, column):
    global currentPlayer, game_over
    
    if game_over or board[row][column]["text"] != "":
        return  # Spot already taken or game is over
    
    board[row][column]["text"] = currentPlayer
    
    # Switch player
    currentPlayer = playerO if currentPlayer == playerX else playerX
    label["text"] = f"{currentPlayer}'s turn"
    
    # Check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1
    
    # Horizontally check rows
    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != "":
            declare_winner(board[row][0]["text"], row, "horizontal")
            return
    
    # Vertically check columns
    for col in range(3):
        if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] and board[0][col]["text"] != "":
            declare_winner(board[0][col]["text"], col, "vertical")
            return
    
    # Diagonally check
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != "":
        declare_winner(board[0][0]["text"], 0, "diagonal")
        return
    
    # Anti-diagonally check
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != "":
        declare_winner(board[0][2]["text"], 2, "anti-diagonal")
        return
    
    # Tie
    if turns == 9:
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)

def declare_winner(winner, index, direction):
    global game_over
    label.config(text=f"{winner} is the winner!", foreground=color_yellow)
    
    if direction == "horizontal":
        for col in range(3):
            board[index][col].config(foreground=color_yellow, background=color_light_gray)
    elif direction == "vertical":
        for row in range(3):
            board[row][index].config(foreground=color_yellow, background=color_light_gray)
    elif direction == "diagonal":
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
    elif direction == "anti-diagonal":
        for i in range(3):
            board[i][2 - i].config(foreground=color_yellow, background=color_light_gray)
    
    game_over = True

def new_game():
    global game_over, turns, currentPlayer
    turns = 0
    game_over = False
    currentPlayer = playerX

    label.config(text=f"{currentPlayer}'s turn", foreground="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)

playerX = "X"
playerO = "O"
currentPlayer = playerX

# Initialize board with buttons
board = [[None for _ in range(3)] for _ in range(3)]

turns = 0
game_over = False

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"  # Fixed the typo here

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=f"{currentPlayer}'s turn", font=("Consolas", 20), background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"), background=color_gray, 
                                            foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_title(row, column))
        board[row][column].grid(row=row + 1, column=column)

button = tkinter.Button(frame, text="Restart", font=("Consolas", 20), background=color_gray, 
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# Center the window
window.update()
window_width = window.winfo_width() 
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# Format
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()
