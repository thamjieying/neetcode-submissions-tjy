
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        # build char map of s
        for s_char in s: 
            char_map[s_char] = char_map.get(s_char, 0) +1
        
        for t_char in t: 
            if t_char not in char_map: 
                return False

            char_map[t_char] -=1            
            if char_map[t_char] == 0: 
                del char_map[t_char]

        return not char_map
        
