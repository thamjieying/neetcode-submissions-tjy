class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 1
        current_sum = nums[0]
        target_min_length = float("inf")

        while start < end and end <= len(nums):
            if current_sum < target: 
                current_sum += nums[end] if end < len(nums) else 0
                end +=1
            
            else: 
                curr_sum_len = end - start
                target_min_length = min(target_min_length, curr_sum_len)
                current_sum -= nums[start]
                start +=1

        return target_min_length if target_min_length != float("inf") else 0