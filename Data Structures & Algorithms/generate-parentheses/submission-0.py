'''
input: int
output:  return all well formed parentheses strings that we can generate with n pairs

constraints:
1 <= n <= 7

approach:
only add open parentheses if open < n 
only add a closing parentheses id closed < n
valid iff open == closed == open


time: O()
space: O()
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        results = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                results.append(''.join(stack))
                return

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()
        
        backtrack(0, 0)

        return results