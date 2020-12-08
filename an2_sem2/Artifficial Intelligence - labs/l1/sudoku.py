import math

# returns true if it exists same nr on the row, and false if not
def used_in_row(sudoku_grid, row, nr,n):
    for i in range(n):
        if sudoku_grid[row][i] == nr:
            return True
    return False


# returns true if it exists same nr on the column, and false if not
def used_in_col(sudoku_grid, col, nr,n):
    for i in range(n):
        if (sudoku_grid[i][col] == nr):
            return True
    return False


# returns true if it exists same nr in the box, and false if not
def used_in_box(sudoku_grid, row, col, nr,n):
    for i in range(int(math.sqrt(n))):
        for j in range(int(math.sqrt(n))):
            if sudoku_grid[i + row][j + col] == nr:
                return True
    return False

# finds first empty location (value of it is 0) and puts its coordinates in the list l
#returns false if there is no empty location
def find_empty_location(sudoku_grid, l,n):
    for row in range(n):
        for col in range(n):
            if sudoku_grid[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

# checks if it is ok to pun a value in that place
def check_location(arr, row, col, num,n):
    return not used_in_row(arr, row, num,n) and not used_in_col(arr, col, num,n) and not used_in_box(arr, row - row % (int(math.sqrt(n))), col - col % int(math.sqrt(n)), num,n)

# solves the sudoku, using backtracking
def solve(sudoku_grid,n):

    position_list = [0, 0]

    if (not find_empty_location(sudoku_grid, position_list,n)):
        return True

    row = position_list[0]
    col = position_list[1]

    for nr in range(1, n+1):

        if (check_location(sudoku_grid, row, col, nr,n)):
            sudoku_grid[row][col] = nr

            if (solve(sudoku_grid,n)):
                return True

            sudoku_grid[row][col] = 0

    return False

# prints the sudoku grid
def print_sudoku(sudoku_grid,n):
    for i in range(n):
        for j in range(n):
            print(sudoku_grid[i][j],end=" ")
        print('')

n=9
sudoku_grid = [[0 for x in range(n)] for y in range(n)]

sudoku_grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

choice=int(input("Trials: "))
while choice>0:
    print()
    print()
    print()
    print()
    if (solve(sudoku_grid,n)):
        print_sudoku(sudoku_grid,n)
    else:
        print("No solution")
    choice-=1