import sys

class Grid:
    def __init__(self, grid, adjacant_digits = 4):
        self.grid = grid
        self.adjacant_digits = adjacant_digits
        self.max = 0
    
    def max_grid(self):
        def max_right(self):
            for i in range(len(self.grid)):
                for j in range(len(self.grid[0])-self.adjacant_digits+1):
                    product = 1
                    for k in range(self.adjacant_digits):
                        product *= self.grid[i][j+k]
                    if product > self.max:
                        self.max = product
        def max_down(self):
            for i in range(len(self.grid)-self.adjacant_digits+1):
                for j in range(len(self.grid[0])):
                    product = 1
                    for k in range(self.adjacant_digits):
                        product *= self.grid[i+k][j]
                    if product > self.max:
                        self.max = product
        def max_diagonal_left(self):
            for i in range(len(grid)-self.adjacant_digits+1):
                for j in range(self.adjacant_digits-1,len(self.grid[0])):
                    for k in range(self.adjacant_digits):
                        product = 1
                        for k in range(self.adjacant_digits):
                            product *= self.grid[i-k][j-k]
                        if product > self.max:
                            self.max = product
        def max_diagonal_right(self):
            for i in range(len(grid)-self.adjacant_digits+1):
                for j in range(len(self.grid[0])-self.adjacant_digits+1):
                    for k in range(self.adjacant_digits):
                        product = 1
                        for k in range(self.adjacant_digits):
                            product *= self.grid[i-k][j+k]
                        if product > self.max:
                            self.max = product
        max_right(self)
        max_down(self)
        max_diagonal_left(self)
        max_diagonal_right(self)

grid = []
with open(sys.path[0]+"/storage/11.txt","r") as f:
    for line in f:
        line_list = line.replace("\n","").split(" ")
        for i in range(len(line_list)):
            line_list[i] = int(line_list[i])
        grid.append(line_list)

g = Grid(grid)
g.max_grid()
print("Max:",g.max)