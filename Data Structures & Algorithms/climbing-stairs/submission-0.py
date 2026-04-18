class Solution:
    def climbStairs(self, n: int) -> int:
        lp_map = [ 0 for i in range(n+1)]
        lp_map[1] =1

        if n >= 2:
            lp_map[2] =2

        if n <= 2: 
            return lp_map[n]
        
        for i in range(3, n+1):
            lp_map[i] = lp_map[i-1] + lp_map[i-2]
        
        return lp_map[n]
