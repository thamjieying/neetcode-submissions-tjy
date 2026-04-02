class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        unique_set = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in unique_set and l < len(s):
                unique_set.remove(s[l])
                l+=1
            
            unique_set.add(s[r])
            max_len = max(max_len, r - l +1)

        return max_len
