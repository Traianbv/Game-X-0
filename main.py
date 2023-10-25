
print("""###########TIC-TAC-TOE-############""")



#Game board Data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#Display board function
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")

curent_player = "X"

#Ask player to choose a spot
def player1(player):

    print(f"current playes {player}")

    position = input("Choose a spot ! ")

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Choose a position from 1-9: ")

    position = int(position) -1

    board[position] = player

#Change player
def flip_player():
    global curent_player
    if curent_player == "X":
        curent_player = "O"
    elif curent_player == "O":
        curent_player = "X"

#check data in game , row , columns , diagonals
def check_row():

    global game_on

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_on = False
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]


def check_columns():
    global game_on

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_on = False
        if col_1:
            return board[0]
        elif col_2:
            return board[1]
        elif col_3:
            return board[2]


def check_diagonal():
    global game_on

    dig_1 = board[0] == board[4] == board[8] != "-"
    dig_2 = board[6] == board[4] == board[2] != "-"

    if dig_1 or dig_2:
        game_on = False
        if dig_1:
            return board[0]
        elif dig_2:
            return board[6]

#check de status of the game win or draw
def check_the_game():
    check_if_win()
    check_if_draw()

def check_if_win():
    global game_on
    global winner

    row_winner = check_row()
    column_winner = check_columns()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_if_draw():

    if "-" not in board:
        global game_on
        game_on = False
        if check_if_win() == None:
            display_board()
            print("Draw !")
        else:
            pass



game_on = True

winner = None

#Game start
while game_on:
    
    display_board()
    player1(curent_player)
    check_the_game()
    flip_player()



    if winner == "X" or winner == "O":
        display_board()
        print(f"{winner} Won !")



