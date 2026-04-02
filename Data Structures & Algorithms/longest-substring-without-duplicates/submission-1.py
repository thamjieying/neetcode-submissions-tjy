class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        start = 0
        max_string_len = 0

        for end_index, end_char in enumerate(s):
            print(end_char, end_index)
            if end_char in char_set:
                max_string_len = max(max_string_len, end_index - start)

                while s[start] != end_char:
                    char_set.remove(s[start])
                    start +=1
                start+=1
                
            else: 
                char_set.add(end_char)

        return max(max_string_len, len(s) - start)

