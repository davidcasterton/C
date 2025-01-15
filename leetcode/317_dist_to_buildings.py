class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return -1
        rows = len(grid)
        cols = len(grid[0])

        # locate buildings
        buildings = [] # [(row, col), ...]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    buildings.append((r,c))
        print(buildings)

        def bfs(r0,c0):
            visited = [[False]*cols for _ in range(rows)]

            q = collections.deque([(r0,c0,0)])
            while q:
                r,c,d = q.popleft()
                neighbors = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
                for _r, _c in neighbors:
                    if 0<=_r<rows and 0<=_c<cols and grid[_r][_c]==0 and not visited[_r][_c]:
                        visited[_r][_c] = True
                        distances[(r0,c0)][_r][_c] = d+1
                        q.append((_r, _c, d+1))

        # calculate distances from each building to empty land
        # keys: [row, col] of building
        # values: List[List[int]] with distance for each empty land
        distances = {}
        for r,c in buildings:
            distances[(r,c)] = [[-1]*cols for _ in range(rows)]
            bfs(r,c)

        # calculate distance to buildings from each cell
        min_dist = [-1, -1, -1] # dist, row, col
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] in [1,2]:
                    continue
                tot_dist = 0
                blocked = False
                for _r, _c in buildings:
                    # tot_dist += abs(r-_r) + abs(c-_c)
                    if distances[(_r,_c)][r][c] == -1:
                        blocked = True
                        break # cannot navigate to building
                    tot_dist += distances[(_r,_c)][r][c]

                if not blocked and (tot_dist < min_dist[0] or min_dist[0] == -1):
                    min_dist = [tot_dist, r, c]

        return min_dist[0]
