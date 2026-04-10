class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {'(': ')', '{': '}', '[' : ']'}
        stack = []

        for bracket in s: 
            if bracket in char_map.keys():
                stack.append(bracket)
            elif stack: 
                start_bracket = stack.pop()
                if bracket != char_map[start_bracket]:
                    return False
            else: 
                return False
        return not stack
