from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find all rotton fruit and put them in a queue
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fresh_fruit_count = 0
        directions = ((0,1), (0,-1), (1,0), (-1,0))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    fresh_fruit_count +=1    

        # deque and rot fruits
        while q: 
            current_min_fruit_count = len(q)
            has_new_rotton_fruit = False
            for _ in range(current_min_fruit_count):
                r, c = q.popleft()

                for dr, dc in directions: 
                    row = r + dr
                    col = c + dc

                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        has_new_rotton_fruit = True
                        grid[row][col] = 2
                        fresh_fruit_count -=1
                        q.append((row,col))
                    
            if has_new_rotton_fruit: 
                time += 1
        return time if fresh_fruit_count == 0 else -1
