from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map = defaultdict(int)
    
        for i in range(len(s)):
            char_map[s[i]] +=1 
            char_map[t[i]] -=1

        for key, val in char_map.items():
            if val != 0: 
                return False
        
        return True