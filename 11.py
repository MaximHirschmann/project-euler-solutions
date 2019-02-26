import Utils

class Grid:
    def __init__(self, grid, adjacant_digits = 4):
        self.grid = grid
        self.adjacant_digits = adjacant_digits
        self.max = 0
    
    def max_grid(self):
        def max_right(self):
            for i in range(len(self.grid)):
                for j in range(len(self.grid[0])-self.adjacant_digits+1):
                    prod = Utils.product(self.grid[i][j+k] for k in range(self.adjacant_digits))
                    if prod > self.max:
                        self.max = prod
        def max_down(self):
            for i in range(len(self.grid)-self.adjacant_digits+1):
                for j in range(len(self.grid[0])):
                    prod = Utils.product(self.grid[i+k][j] for k in range(self.adjacant_digits))
                    if prod > self.max:
                        self.max = prod
        def max_diagonal_left(self):
            for i in range(self.adjacant_digits-1, len(grid)-self.adjacant_digits+1):
                for j in range(self.adjacant_digits-1,len(self.grid[0])):
                    prod = Utils.product(self.grid[i-k][j-k] for k in range(self.adjacant_digits))
                    print(prod)
                    if prod > self.max:
                        self.max = prod
        def max_diagonal_right(self):
            for i in range(len(grid)-self.adjacant_digits+1):
                for j in range(len(self.grid[0])-self.adjacant_digits+1):
                    prod = Utils.product(self.grid[i-k][j+k] for k in range(self.adjacant_digits))
                    if prod > self.max:
                        self.max = prod
        max_right(self)
        max_down(self)
        max_diagonal_left(self)
        max_diagonal_right(self)
        return self.max


grid = [[int(i) for i in line.replace("\n","").split(" ")] for line in open("storage//11.txt","r")]

g = Grid(grid)
print(g.max_grid())
