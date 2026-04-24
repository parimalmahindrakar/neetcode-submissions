class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis_mapping = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                popped_parenthesis = stack.pop()
                if popped_parenthesis != parenthesis_mapping[char]:
                    return False
        
        return len(stack) == 0
        