# https://stackoverflow.com/a/20279566
def findNextCellToFill(grid, i, j):
    for x in range(i,9):
        for y in range(j,9):
            if grid[x][y] == 0:
                    return x,y
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                return x,y
    return -1,-1

def isValid(sudoku, i, j, num):
    # check verical and vertical
    for k in range(9):
        if sudoku[k][j] == num or sudoku[i][k] == num:
            return False
    # check box
    box = (3 * (i//3), 3* (j//3))
    for k in range(3):
        for l in range(3):
            if sudoku[box[0] + k][box[1] + l] == num:
                return False
    return True

def solveSudoku(grid, i=0, j=0):
    i,j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1,10):
        if isValid(grid,i,j,e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False

def solve_obvious(grid):
    # solves by logic
    nums = set(range(1, 10))
    repeat = True
    while repeat:
        repeat = False  # repeat only if a cell was solved
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    possible = (nums 
                    - set([grid[i][x] for i in range(9)]) # horizontal
                    - set([grid[y][i] for i in range(9)]) # verical
                    - set(grid[i][j] for i in range((y//3)*3, ((y//3)*3)+3) for j in range((x//3)*3, ((x//3)*3)+3))) # 3x3 box
                    if len(possible) == 1:
                        grid[y][x] = list(possible)[0]
                        repeat = True

with open('storage//96_sudokus.txt','r') as f:
    lines = f.readlines()
    sudokus = [[[int(k) for k in lines[i+j].replace('\n','')] for j in range(1, 10)] for i in range(len(lines)) if 'Grid' in lines[i]]
result = 0
for sudoku in sudokus:
    solve_obvious(sudoku)
    solveSudoku(sudoku)
    result += sudoku[0][0]*100 + sudoku[0][1]*10 + sudoku[0][2]
print(result)