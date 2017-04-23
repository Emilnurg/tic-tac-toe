# Tic-Tac-Toe
# Plays the game of tic-tac-toe against a human opponent
   
# global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "НИЧЬЯ"
NUM_SQUARES = 10


def display_instruct():
    """Выводит на экран инструкцию для игрока."""  
    print(
    """
    Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен.
Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики".

Чтобы сделать ход. введи число от О до 8. Числа однозначно соответствуют полям
доски - так. как показано ниже:\n
    
                    7 | 8 | 9
                    ---------
                    4 | 5 | 6
                    ---------
                    1 | 2 | 3

Приготовься к бою. жалкий белковый человечишка. Вот-вот начнется решающее сражение.\n
    """
    )


def ask_yes_no(question):
    """Задает вопрос с ответом 'да' или 'нет'"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Просит ввести число из диапазона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Определяет принадлежность первого хода."""
    go_first = ask_yes_no("Xoчeшь оставить за собой первый ход? (y/n): ")
    if go_first == "y":
        print("\nHy что ж. даю тебе фору: играй крестиками.")
        human = X
        computer = O
    else:
        print("\nTвoя удаль тебя погубит.Буду начинать я.")
        computer = X
        human = O
    return computer, human


def new_board():
    """Создает новую игровую доску."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Отображает игровую доску на экране."""
    print("\n\t", board[7], "|", board[8], "|", board[9])
    print("\t", "---------")
    print("\t", board[4], "|", board[5], "|", board[6])
    print("\t", "---------")
    print("\t", board[1], "|", board[2], "|", board[3], "\n")


def legal_moves(board):
    """создает список доступных ходов"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Определяет победителя в игре"""
    WAYS_TO_WIN = ((1, 2, 3),
                   (4, 5, 6),
                   (7, 8, 9),
                   (3, 6, 9),
                   (1, 4, 7),
                   (2, 5, 8),
                   (1, 5, 9),
                   (3, 5, 7))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY: 
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def human_move(board, human):
    """Получает ход человека."""  
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Tвoй ход. Выбери одно из полей (1 - 9):", 1, NUM_SQUARES)
        if move not in legal:
            print("\nCмeшнoй человек! Это поле уже занято. Выбери дpyroe.\n")
    print("Ладно...")
    return move


def computer_move(board, computer, human):
    """Делает ход за компьютерного противника."""
    # make a copy to work with since function will be changing list
    board = board[:]
    # the best positions to have, in order
    BEST_MOVES = (5, 1, 3, 7, 9, 2, 4, 6, 8)

    print("Я выберу поле номер", end=" ")
    
    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY
    
    # if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checkin this move, undo it
        board[move] = EMPTY

    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X

    
def congrat_winner(the_winner, computer, human):
    """Поздравляет победителя игры"""
    if the_winner != TIE:
        print(the_winner, "выиграл!\n")
    else:
        print("Ничья\n")

    if the_winner == computer:
        print("Kaк я и предсказывал. победа в очередной раз осталась за мной.\n"
"Вот еще один довод в пользу того. что компьютеры превосходят людей решительно во всем.")

    elif the_winner == human:
        print("O нет. этого не может быть! Неужели ты как-то сумел перехитрить меня.\
белковый?\n"
"Клянусь: я. компьютер. не допущу этого больше никогда!")

    elif the_winner == TIE:
       print("Teбe несказанно повезло. дружок: ты сумел свести игру вничью.\n"
"Радуйся же сегодняшнему успеху! Завтра тебе уже не суждено его повторить.")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# start the program
main()

input("\n\nНажмите Enter. чтобы выйти.")
