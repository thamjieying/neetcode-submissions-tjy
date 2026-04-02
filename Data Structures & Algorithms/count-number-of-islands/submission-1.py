class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(grid, row, col):
            grid[row][col] = '0'
            directions = ((0,1), (0,-1), (1,0), (-1,0))

            for dr, dc in directions: 
                r = dr + row
                c = dc + col

                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
                    dfs(grid, r, c)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(grid, r, c)
                    island_count += 1

        return island_count