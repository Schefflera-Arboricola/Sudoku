import random
import copy

def is_valid(board, row, col, num):
    # Check if 'num' is not already in the current row, column, or 3x3 subgrid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                l=list(range(1, 10))
                random.shuffle(l)
                for num in l:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack if the current placement is invalid
                return False
    return True

def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    solve_sudoku(board)
    return board

def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid_sudoku(board):
    def is_valid_row(row):
        seen = set()
        for num in row:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True

    def is_valid_col(col):
        seen = set()
        for row in board:
            num = row[col]
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True

    def is_valid_box(row, col):
        seen = set()
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                num = board[i][j]
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
        return True

    # Check rows and columns
    for i in range(9):
        if not is_valid_row(board[i]) or not is_valid_col(i):
            return False

    # Check 3x3 boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_valid_box(i, j):
                return False

    return True

def remove_numbers(board_, num_to_remove):
    board = copy.deepcopy(board_)
    # Create a list of unique cells (row, col) to ensure we don't remove the same cell twice
    cells = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(cells)
    
    for row, col in cells:
        temp = board[row][col]
        board[row][col] = 0
        
        # Check if the puzzle still has a unique solution after removing a number
        temp_board = copy.deepcopy(board)
        if solve_sudoku(temp_board):
            num_to_remove -= 1  # Decrease the count of numbers to remove
            if num_to_remove == 0:
                break
        else:
            board[row][col] = temp  # Restore the number if it's needed
        
    return board

'''
if __name__ == "__main__":
    for _ in range(5):
        random.seed()  # Seed the random number generator with the current system time
        sudoku_grid = generate_sudoku()
        
        print("Generated Sudoku Grid:")
        print_sudoku(sudoku_grid)

        # Check if the Sudoku board is valid
        isValid = is_valid_sudoku(sudoku_grid)
        print(isValid)  # Output should be True if the board is valid

        print()

        print("Generated Sudoku Puzzle:")
        modified_board = remove_numbers(sudoku_grid, num_to_remove=50)
        print_sudoku(modified_board)

        print()
        print()
'''