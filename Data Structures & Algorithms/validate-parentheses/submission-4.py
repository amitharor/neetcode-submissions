class Solution:
    def isValid(self, s):
        if len(s) % 2:
            return False

        closing_brackets = {"}": "{", "]": "[", ")": "("}
        stack = []

        for bracket in s:
            if bracket in closing_brackets:
                if not stack or closing_brackets[bracket] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        return not stack
