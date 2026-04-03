class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxArea = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def calcArea(i, j):
            if i not in range(rows) or j not in range(cols) or grid[i][j] == 0 or (i, j) in visited:
                return 0
            visited.add((i, j))
            area = 1
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in directions:
                area += calcArea(i + dr, j + dc)
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = calcArea(i, j)
                    maxArea = max(maxArea, area)
        
        return maxArea
        