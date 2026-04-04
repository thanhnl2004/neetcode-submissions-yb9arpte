class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if i not in range(rows) or j not in range(cols) or grid[i][j] == '0' or (i, j) in visited:
                return

            visited.add((i, j))

            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in directions:
                dfs(i + dr, j + dc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    dfs(i, j)

        return count


        