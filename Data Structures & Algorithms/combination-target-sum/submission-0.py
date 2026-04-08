class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, curr: List[int], total: int):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target: 
                return
            
            # path 1: include current number
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            # path2: don't include number
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0,[],0)
        return res

