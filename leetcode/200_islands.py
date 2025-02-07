class Solution:
    def __init__(self):
        self.grid: List[List[str]] = []
        self.rows = 0
        self.cols = 0
        self.visited: List[List[str]] = []
        self._numIslands = 0

    def isIsland(self, row, col):
        if self.visited[row][col]:
            return

        self.visited[row][col] = True

        # is island
        if self.grid[row][col] == "1":
            neighbors = [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]

            # check if new island
            newIsland = True
            for r,c in neighbors:
                if r == -1 or c == -1:
                    continue
                try:
                    if self.grid[r][c] == "1" and self.visited[r][c]:
                        newIsland = False
                except IndexError:
                    pass
            if newIsland:
                self._numIslands += 1

            # recursively expand to neighbors
            for r,c in neighbors:
                if r<0 or r>self.rows-1 or c<0 or c>self.cols-1:
                    continue
                self.isIsland(r,c)

    def numIslands(self, grid: List[List[str]]) -> int:
        # handle empty dimensions
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            # print('early exit')
            return 0

        # init data structures
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited: List[List[str]] = [[False] * self.cols for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                self.isIsland(r,c)

        return self._numIslands
