class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = set()

        if not grid:
            return 0

        def dfs(i, j):
            if not i in range(rows) or not j in range(cols) or grid[i][j] != '1' or (i, j) in visited:
                return
            visited.add((i, j))
            
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(i + dr, j + dc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not (i, j) in visited:
                    dfs(i, j)
                    count += 1

        return count
        
        