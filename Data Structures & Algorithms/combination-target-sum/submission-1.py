class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, combi, total):
            if total == target: 
                res.append(combi.copy())
                return 
            
            if index >= len(nums) or total > target:
                return 
            
            dfs(index,[*combi, nums[index]], total + nums[index])
            dfs(index+1, combi, total)
        
        dfs(0, [], 0)
        return res