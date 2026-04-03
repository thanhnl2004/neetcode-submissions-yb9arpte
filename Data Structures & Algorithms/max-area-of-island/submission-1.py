class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        if not grid:
            return 0

        def calculateArea(i, j):
            if i not in range(rows) or j not in range(cols) or grid[i][j] != 1 or (i, j) in visited:
                return 0
            visited.add((i, j))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            area = 1 # current cell
            for dr, dc in directions:
                area += calculateArea(i + dr, j + dc)
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(maxArea, calculateArea(i, j))

        return maxArea

        
        