class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid) # rows
        N = len(grid[0]) # cols

        c: list[list[int]] = []
        for m in range(M):
            c.append([])
            for n in range(N):
                if m==0 and n==0:
                    # top row and left column
                    # print(f'top row and left column {m=} {n=} {c=}')
                    c[m].append(grid[m][n])
                elif n==0:
                    # left column
                    # print(f'left column {m=} {n=} {c=}')
                    c[m].append(c[m-1][n] + grid[m][n])
                elif m==0:
                    # top row
                    # print(f'top row {m=} {n=} {c=}')
                    c[m].append(c[m][n-1] + grid[m][n])
                else:
                    t = c[m-1][n]
                    l = c[m][n-1]
                    c[m].append(min([t,l]) + grid[m][n])
        # print(f'{c=}')
        return c[M-1][N-1]
