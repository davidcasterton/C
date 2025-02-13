from typing import Optional

class Solution:
    def __init__(self):
        self.__grid: Optional[List[List[str]]] = None
        self.__M: Optional[int] = None
        self.__N: Optional[int] = None
        self.__visited: Optional[List[List[str]]] = None

        self.num_islands = 0

    @property
    def grid(self):
        if self.__grid == None:
            assert AssertionError('grid is undefined')
        return self.__grid

    @grid.setter
    def grid(self, grid):
        self.__grid = grid
        self.__M = len(grid)
        self.__N = len(grid[0])
        self.__visited = [[False] * self.N for _ in range(self.M)]

    @property
    def M(self):
        if self.__M == None:
            assert AssertionError('M is undefined')
        return self.__M

    @property
    def N(self):
        if self.__N == None:
            assert AssertionError('N is undefined')
        return self.__N

    @property
    def visited(self):
        if self.__visited == None:
            assert AssertionError('visited is undefined')
        return self.__visited

    @visited.setter
    def visited(self, vals):
        m, n, val = vals
        self.__visited[m][n] = val


    def recursive_is_island(self, m, n, expansion=False):
        if not (0 <= m < self.M) or not (0 <= n < self.N):
            return
        if self.visited[m][n]:
            return
        print(m,n)

        self.visited = (m, n, True)

        if self.grid[m][n] == "1":
            if not expansion:
                self.num_islands += 1

            neighbors = [[m, n-1], [m, n+1], [m-1, n], [m+1, n]]
            for _m, _n in neighbors:
                self.recursive_is_island(_m, _n, expansion=True)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0 # handle empty dimensions

        self.grid = grid

        for m in range(self.M):
            for n in range(self.N):
                self.recursive_is_island(m, n)

        return self.num_islands
