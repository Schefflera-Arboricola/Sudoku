from sudoku import *

num_to_remove = 30
solved_sudoku = generate_sudoku()
sudoku_puzzle = remove_numbers(solved_sudoku, num_to_remove)

def generate_new_sudoku():
    global solved_sudoku, sudoku_puzzle
    num_to_remove = 30
    solved_sudoku = generate_sudoku()
    sudoku_puzzle = remove_numbers(solved_sudoku, num_to_remove)
    return solved_sudoku,sudoku_puzzle