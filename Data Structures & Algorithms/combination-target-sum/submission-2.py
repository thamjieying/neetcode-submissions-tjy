class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, combi, total):
            if total == target: 
                res.append(combi.copy())
                return
            
            if i >= len(nums):
                return 
            
            if total > target: 
                return 
            
            dfs(i, [*combi, nums[i]], total+ nums[i])
            dfs(i+1, combi.copy(), total)
        
        dfs(0, [], 0)
        return res

