class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        buildings = []

        # locate buildings
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    buildings.append((r,c))

        # bfs calculate distance from each buildin to empty lands
        def bfs(r,c) -> List[List[int]]:
            visited = [[False]*N for _ in range(M)]
            distances = [[-1]*N for _ in range(M)]
            q = collections.deque([(r,c,0)])
            while q:
                r,c,d = q.popleft()
                neighbors = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
                for _r, _c in neighbors:
                    if 0<=_r<M and 0<=_c<N and grid[_r][_c]==0 and not visited[_r][_c]:
                        visited[_r][_c] = True
                        distances[_r][_c] = d+1
                        q.append((_r,_c,d+1))
            return distances

        distances = {}
        for r,c in buildings:
            distances[(r,c)] = bfs(r,c)

        # calculate distances from each cell to buildings
        answer = [-1, -1, -1] # distance, row, column
        for r in range(M):
            for c in range(N):
                if grid[r][c] in [1,2]:
                    continue
                tot_dist = 0
                blocked = False
                for _r,_c in buildings:
                    if distances[(_r,_c)][r][c] == -1:
                        blocked = True
                        break
                    tot_dist += distances[(_r,_c)][r][c]

                if not blocked and (tot_dist < answer[0] or answer[0] == -1):
                    answer = [tot_dist, r, c]

        return answer[0]
