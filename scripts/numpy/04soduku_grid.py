# a sudoku square consists of a 9x9 grid with entries such that each row, col
# and each of the 9 non-overlapping 3x3 tiles contains the numbers 1-9 once
# only. The following program verifies that a provided grid is a valid Sudoku
# square

import numpy as np

def check_sudoku(grid):
    """ return True if grid is a valid Sudoku square, otherwise False"""
    for i in range(9):
        # j, k index top left hand corner of each 3x3 tile
        j, k = (i//3) * 3, (i%3) * 3
        if len(set(grid[i, :])) !=9 or len(set(grid[:, i])) !=9\
                  or len(set(grid[j:j+ 3, k:k+ 3].ravel())) !=9:
            return False
    return True

sudoku = """145327698
            839654127
            672918543
            496185372
            218473956
            753296481
            367542819
            984761235
            521839764"""

# turn the provided string, sudoku, into an integer array
grid = np.array([[int(i) for i in line] for line in sudoku.split()])
print(grid)

if check_sudoku(grid):
    print('grid valid')
else:
    print('grid invalid')
