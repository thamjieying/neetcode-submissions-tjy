class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0

        rows = len(grid)
        cols = len(grid[0])
        

        def dfs(grid, row, col):
            directions = ((-1,0), (1,0), (0,1), (0,-1))
            grid[row][col] = '0'
            for dr, dc in directions:
                r = dr + row    
                c = dc + col 

                if 0 <= r < rows and 0 <= c < cols and grid[r][c] =='1':
                    dfs(grid, r, c)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    island_count +=1
                    dfs(grid, row, col)
        return island_count