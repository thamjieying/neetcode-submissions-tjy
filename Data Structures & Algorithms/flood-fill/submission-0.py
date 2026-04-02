class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        def dfs(image, row, col, target, original):
            image[row][col] = target
            directions = ((0,1), (0,-1), (1,0), (-1,0))

            for dr, dc in directions: 
                r = dr + row
                c = dc + col 

                if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == original:
                    dfs(image, r, c, target, original)
                
        
        dfs(image, sr, sc, color, image[sr][sc])

        return image