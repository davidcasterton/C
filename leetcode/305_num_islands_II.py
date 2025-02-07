class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.positions = []

    # def expand_island(self, grid, r, c, visited):
    #     # expands visited cells to all neighbors of island
    #     visited[r][c] = True
    #     neighbors = [(r+1, c), (r-1,c), (r,c+1), (r,c-1)]
    #     for _r,_c in neighbors:
    #         if not 0<=_r<self.m or not 0<=_c<self.n:
    #             continue # out of grid
    #         if grid[_r][_c] == 1 and not visited[_r][_c]:
    #             visited[_r][_c] = True
    #             self.expand_island(grid, _r, _c, visited)
    #         else:
    #             visited[_r][_c] = True
    #     return visited

    def is_new(self, grid, r, c) -> bool:
        # is new island if all neighbors are empty
        neighbors = [(r+1, c), (r-1,c), (r,c+1), (r,c-1)]
        new = True
        for _r,_c in neighbors:
            if not 0<=_r<self.m or not 0<=_c<self.n:
                continue # out of grid
            if grid[_r][_c] == 1:
                new = False
                break
            else:
                new = True
        return new

    # def numIslands(self, grid: List[List[int]], r, c, num_islands) -> int:
    #     visited = [[False]*self.n for _ in range(self.m)]
    #     answer = 0

    #     for r in range(self.m):
    #         for c in range(self.n):
    #             if grid[r][c] == 1 and not visited[r][c]:
    #                 answer += 1
    #                 visited = self.expand_island(grid, r, c, visited)
    #     return answer

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # handle empty dimensions
        if len(positions) == 0:
            return 0
        self.m = m
        self.n = n
        self.positions = positions

        # init data structures
        grid = [[0]*n for _ in range(m)]
        num_islands = 0
        answer = []
        for i in range(len(positions)):
            r,c = positions[i]
            if grid[r][c] == 0 and self.is_new(grid, r, c):
                num_islands += 1
            grid[r][c] = 1
            answer.append(num_islands)

        return answer
