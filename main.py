from random import choice
import numpy as np
from os import system, name
from time import sleep


def clear():
    # For Windows
    if name == 'nt':
        _ = system('cls')

    # For Mac and Linux
    else:
        _ = system('clear')


def board_setup():
    board = '''┏━━━━━┳━━━━━┳━━━━━┓
┃  x  ┃  x  ┃  x  ┃
┣━━━━━╋━━━━━╋━━━━━┫
┃  x  ┃  x  ┃  x  ┃
┣━━━━━╋━━━━━╋━━━━━┫
┃  x  ┃  x  ┃  x  ┃
┗━━━━━┻━━━━━┻━━━━━┛'''

    board_index_list = []

    i = 0
    for char in board:
        if char == "x":
            board_index_list.append(i)
        i += 1

    return board_index_list


def user_input(available_cells, player_cells):
    return player_cell


def select_spot(game_board, board_index, char):
    game_board = game_board[:board_index] + game_board[board_index:].replace(' ', f'{char}', 1)

    return game_board


def check_win(cells):
    board_matrix = np.array([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]])

    # Checks cells against each row, column, and diagonal. Must get three in a row to win.
    for i in range(3):
        for array in [board_matrix[i], board_matrix[:, i], board_matrix.diagonal(), np.fliplr(board_matrix).diagonal()]:
            win = all(cell in cells for cell in array)
            if win:
                return win


def play_game():
    board_index_list = board_setup()

    num_board = '''┏━━━━━┳━━━━━┳━━━━━┓
┃  1  ┃  2  ┃  3  ┃
┣━━━━━╋━━━━━╋━━━━━┫
┃  4  ┃  5  ┃  6  ┃
┣━━━━━╋━━━━━╋━━━━━┫
┃  7  ┃  8  ┃  9  ┃
┗━━━━━┻━━━━━┻━━━━━┛'''

    game_board = '''┏━━━━━┳━━━━━┳━━━━━┓
┃     ┃     ┃     ┃
┣━━━━━╋━━━━━╋━━━━━┫
┃     ┃     ┃     ┃
┣━━━━━╋━━━━━╋━━━━━┫
┃     ┃     ┃     ┃
┗━━━━━┻━━━━━┻━━━━━┛'''

    clear()

    # Player selects X or O. Computer gets the other option.
    char_choices = "XO"
    player_char = input("Choose X or O: ")
    cpu_char = char_choices.replace(player_char, "")
    while player_char not in char_choices:
        print("Invalid input. Try again.")
        player_char = input("X or O? ")
        cpu_char = char_choices.replace(player_char, "")

    player_cells = []
    cpu_cells = []

    available_cells = list(range(1, 10))

    print(num_board)

    while not check_win(cpu_cells):

        while True:
            try:
                player_cell = int(input("Select a spot: "))
                if isinstance(player_cell, int):
                    break
            except ValueError:
                print("Invalid input. Try again.")

        if player_cell in available_cells:
            player_cells.append(player_cell)
        while player_cell not in available_cells:
            print("Invalid input. Try again.")
            player_cell = int(input("Select a spot: "))
            player_cells.append(player_cell)
        game_board = select_spot(game_board, board_index_list[player_cell - 1], player_char)
        available_cells.remove(player_cell)

        if check_win(player_cells):
            clear()
            print(game_board)
            print("You win!\n")
            break

        if len(available_cells) == 0:
            clear()
            print(game_board)
            print("It's a draw!\n")
            break

        # How can I make a smart CPU?
        cpu_cell = choice(available_cells)
        cpu_cells.append(cpu_cell)
        game_board = select_spot(game_board, board_index_list[cpu_cell - 1], cpu_char)
        available_cells.remove(cpu_cell)

        clear()
        print(game_board)

    if check_win(cpu_cells):
        clear()
        print(game_board)
        print("You lose!\n")

    play_again_choices = "yn"
    play_again = input("Play again? (Y/N) ")
    while play_again.lower() not in play_again_choices:
        play_again = input("Play again? (Y/N) ")

    if play_again.lower() == "y":
        play_game()


if __name__ == '__main__':
    play_game()
