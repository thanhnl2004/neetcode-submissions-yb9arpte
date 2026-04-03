class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return [[]]

        visited = set()

        start_color = image[sr][sc]
        rows, cols = len(image), len(image[0])

        def dfs(i, j):
            if i not in range(rows) or j not in range(cols) or image[i][j] != start_color or (i, j) in visited:
                return
            image[i][j] = color
            visited.add((i, j))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(i + dr, j + dc)
            
        dfs(sr, sc)

        return image


