board = [1,2,3,4,5,6,7,8,9]

def check_win():
    win = False
    win_move = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )
    for pos in win_move:
        if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]:
            win = board[pos[0]]
    return win

#def check_move():
#    if (step == 9):
#        print("Ничья")
#    else:
#        print("Выйграл", check_win())


def draw_board():
    for i in range(3):
        print(board[i*3], board[1+i*3], board[2+i*3])



def game_step(move, char):
    if move > 10 or move < 1 or board[move-1] in ("X", "O"):
        return False

    board[move-1] = char
    return True



def game():
    player = "X"
    step = 0


    draw_board()

    while (step < 10) and (check_win() == False):
        move = int(input("Выберите куда сходить: "))
        if game_step(move, player):
            print("Верный ход")
            if player == "X":
                player = "O"
            else:
                player = "X"

            draw_board()
            step += 1

        else:
            print("Неверный ход")

    if step == 10:
        print("Ничья!")
    else:
        print("выйграл", check_win())

print("Добро пожаловать в Крестики-Нолики!")
game()
