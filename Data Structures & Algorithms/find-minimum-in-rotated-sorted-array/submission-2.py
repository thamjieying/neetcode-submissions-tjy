class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums)-1

        while l < r: 
            m = (l+r) //2
            if nums[l] <= nums[m] <= nums[r]:
                return nums[l]

            if nums[m] < nums[l]: # m is on the right sorted region 
                r = m
            else: # smallest value 
                l = m+1
        
        return  nums[l]
            